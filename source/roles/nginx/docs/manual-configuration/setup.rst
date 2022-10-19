.. _service-nginx-setup:

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

`Automatic generator <https://www.digitalocean.com/community/tools/nginx>`_ to
generate base configuration templates.

.. literalinclude:: source/base-reverse-proxy.conf
  :caption: **0644 root root** ``/etc/nginx/conf.d/reverse-proxy.conf``
  :language: nginx

* The ``SERVER DNS NAME`` should be in the SSL certificate; a wildcard
  certificate will work.
* ``ssl-dhparams.pem`` may be generated with ``openssl dhparam -out
  ssl-dhparams.pem 4096``.
* **resolver** should be set to a DNS resolver. localhost, gateway or pihole
  are all viable options. Check logs to ensure resolution works.

`Reference <https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f>`__

`Reference <https://community.letsencrypt.org/t/no-resolver-defined-to-resolve-ocsp-int-x3-letsencrypt-org-while-requesting-certificate-status-responder-ocsp-int-x3-letsencrypt-org/21427>`__

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

  nginx -s reload

.. note::
  If underlying services have changed **expose** or **ports**, those containers
  will need to be restarted.
