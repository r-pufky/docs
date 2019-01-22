gogs
----
[A painless self-hosted Git service.][1] This provides a github-like service for
private repository use. Can be exposed and use publicly as well.

[Docker repository][5]

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
| 22          | TCP      | ssh connections.           |
 * You can disable both http and ssh connections depending on your setup.

Important File Locations
------------------------
Relative to docker container

| File                    | Purpose           |
|-------------------------|-------------------|
| /data/gogs/conf/app.ini | Settings          |
| /data/gogs/git          | Git repo location |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
git repository.

* Cannot specify a UID/GID to run under - git files must be accessible to
  docker.

### Independant Container
```bash
docker run -t -d \
  --name=gogs \
  --net=host \
  --restart=unless-stopped \
  -p 10080:3000 \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/gogs:/data \
  gogs/gogs:latest
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

You may specify your own git repository location
```bash
docker run -t -d \
  --name=gogs \
  --net=host \
  --restart=unless-stopped \
  -p 10080:3000 \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/gogs:/data \
  -v /data/backup/git:/data/git \
  gogs/gogs:latest
```

### Docker Compose
```yaml
gogs:
  image: gogs/gogs:latest
  restart: unless-stopped
  ports:
    - "10080:3000"
  environment:
    - TZ=America/Los_Angeles
  volumes:
    - /data/git/gogs:/data/git
    - /data/services/gogs:/data
    - /etc/localtime:/etc/localtime:ro
```

Initial Setup
-------------
This will initially setup gogs with restricted permissions during configuration.

```
<IP>:10080/install
```

database:
 * database: sqlite3 (only used for web frontend, tracking is done in git)

Application general settings:
 * site title: your-site-name
 * git repository: /data/git

Optional settings:
 * server and other services settings:
   * enable federated avatars lookup (e.g. allows github avatar icons on this)
   * disable self-registration (prevents public usage)
   * enable require sign in to view pages
 * admin account settings:
   * enter user/pass/email (email can be a fake).

## Generate self-signed certificate (if needed)
This will generate self-signed certificates, skip if you have these.

```bash
docker exec -it gogs /bin/bash
cd /app/gogs
./gogs cert --ca --host <hostname>,<IP>
mv *.pem /data/gogs/conf/
exit
```
The host paramater is a comma separated list of IP's and host/dns names for the
cert.

## Enable HTTPS
Stop the docker container and enable HTTPS.

```bash
docker stop gogs
```

/data/services/gogs/gogs/conf/app.ini
```ini
[server]
PROTOCOL = https
DOMAIN = <IP>
ROOT_URL = https://<IP>:10080/
DISABLE_SSH = true
CERT_FILE = /data/gogs/conf/cert.pem
CERT_KEY = /data/gogs/conf/key.pem

[session]
COOKIE_SECURE = true
```
 * Captilization matters for config. Using `protocol` will not enable https.
   `PROTOCOL` will.
 * DOMAIN: refers the the SSH domain when being used.
 * ROOT_URL: is the redirect URL used when reloading pages. This should be your
   Docker's host IP and accessible port.
 * ROOT_URL: note httpS. This is required.

## Alternative git repo location
Map the git repository backing to data store not in docker config.

```bash
mv /data/services/gogs/git/* <git date store>
rm /data/services/gogs/git
```
 * Only need to do this if initially creating gogs git repository.
 * Recreate the docker container, mapping `/data/git` to your data store.

Then restart gogs
```bash
docker start gogs
```

Reverse Proxy Setup
-------------------
Allows you to isolate your containers as well as wrap connections in SSL. See
[nginx][ref2] for more details. Recommended.

If using heimdall, setup gogs using the `gitea` template.

docker-compose.yml
```yaml
gogs:
  image: gogs/gogs:latest
  restart: unless-stopped
  environment:
    - TZ=America/Los_Angeles
  volumes:
    - /data/git/gogs:/data/git
    - /data/services/gogs:/data
    - /etc/localtime:/etc/localtime:ro
```
* Proxy will forward traffic to the container, so no ports need to be exposed.

### Using Subdomains
[nginx/conf.d/reverse-proxy.conf][2]
```nginx
server {
  listen 443 ssl http2;
  server_name gogs.<DOMAIN> gogs;

  location / {
    proxy_pass https://gogs:3000/;
    proxy_set_header X-Real-IP $remote_addr;
    client_max_body_size 1024m;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.

gogs/gogs/conf/app.ini
```yaml
[server]
DOMAIN   = your.ssl.proxy.fqdn
ROOT_URL = https://your.ssl.proxy.fqdn/gogs/
```
* `your.ssl.proxy.fqdn` is what an external user will see your reverse-proxy DNS
  name.

### Using Subpaths
[nginx/conf.d/reverse-proxy.conf][6]
```nginx
server {
  location /gogs/ {
    proxy_pass https://gogs:3000/;
    proxy_set_header X-Real-IP $remote_addr;
    client_max_body_size 1024m;
  }
}
```
* [proxy-control.conf][ref1] contains default proxy settings. Reload nginx.
* Adjust `client_max_body_size` to expected max size of data in a git change.

gogs/gogs/conf/app.ini
```yaml
[server]
ROOT_URL = https://your.ssl.proxy.fqdn/gogs/
```
* `your.ssl.proxy.fqdn` is what an external user will see your reverse-proxy DNS
  name.

Importing Git Repositories
--------------------------
You can import other git repositories, including local and cloned ones:

 * Create an aptly named repository on gogs, intialize it empty.
 * [Push a mirror][2] to this repository. All information will be retained.
 * Disable [SSL verification][3] if using self-signed certs.

 ```bash
cd my-repo-to-import
git -c http.sslVerify=false push --mirror https://<IP>:10080/<user>/<reponame>.git
```
As this is a mirror, you want to commit the git metadata and not just the files.

The git repository is stored in /data/gogs/git as a stand git repository.
Importing this way sets up the gogs fronend database metadata for the project.

Dashboard not updating on commits
---------------------------------
If the dashboard stop updating when commits are made, it generally means the
(sole) developer missed a database conversion with a version upgrade. The
solution to this is to re-create the repository on gogs. This is non-destructive
to the git data, however, GOGS specific data (e.g. issues, wiki) may be
destroyed.

1. Create bare repo clone `git clone --bare https://gogs:10080/user/repo.git`
1. Copy any metadata from repo
1. Delete GOGS repo `repo > settings > Delete this Repository`
1. Create GOGS repo, same name. Init **bare** (do not init with selected files)
1. Push mirror to GOGS

```bash
cd repo.git
git -c http.SslVerify=false push --mirror https://gogs:10080/user/repo.git
```

Other Options
-------------
[gitea][4] is a better option (gogs community managed forked), but is currently
broken with HTTPS certs. Gitea is supported by a community of developers and has
a lot more features then gogs. Gogs is maintained by a single developer.

[1]: https://gogs.io/
[2]: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
[3]: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
[4]: https://gitea.io/en-US/
[5]: https://hub.docker.com/r/gogs/gogs/
[6]: https://gogs.io/docs/intro/faqs

[ref1]: ../nginx/proxy-control.conf
[ref2]: ../nginx/README.md