gogs
----
[A painless self-hosted Git service.][1] This provides a github-like service for
private repository use. Can be exposed and use publicly as well.

Docker Ports Exposed
--------------------

| Docker Port | Protocol |Purpose                     |
|-------------|----------|----------------------------|
| 3000        | TCP      | http/https connections.    |
| 22          | TCP      | ssh connections.           |
 * You can disable both http and ssh connections depending on your setup.

Docker Creation
---------------

If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
git repository.
```bash
docker run --name=gogs -p 10080:3000 -e /etc/localtime:/etc/localtime:ro -v /data/services/gogs:/data gogs/gogs:latest
```

Specify your own git repository location
```bash
docker run --name=gogs -p 10080:3000 -e /etc/localtime:/etc/localtime:ro -v /data/services/gogs:/data -v /data/backup/git:/data/git gogs/gogs:latest
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

Importing git repositories
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

Other Options
-------------
[gitea][4] is a better option (gogs community managed forked), but is currently
broken with HTTPS certs. Gitea is supported by a community of developers and has
a lot more features then gogs. Gogs is maintained by a single developer.

[1]: https://gogs.io/
[2]: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
[3]: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
[4]: https://gitea.io/en-US/
