.. _service-gitea:

`Gitea`_
########
A community managed fork of gogs. This provides a github-like service for
private repository use. Can be exposed and used publicly as well.

See `Gitea Docker and Documentation`_ and `Gitea cheat sheet`_.

.. gport:: Ports (Gitea)
  :port:     3000
  :protocol: TCP
  :type:     Exposed
  :purpose:  http/https connections.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Gitea)
  :file:    /data/services/gitea/conf/app.ini,
            /data/services/gitea/git
  :purpose: Settings.,
            Git repo location.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can re-create with a mapped
git repository.

* ``:1`` will use the `latest stable version of Gitea`_.
* You may specify your own git repository location.

.. code-block:: yaml
  :caption: Docker Compose

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

* Proxy will forward traffic to the container, so no ports need to be exposed.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `Gitea reverse proxy reference`_.

.. note::
  Adjust ``client_max_body_size`` to expected max size of data in a git change.

Using Subdomains
================
This requires a hard IP resolution. Hairpin NAT / NAT reflection will result in
the web front working but git pull/push/clones failing. This is due to the way
Gitea `handles these requests with custom written handlers`_. Setup DNS
resolution or add to ``hosts`` file.

.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Postgres Backend
****************
.. warning::
  Though there is some documentation on moving from ``sqlite3`` to
  ``postgresql`` for gitea; all migrations seem to carry over artifacts that
  express different kinds of failures (like ``500``'s on issue updates).

  Decide on a backend before committing any amount of metadata to Gitea.

.. code-block:: ini
  :caption: **0600 gitea gitea** ``gitea/conf/app.ini``

  [database]
  DB_TYPE = postgres
  HOST = {DB IP}:{DB PORT}
  NAME = gitea
  USER = {USER}
  PASSWD = {PASS}

.. note::
  ``DB_PATH`` can be removed if not using ``sqlite3``.

  These options should be set **during** the
  :ref:`service-gitea-initial-setup`.

.. _service-gitea-initial-setup:

Initial Setup
*************
This will initially setup Gitea with restricted permissions during
configuration:

Navigate to: ``{REVERSE PROXY URI}/install``.

.. ggui:: Database Settings
  :option:  Database,
            Path
  :setting: sqlite3,
            /data/gitea/gitea.db
  :no_key_title:
  :no_caption:
  :no_launch:

.. ggui:: General Settings
  :option:  Site Title,
            Repository Root Path,
            Git LFS Root Path,
            Run As Username,
            SSH Server Domain,
            SSH Server Port,
            Gitea HTTP Listen Port,
            Gitea Base URL,
            Log Path
  :setting: {YOUR SITE NAME},
            /data/git/repositories,
            /data/git/lfs,
            git,
            localhost,
            22,
            3000,
            https://{YOUR SUBDOMMAIN OR DOMAIN/PATH}/,
            /data/gitea/log
  :no_key_title:
  :no_caption:
  :no_launch:

.. warning::
  If the base URL in web admin configuration page is not set to your domain, it
  will appear that everything is working, however intersite links will fail
  (such as issue updates). This can be changed by editing ``ROOT_URL`` in the
  ``/data/services/gitea/conf/app.ini`` file post initial configuration.

.. ggui:: Optional Settings
  :option:  ☑,
            ☑,
            ☐,
            ☐,
            ☑,
            ☐,
            ☐,
            ☑,
            ☑,
            ☐,
            ☑,
            ☑,
            Hidden Email Domain,
            Administrator Account Settings,
            › Administration Username,
            › Password,
            › Confirm Password,
            › Email Address
  :setting: Enable Local Mode,
            Disable Gravatar,
            Enable Federated Avatars,
            Enable OpenID Sign-In,
            Disable Self-Registration,
            Allow Registration Only Through External Services,
            Enable OpenID Self-Registration,
            Enable CAPTCHA,
            Require Sign-In to View Pages,
            Hide Email Addresses by Default,
            Allow Creation of Organizations by Default,
            Enable Time Tracking by Default,
            users.noreply.{DOMAIN},
            ,
            {USER},
            {PASS},
            {PASS},
            {EMAIL}
  :no_key_title:
  :no_caption:
  :no_launch:

Importing Git Repositories
**************************
You can import other git repositories, including local and cloned ones:

* Create an aptly named repository on Gitea, intialize it empty.
* `Push a mirror`_ to this repository. All information will be retained.
* Disable `SSL verification`_ if using self-signed certs.

.. code-block:: bash
  :caption: Push mirror to Gitea.

  cd my-repo-to-import
  git push --mirror https://{IP}:3000/{USER}/{REPO}.git

As this is a mirror, you want to commit the *git metadata* and not just the
files. The git repository is stored in ``/data/gitea/git`` as a standard git
repository. Importing this way sets up the Gitea frontend database metadata for
the project.

SSL Client Cert Authentication
******************************
A reverse proxy requiring SSL client certification authentication requires no
change in the Gitea configuration.

See :ref:`service-nginx-cert-auth-git` to configure your git client.

.. _Gitea: https://docs.gitea.io/en-us/
.. _Gitea Docker and Documentation: https://hub.docker.com/r/gitea/gitea/
.. _Gitea cheat sheet: https://docs.gitea.io/en-us/config-cheat-sheet/
.. _Gitea reverse proxy reference: https://docs.gitea.io/en-us/reverse-proxies/
.. _Push a mirror: https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
.. _SSL verification: https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
.. _latest stable version of Gitea: https://docs.gitea.io/en-us/install-with-docker/
.. _handles these requests with custom written handlers: https://discuss.gogs.io/t/reverse-proxy-unauthorized-401-windows/2057
