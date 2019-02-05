Gitea
=====
[A community managed fork of gitea.][i2] This provides a github-like service for
private repository use. Can be exposed and used publicly as well.

[Docker repository][3e]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Reverse Proxy Setup](#reverse-proxy-setup)
1. [Importing Git Repositories](#importing-git-epositories)
1. [Other Options](#other-options)

Docker Ports Exposed
--------------------

| Docker Port | Protocol |Purpose                     |
|-------------|----------|----------------------------|
| 3000        | TCP      | http/https connections.    |

Important File Locations
------------------------
Relative to docker container

| File                              | Purpose           |
|-----------------------------------|-------------------|
| /data/services/gitea/conf/app.ini | Settings          |
| /data/services/gitea/git          | Git repo location |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
git repository.

* `:1` will use the [latest stable version of gitea][OD].

You may specify your own git repository location

### Docker Compose
```yaml
gitea:
  image: gitea/gitea:1
  restart: unless-stopped
  ports:
    - "3000:3000"
  environment:
    - USER_UID=1001
    - USER_GID=1001
    - RUN_MODE=prod
    - DISABLE_SSH=true
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/gitea:/data
    - /data/git/gitea:/data/git/repositories
    - /etc/localtime:/etc/localtime:ro
```

Initial Setup
-------------
This will initially setup gitea with restricted permissions during
configuration.

```
<IP>:3000/install
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
* Gitea Base URL: `http://localhost:3000/`
* Log Path: `/data/gitea/log`

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

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref9s] for more details. Recommended.

If using heimdall, setup gitea using the `gitea` template.

docker-compose.yml
```yaml
gitea:
  image: gitea/gitea:1
  restart: unless-stopped
  environment:
    - USER_UID=1001
    - USER_GID=1001
    - RUN_MODE=prod
    - DISABLE_SSH=true
    - ROOT_URL='{YOUR SUBDOMMAIN OR DOMAIN/PATH}'
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/gitea:/data
    - /data/git/gitea:/data/git/repositories
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
This requires a hard IP resolution. Hairpin NAT / NAT reflection will result in
the web front working but git pull/push/clones failing. This is due to the way
gitea [handles these requests with custom written handlers][7]. Setup DNS
resolution or add to `hosts` file.

[nginx/conf.d/reverse-proxy.conf][fi]
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
[nginx/conf.d/reverse-proxy.conf][fi]
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

Importing Git Repositories
--------------------------
You can import other git repositories, including local and cloned ones:

* Create an aptly named repository on gitea, intialize it empty.
* [Push a mirror][d9] to this repository. All information will be retained.
* Disable [SSL verification][Ek] if using self-signed certs.

 ```bash
cd my-repo-to-import
git push --mirror https://<IP>:3000/<user>/<reponame>.git
```
As this is a mirror, you want to commit the git metadata and not just the files.

The git repository is stored in /data/gitea/git as a standard git repository.
Importing this way sets up the gitea frontend database metadata for the project.

[i2]: https://docs.gitea.io/en-us/
[3e]: https://hub.docker.com/r/gitea/gitea/
[is]: https://docs.gitea.io/en-us/config-cheat-sheet/
[fi]: https://docs.gitea.io/en-us/reverse-proxies/
[d9]: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
[Ek]: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
[OD]: https://docs.gitea.io/en-us/install-with-docker/

[refv3]: ../nginx/proxy-control.conf
[ref9s]: ../nginx/README.md