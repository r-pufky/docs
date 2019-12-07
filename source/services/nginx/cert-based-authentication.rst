.. _service-nginx-cert-based-authentication:

`Cert Based Authentication`_
############################
Configure NGINX to verify client certifcate before responding to requests. This
provides another security layer to NGINX enabling only known certificates access
to make requests for the proxy. Generally, these should be considered *machine
certificates* as they do not identify a particular user, just a machine with a
certificate.

See :ref:`service-certificate-authority` for instructions on setting up required
certificates used here. An excellent reference for `basic certificate usage`_
and should be well understood before proceeding.

`Nginx Configuration`_
**********************
If the ``default_server`` is set to not require cert-based authentication and
additional server blocks do, clients that do not support it will fall back to
the ``default_server`` and be **able** to make valid requests. Therefore the
default server should act as a **catch all** for non-cert based requests and
specifically respond to those requests. In this case we will respond immediately
with a ``403``.

.. danger::
  You are entering a dangerous space. Once a client has a valid SSL connection,
  certificate validation needs to be explicitly enforced; otherwise a client can
  access other SSL areas (due to a pre-existing valid SSL connection).

  **ALWAYS** explicitly check for valid client certificates and do penetration
  testing to verify your assumptions.

.. literalinclude:: source/server-cert-authentication.conf
  :caption: Setup NGINX SSL server with client cert authentication.

* ``If`` statements should only be used to for ``rewrite`` and ``return``
  (``proxy_pass`` is a ``rewrite`` statement). See :ref:`if-is-evil`.
* Access can be provided based on client certificate presented as well (e.g.
  specific `access for specific certificates`_).
* Disabling for a specific host may be required for backend hosts communicating
  with each other via the proxy. Most backend services do not support client
  authentication. The address here should be the proxy ``gateway`` address as
  that is where those proxied requests will be coming **from**. This will only
  allow traffic **originating** from the proxy through, not proxied requests
  from clients. Always be sure to enforce client verification and test
  assumptions.
* The Certificate Revocation List must include all CRL's up to the Root CA for
  the CRL to work, otherwise all CRL checks will be invalid and block access
  even for valid clients.

Proxy-specific Client Certificate
*********************************
For cases where a backend **requires** a certificate but the client using the
proxy does not have one. This is **dangerous** if used without layering
additional security measures. Explicitly specify a certificate that the proxy
will use to authenticate to backends for requests.

.. code-block:: nginx
  :caption: Create a client ceritifcate as normal and configure NGINX with.

  server {
    proxy_ssl_certificate         /etc/nginx/auth/nginx.crt.pem;
    proxy_ssl_certificate_key     /etc/nginx/auth/nginx.key.pem;
    proxy_ssl_trusted_certificate /etc/nginx/auth/{BACKEND}.crt.pem;
  }

.. _service-nginx-cert-auth-git:

Git Configuration
*****************
Accessing a https based git repository behind a NGINX proxy requiring client
certificate authentication is supported both locally and via URI matching.

`Git Cert Auth for Repo Site`_
==============================
.. code-block::
  :caption: **0400 user user** ``~/.gitconfig``

  [http "https://git.example.com"]
    sslCert = /home/user/{MACHINE}.crt.pem
    sslKey = /home/user/{MACHINE}.key.pem

`Git Cert Auth for Specific Repo`_
==================================
.. code-block:: bash

  git config --local http.sslCert "/home/user/{MACHINE}.crt.pem"
  git config --local http.sslKey "/home/user/{MACHINE}.key.pem"

.. note::
  ``--global`` will force certification authentication for all repositories.
  This is probably not what you want to do.

Chrome Client Certificate
*************************
`Setup chrome`_ to auto present correct certificate when challenged by proxy
server.

.. ggui:: Import Client Certificate to Chrome.
  :key_title: chrome://settings -->
              Settings -->
              Advanced -->
              Privacy and security -->
              Manage certificates -->
              Import
  :option:    ☐,
              ☐,
              ☑,
              ☑ Place all certificates in the following store
  :setting:   Enable strong private key protection.,
              Mark this key as exportable.,
              Include all extended properties.,
              Personal.
  :no_section:
  :no_launch:

.. note::
  Use export password to decrypt and import.

Restart Chrome. Nagivate to a proxied site and the certificate prompt should
appear to select which cert to authenticate with. If NGINX has been reloaded and
setup, then this should allow you to passthrough.

Auto-select Client Certificate
==============================
Auto selecting the `correct certificate`_ will enable transparent authentication
for proxied sites. Enabled via Group Policy or `Reg Edit`_.

.. wregedit:: Auto-select Client Certificate
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls
  :names:     1
  :types:     REG_SZ
  :data:      {"pattern":"https://[*.]example.com","filter":{"ISSUER":{"O":"{SERVER}"}}}
  :delim:     ;
  :admin:
  :no_caption:

    * ``1`` incremental counter for which matching patterns to apply. If using
      multiple certificates this will represent the resolution order.
    * ``O`` is used to match the **Organizational Name** of the server CA
      ``{SERVER}``. This will use this certificate for all ``{SERVER`` cert auth
      requests.
    * If using a **reg** file, ensure proper escaping:

      .. code-block::

        "1"="{\"pattern\":\"https://[*.]example.com\",\"filter\":{\"ISSUER\":{\"O\":\"{SERVER}\"}}}"

Restarting chrome will pickup the configuration changes.

.. _Cert Based Authentication: https://fardog.io/blog/2017/12/30/client-side-certificate-authentication-with-nginx/
.. _basic certificate usage: https://jamielinux.com/docs/openssl-certificate-authority/introduction.html
.. _Nginx Configuration: https://tech.mendix.com/linux/2014/10/29/nginx-certs-sni/
.. _if is evil: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
.. _access for specific certificates: https://stackoverflow.com/questions/41513400/nginx-authorization-based-on-client-certificates
.. _Git Cert Auth for Repo Site: https://stackoverflow.com/questions/9008309/how-do-i-set-git-ssl-no-verify-for-specific-repos-only
.. _Git Cert Auth for Specific Repo: http://www.wakoond.hu/2013/07/using-git-with-https-client-certificate.html
.. _Setup chrome: https://www.tbs-certificates.co.uk/FAQ/en/installer_certificat_client_google_chrome.html
.. _correct certificate: https://blogs.sap.com/2014/01/30/avoid-certification-selection-popup-in-chrome/
.. _Reg Edit: https://www.chromium.org/administrators/policy-list-3#AutoSelectCertificateForUrls