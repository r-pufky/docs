.. _service-nginx-setup:

NGINX Setup
###########
.. gport:: Ports (NGINX)
  :port:     80,
             443
  :protocol: TCP,
             TCP
  :type:     Public,
             Public
  :purpose:  http connection -- redirected to https.,
             https connections.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (NGINX)
  :file:    /etc/nginx/conf.d,
            /etc/nginx/ssl
  :purpose: Proxy configuration settings.,
            SSL certificate location.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
.. code-block:: yaml
  :caption: Docker Compose

  nginx-proxy:
    image: nginx
    restart: unless-stopped
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - /data/services/nginx/conf.d:/etc/nginx/conf.d:ro
      - /data/services/letsencrypt:/etc/nginx/ssl:ro
      - /etc/localtime:/etc/localtime:ro

.. note::
  Let's Encrypt local mount should just point to the install location of let's
  encrypt, typically ``/etc/letsencrypt``. See :ref:`service-letsencrypt`.

.. _service-nginx-logs-to-system:

Send NGINX Logs to System
=========================
If using NGINX as a proxy for dockers, setup to log to system.

.. code-block:: yaml
  :caption: Docker Compose

  nginx-proxy:
    volumes:
      - /var/log/nginx:/var/log/nginx

.. note::
  Restart NGINX container. Logs should appear in ``/var/log/nginx/*.log`` on
  host. Logs will no longer be accessible via ``docker logs``.

Setup Base Reverse Proxy
************************
This will setup a basic reverse-proxy that:

* Forces HTTP to HTTPS connections for IPv4/6 with a permenant redirect.
* Serves traffic only over SSL (443).
* Enables HTTP2 if the service behind the proxy supports it.
* Ability to upgrade a connection to a websocket if a service requires it.
* Direct requests to the proxy cannot contain data.
* Import SSL certificate settings used in Let's Encrypt for strong validation of
  certifcate usage.

`Automatic generator`_ to generate base configuration templates.

.. literalinclude:: source/base-reverse-proxy.conf
  :caption: **0644 root root** ``/etc/nginx/conf.d/reverse-proxy.conf``
  :language: nginx

* The ``SERVER DNS NAME`` should be in the SSL certificate; a `wildcard
  certificate`_ will work.
* ``ssl-dhparams.pem`` may be generated with ``openssl dhparam -out
  ssl-dhparams.pem 4096``.
* **resolver** should be set to a `DNS resolver`_. localhost, gateway or pihole
  are all viable options. Check logs to ensure resolution works.

.. _service-nginx-base-proxy-control:

Setup Base Proxy Control
************************
A proxy control template will enable complex proxy configurations to be
consistenly applied to multiple proxy sites.

.. literalinclude:: source/base-proxy-control.conf
  :caption: **0644 root root** ``/etc/nginx/conf.d/proxy-control.conf``
  :language: nginx

Reload Configuration
********************
.. code-block:: bash
  :caption: Reload nginx configuration while running.

  docker exec -it nginx-proxy nginx -s reload

.. note::
  If underlying services have changed **expose** or **ports**, those containers
  will need to be restarted.

.. _Automatic generator: https://www.digitalocean.com/community/tools/nginx
.. _wildcard certificate: https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f
.. _DNS resolver: https://community.letsencrypt.org/t/no-resolver-defined-to-resolve-ocsp-int-x3-letsencrypt-org-while-requesting-certificate-status-responder-ocsp-int-x3-letsencrypt-org/21427