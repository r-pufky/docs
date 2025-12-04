# Forgejo
Forgejo (GIT) Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.forgejo][a].


## Repository Management

### [Importing Git Repositories][b]
You can import other git repositories including local and cloned ones:

* Create an aptly named repository and initialize it empty.
* Push a mirror to this repository. All information will be retained.
* Disable [SSL verification if using self-signed certs][c].

``` bash
# Push mirror to Forgejo.
cd my-repo-to-import
git push --mirror https://{IP}:3000/{USER}/{REPO}.git
```

As this is a mirror, you want to commit the *git metadata* and not just the
files. The Forgejo repository is stored in **forgejo_repository_root** as a
standard git repository. Importing this way sets up the Forgejo frontend
database metadata for the project.


## [Mirrors][d]
Forgejo mirrors can automatically manage upstream mirror syncs if setup to do
so. This will also allow for local forking of those mirrors for individual use.

!!! example "Create Mirror ➔ + ➔ New Migration"
    * Migrate / Clone from URL: **{REMOTE REPOSITORY URL}**
    * Owner: **{ORGANIZATION OWNER}**
    * Repository Name: **{SAME REPO NAME}**
    * Visibility: **Make Repository Private**
    * Migration Type: **This repository will be a mirror**
    * Description: **{DESCRIPTION}**


## Reverse Proxy
Forgejo should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][e] for more details.
[See Base Proxy Control][f] for basic proxy configuration.

### [Subdomains][g]
This requires a hard IP resolution. Hairpin NAT / NAT reflection will result in
the web front working but git pull/push/clones failing. This is due to the way
Forgejo handles these requests with custom written handlers. Setup DNS
resolution or add to **hosts** file.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subdomain
    server {
      listen                 443 ssl http2;
      server_name            gitea.{DOMAIN} gitea;

      location / {
        proxy_pass           http://gitea:3000;
        client_max_body_size 1024m;  # Expected max size of data in a git change.
      }
    }
    ```

### [Subpath][h]

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    # Subpath
    server {
      location /gitea/ {
        proxy_pass           http://gitea:3000/;
        client_max_body_size 1024m;  # Expected max size of data in a git change.
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
[c]: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
[d]: https://github.com/go-gitea/gitea/issues/4493
[e]: ../nginx/README.md
[f]: ../nginx/manual/setup.md#setup-base-reverse-proxy
[g]: https://discuss.gogs.io/t/reverse-proxy-unauthorized-401-windows/2057
[h]: https://forgejo.org/docs/latest/admin/setup/reverse-proxy