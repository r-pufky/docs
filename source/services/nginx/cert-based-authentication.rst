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

Nginx Configuration
*******************
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

* This provices **Authentication (authn)** See :ref:`service-nginx-cert-authz`
  for **authorization** setup.
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

.. _service-nginx-cert-authz:

Certificate Authorization (authz)
*********************************
Enable `specific site access to client certificates`_.

.. code-block:: nginx
  :caption: **0644 root root** ``/etc/nginx/conf.d/default.conf``

  include /etc/nginx/conf.d/include/context/map-hash-size-optimal;
  include /etc/nginx/conf.d/include/context/map-client-blacklist;

.. code-block:: nginx
  :caption: **0644 root root** ``/etc/nginx/conf.d/include/context/map-hash-size-optimal``

  # Increase hashtable size for optimal map lookups.
  map_hash_max_size 1024;
  map_hash_bucket_size 128;

.. code-block:: nginx
  :caption: **0644 root root** ``/etc/nginx/conf.d/include/context/map-client-blacklist``

  map $ssl_client_s_dn $cert_authz {
    default SUCCESS;
    "emailAddress=XX,CN=XX,OU=XX,O=XX,L=XX,ST=XX,C=XX" FAILURE;
  }

.. note::
  ``Subject DN`` can be found by inspecting the certificate:

  .. code-block:: bash

    openssl x509 -text -noout -in {CERT}

  Order of the ``Subject DN`` can be found by inspecting the response headers.
  See :ref:`service-nginx-debug-nginx-configs`.

.. code-block:: nginx
  :caption: **0644 root root** ``/etc/nginx/conf.d/include/authz/enforce-blacklist``

  # Blacklisted authz certs should 403.
  if ($cert_authz != SUCCESS) {
    return 403;
    break;
  }

.. code-block:: nginx
  :caption: **0644 root root** ``/etc/nginx/conf.d/include/proxy/site``

  include /etc/nginx/conf.d/include/authn/cert/force-all-connections;
  include /etc/nginx/conf.d/include/authz/enforce-blacklist;

.. note::
  ``force-all-connections`` provides the **authentication** step.
  ``enforce-blacklist`` provides the **authorization** step.

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

.. _service-nginx-chrome-client-certificate:

Chrome Client Certificate
*************************
`Setup chrome`_ to auto present correct certificate when challenged by proxy
server.

.. gui::   Import Client Certificate to Chrome
  :path:   chrome://settings -->
           Settings -->
           Advanced -->
           Privacy and security -->
           Manage certificates -->
           Import
  :value0: ☐, Enable strong private key protection
  :value1: ☐, Mark this key as exportable
  :value2: ☑, Include all extended properties
  :value3: ☑ Place all certificates in the following store, Personal

.. note::
  Use export password to decrypt and import.

Restart Chrome. Nagivate to a proxied site and the certificate prompt should
appear to select which cert to authenticate with. If NGINX has been reloaded and
setup, then this should allow you to passthrough.

Auto-select Client Certificate
==============================
Auto selecting the `correct certificate`_ will enable transparent authentication
for proxied sites. Enabled via Group Policy or Registry.

.. regedit:: Auto-select Client Certificate (Windows)
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls
  :value0:   1; {SZ}; {"pattern":"https://[\*.]example.com","filter":{"ISSUER":{"O":"{SERVER}"}}}
  :delim:    ;
  :ref:      https://chromeenterprise.google/policies/#AutoSelectCertificateForUrls
  :update:   2021-12-29

  * ``1`` incremental counter for which matching patterns to apply. If using
    multiple certificates this will represent the resolution order.
  * ``O`` is used to match the **Organizational Name** of the server CA
    ``{SERVER}``. This will use this certificate for all ``{SERVER}`` cert auth
    requests.
  * If using a **reg** file, ensure proper escaping:

    .. code-block::

      "1"="{\"pattern\":\"https://[*.]example.com\",\"filter\":{\"ISSUER\":{\"O\":\"{SERVER}\"}}}"

.. dropdown:: Auto-select Client Certificate (Linux)
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  All directories should be readable by ``other``.

  .. code-block::
    :caption: **0644 root root** ``/etc/opt/chrome/policies/managed/auto_select_certificate.json``

    {
      "AutoSelectCertificateForUrls": [
        "{\"pattern\":\"https://[*.]example.com\",\"filter\":{\"ISSUER\":{\"O\":\"{SERVER}\"}}}"
      ]
    }

Restarting chrome will pickup the configuration changes.


.. _service-nginx-firfox-client-certificate:

Firefox Client Certificate
*************************
Setup Firefox to auto present correct certificate when challenged by proxy
server.

.. gui::   Import Client Certificate to Firefox
  :path:   about:preferences#privacy -->
           Certificates -->
           OSCP -->
           View Certificates -->
           Your Certificates -->
           Import

.. note::
  Use export password to decrypt and import.

.. gui::   Disable client certificate sync'ing.
  :path:   about:config -->
           Accept the Risk and Continue -->
           services.sync.prefs.sync.security.default_personal_cert
  :value0: {false}
  :ref:    https://stackoverflow.com/questions/27864553/how-can-i-choose-a-different-client-certificate-in-firefox

Restart Firefox. Nagivate to a proxied site and the certificate prompt should
appear to select which cert to authenticate with. If NGINX has been reloaded and
setup, then this should allow you to passthrough. Remember decision to prevent
additional certificate prompts on revisit.

.. _Cert Based Authentication: https://fardog.io/blog/2017/12/30/client-side-certificate-authentication-with-nginx/
.. _basic certificate usage: https://jamielinux.com/docs/openssl-certificate-authority/introduction.html
.. _if is evil: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
.. _access for specific certificates: https://stackoverflow.com/questions/41513400/nginx-authorization-based-on-client-certificates
.. _Git Cert Auth for Repo Site: https://stackoverflow.com/questions/9008309/how-do-i-set-git-ssl-no-verify-for-specific-repos-only
.. _Git Cert Auth for Specific Repo: http://www.wakoond.hu/2013/07/using-git-with-https-client-certificate.html
.. _Setup chrome: https://www.tbs-certificates.co.uk/FAQ/en/installer_certificat_client_google_chrome.html
.. _correct certificate: https://blogs.sap.com/2014/01/30/avoid-certification-selection-popup-in-chrome/
.. _specific site access to client certificates: https://stackoverflow.com/questions/41513400/nginx-authorization-based-on-client-certificates
