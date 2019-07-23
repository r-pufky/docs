[Gitea][3e]
===========
[A community managed fork of gitea.][i2] This provides a github-like service for
private repository use. Can be exposed and used publicly as well.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Initial Setup](#initial-setup)
1. [Importing Git Repositories](#importing-git-epositories)
1. [SSL Client Cert Authentication](#ssl-client-cert-authentication)

Ports
-----
Docker reverse-proxy.

| Docker Port | Protocol | Exposed/Public | Purpose                 |
|-------------|----------|----------------|-------------------------|
| 3000        | TCP      | Exposed        | http/https connections. |

Important File Locations
------------------------
Relative to docker container.

| File                              | Purpose            |
|-----------------------------------|--------------------|
| /data/services/gitea/conf/app.ini | Settings.          |
| /data/services/gitea/git          | Git repo location. |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
git repository.

* `:1` will use the [latest stable version of gitea][od].
* You may specify your own git repository location.

Docker Compose:
```yaml
gitea:
  image: gitea/gitea:1
  restart: unless-stopped
  environment:
    - USER_UID=1001
    - USER_GID=1001
    - RUN_MODE=prod
    - DISABLE_SSH=true
    - ROOT_URL='https://{YOUR SUBDOMMAIN OR DOMAIN/PATH}/'
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/gitea:/data
    - /data/git/gitea:/data/git/repositories
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref9s] for more details.

### Using Subdomains
This requires a hard IP resolution. Hairpin NAT / NAT reflection will result in
the web front working but git pull/push/clones failing. This is due to the way
gitea [handles these requests with custom written handlers][fp]. Setup DNS
resolution or add to `hosts` file.

[nginx/conf.d/reverse-proxy.conf][fi] `root:root 0644`
```nginx
server {
  listen 443 ssl http2;
  server_name gitea.<DOMAIN> gitea;

  location / {
    proxy_pass http://gitea:3000;
    client_max_body_size 1024m;
  }
}
```
* [proxy-control.conf][refv3] contains default proxy settings. Reload nginx.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][fi] `root:root 0644`
```nginx
server {
  location /gitea/ {
    proxy_pass http://gitea:3000/;
    client_max_body_size 1024m;
  }
}
```
* [proxy-control.conf][refv3] contains default proxy settings. Reload nginx.
* Adjust `client_max_body_size` to expected max size of data in a git change.

Initial Setup
-------------
This will initially setup gitea with restricted permissions during
configuration:
```
{REVERSE PROXY URI}/install
```

Database Settings:
* Database: `sqlite3`
* Path `/data/gitea/gitea.db`

General Settings:
* Site Title: {YOUR SITE NAME}
* Repository Root Path: `/data/git/repositories`
* Git LFS Root Path: `/data/git/lfs`
* Run As Username: `git`
* SSH Server Domain: `localhost`
* SSH Server Port: `22`
* Gitea HTTP Listen Port: `3000`
* Gitea Base URL: `https://{YOUR SUBDOMMAIN OR DOMAIN/PATH}/`
* Log Path: `/data/gitea/log`

> :warning:  
> If the base URL in web admin configuration page is not set to your domain, it
> will appear that everything is working, however intersite links will fail
> (such as issue updates). This can be changed by editing `ROOT_URL` in the
> `/data/services/gitea/conf/app.ini` file post initial configuration.

Optional Settings:
* [x] Enable Local Mode
* [x] Disable Gravatar
* [ ] Enable Federated Avatars
* [ ] Enable OpenID Sign-In
* [x] Disable Self-Registration
* [ ] Allow Registration Only Through External Services
* [ ] Enable OpenID Self-Registration
* [x] Enable CAPTCHA
* [x] Require Sign-In to View Pages
* [ ] Hide Email Addresses by Default
* [x] Allow Creation of Organizations by Default
* [x] Enable Time Tracking by Default
* Hidden Email Domain: `users.noreply.`{DOMAIN}
* Administrator Account Settings
  * Administration Username: {USER}
  * Password: {PW}
  * Confirm Password: {PW}
  * Email Address: {EMAIL}

Importing Git Repositories
--------------------------
You can import other git repositories, including local and cloned ones:
* Create an aptly named repository on gitea, intialize it empty.
* [Push a mirror][d9] to this repository. All information will be retained.
* Disable [SSL verification][ek] if using self-signed certs.

```bash
cd my-repo-to-import
git push --mirror https://<IP>:3000/<user>/<reponame>.git
```

As this is a mirror, you want to commit the git metadata and not just the files.

The git repository is stored in _/data/gitea/git_ as a standard git repository.
Importing this way sets up the gitea frontend database metadata for the project.

SSL Client Cert Authentication
------------------------------
A reverse proxy requiring SSL client certification authentication requires no
change in the gitea configuration. The git client itself will need to be updated
to handle this authentication:

/home/user/{MACHINE}.crt `user:user 0400`

/home/user/{MACHINE}.key `user:user 0400`

### [Git Cert Auth for Specific Repo][8v]
```bash
git config --local http.sslCert "/home/user/{MACHINE}.crt"
git config --local http.sslKey "/home/user/{MACHINE}.key"
```
* `--global` will force certification authentication for all repositories. This
  is probably not what you want to do.

### [Git Cert Auth for Repo Site][8s]
Applies cert authentication to all repositories matched in base URI.

~/.gitconfig `user:user 0400`
```config
[http "https://gitea.example.com"]
  sslCert = /home/user/mono.crt
  sslKey = /home/user/mono.key
```

[docker-service-template.md|c9067f2][XX]

[i2]: https://docs.gitea.io/en-us/
[3e]: https://hub.docker.com/r/gitea/gitea/
[is]: https://docs.gitea.io/en-us/config-cheat-sheet/
[fi]: https://docs.gitea.io/en-us/reverse-proxies/
[d9]: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
[ek]: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
[od]: https://docs.gitea.io/en-us/install-with-docker/
[fp]: https://discuss.gogs.io/t/reverse-proxy-unauthorized-401-windows/2057
[8v]: http://www.wakoond.hu/2013/07/using-git-with-https-client-certificate.html
[8s]: https://stackoverflow.com/questions/9008309/how-do-i-set-git-ssl-no-verify-for-specific-repos-only
[XX]: https://github.com/r-pufky/docs/blob/c9067f2bc3d0aeb0f2915e63f8cd9515c00640a2/services/docker-service-template.md

[refv3]: ../nginx/proxy-control.conf
[ref9s]: ../nginx/README.md