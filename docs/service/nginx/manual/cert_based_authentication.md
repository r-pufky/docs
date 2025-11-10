# [Cert Based Authentication](https://fardog.io/blog/2017/12/30/client-side-certificate-authentication-with-nginx/)
Configure NGINX to verify client certificate before responding to requests.
This provides another security layer to NGINX enabling only known certificates
access to make requests for the proxy. Generally, these should be considered
*machine certificates* as they do not identify a particular user, just a
machine with a certificate.

See [Certificate Authority](../../ca/setup.md) for instructions on setting up
required certificates used here. An excellent reference for [basic certificate
usage](https://jamielinux.com/docs/openssl-certificate-authority/introduction.html)
and should be well understood before proceeding.

Nginx Configuration
*******************
If the **default_server** is set to not require cert-based authentication and
additional server blocks do, clients that do not support it will fall back to
the **default_server** and be **able** to make valid requests. Therefore the
default server should act as a **catch all** for non-cert based requests and
specifically respond to those requests. In this case we will respond
immediately with a **403**.

!!! danger
    You are entering a dangerous space. Once a client has a valid SSL
    connection, certificate validation needs to be explicitly enforced;
    otherwise a client can access other SSL areas (due to a pre-existing valid
    SSL connection).

    **ALWAYS** explicitly check for valid client certificates and do
    penetration testing to verify your assumptions.

/etc/nginx/conf.d/server_cert_authentication.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Setup NGINX SSL server with client cert authentication.
server {
  # Security-related headers (cross-site/domain, referrer)
  # https://geekflare.com/http-header-implementation/
  # https://geekflare.com/nginx-webserver-security-hardening-guide/
  # https://www.cyberciti.biz/tips/linux-unix-bsd-nginx-webserver-security.html
  add_header X-Content-Type-Options            nosniff;
  add_header X-XSS-Protection                  "1; mode=block";
  add_header X-Robots-Tag                      none;
  add_header X-Download-Options                noopen;
  add_header X-Permitted-Cross-Domain-Policies none;
  add_header Referrer-Policy                   no-referrer;
  add_header Strict-Transport-Security         "max-age=15768000; includeSubDomains; preload;";

  # Enable basic SSL security settings.
  ssl_certificate                              /etc/nginx/ssl/letsencrypt-fullchain.pem;
  ssl_certificate_key                          /etc/nginx/ssl/letsencrypt-privkey.pem;
  ssl_trusted_certificate                      /etc/nginx/ssl/letsencrypt-chain.pem;
  ssl_dhparam                                  /etc/nginx/ssl/letsencrypt-ssl-dhparams.pem;

  # Enable OCSP stapling https://en.wikipedia.org/wiki/OCSP_stapling.
  ssl_stapling                                 on;
  ssl_stapling_verify                          on;

  # make client certificate verification optional, so we can display a 403
  # message to those who fail authentication. All loctions **must** explicitly
  # validate ssl_client_verify for restricted access to work. Alternatively the
  # ``on`` option will force client auth for all connections, including error
  # pages.
  ssl_client_certificate                       /etc/nginx/auth/ca-chain.cert.pem;
  ssl_crl                                      /etc/nginx/auth/ca-chain.crl.pem;
  ssl_verify_client                            optional;

  # One error page for everything. Does not require client cert.
  root       /www;
  error_page 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 421 422 423 424 426 428 429 431 451 500 501 502 503 504 505 506 507 508 510 511 /error.html;
  location = /error.html {
    allow    all;
    internal;
    root     /www;
  }

  # If no cert auth is used, 403.
  location /secured_site {
    # Disable client certificate authentication for a specific host. See geo
    # module for catching subnets.
    if ($remote_addr = 10.10.10.10) {
      proxy_pass http://some-backend;
      break;
    }

    if ($ssl_client_verify != SUCCESS) {
      return     403;
      break;
    }
    proxy_pass   http://some-backend;
  }
}
```

* This provices **Authentication (authn)** [See Certificate
  Authorization](#certificate-authorization-authz) for **authorization** setup.
* **If** statements should only be used to for **rewrite** and **return**
  (**proxy_pass** is a **rewrite** statement). See
  [if-is-evil](https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/).
* Access can be provided based on client certificate presented as well (e.g.
  specific [access for specific certificates](https://stackoverflow.com/questions/41513400/nginx-authorization-based-on-client-certificates).
* Disabling for a specific host may be required for backend hosts communicating
  with each other via the proxy. Most backend services do not support client
  authentication. The address here should be the proxy **gateway** address as
  that is where those proxied requests will be coming **from**. This will only
  allow traffic **originating** from the proxy through, not proxied requests
  from clients. Always be sure to enforce client verification and test
  assumptions.
* The Certificate Revocation List must include all CRL's up to the Root CA for
  the CRL to work, otherwise all CRL checks will be invalid and block access
  even for valid clients.

## Proxy-specific Client Certificate
For cases where a backend **requires** a certificate but the client using the
proxy does not have one. This is **dangerous** if used without layering
additional security measures. Explicitly specify a certificate that the proxy
will use to authenticate to backends for requests.

Create a client certificate as normal and configure NGINX with.
``` nginx
server {
  proxy_ssl_certificate         /etc/nginx/auth/nginx.crt.pem;
  proxy_ssl_certificate_key     /etc/nginx/auth/nginx.key.pem;
  proxy_ssl_trusted_certificate /etc/nginx/auth/{BACKEND}.crt.pem;
}
```

## Certificate Authorization (authz)
Enable [specific site access to client certificates](https://stackoverflow.com/questions/41513400/nginx-authorization-based-on-client-certificates).

/etc/nginx/conf.d/default.conf (1)
{ .annotate }

1. 0644 root:root

``` nginx
include /etc/nginx/conf.d/include/context/map-hash-size-optimal;
include /etc/nginx/conf.d/include/context/map-client-blacklist;
```

/etc/nginx/conf.d/include/context/map-hash-size-optimal (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Increase hash table size for optimal map lookups.
map_hash_max_size 1024;
map_hash_bucket_size 128;
```

/etc/nginx/conf.d/include/context/map-client-blacklist (1)
{ .annotate }

1. 0644 root:root

``` nginx
map $ssl_client_s_dn $cert_authz {
  default SUCCESS;
  "emailAddress=XX,CN=XX,OU=XX,O=XX,L=XX,ST=XX,C=XX" FAILURE;
}
```

!!! note
    **Subject DN** can be found by inspecting the certificate:

    ``` bash
    openssl x509 -text -noout -in {CERT}
    ```

    Order of **Subject DN** can be found by inspecting the response headers.
    See [Debug Headers](../troubleshooting.md#debug-nginx-configs).

/etc/nginx/conf.d/include/authz/enforce-blacklist  (1)
{ .annotate }

1. 0644 root:root

``` nginx
# Blacklisted authz certs should 403.
if ($cert_authz != SUCCESS) {
  return 403;
  break;
}
```

/etc/nginx/conf.d/include/proxy/site (1)
{ .annotate }

1. 0644 root:root

``` nginx
include /etc/nginx/conf.d/include/authn/cert/force-all-connections;
include /etc/nginx/conf.d/include/authz/enforce-blacklist;
```

!!! note
    **force-all-connections** provides the **authentication** step.
    **enforce-blacklist** provides the **authorization** step.

## Git Configuration
Accessing a https based git repository behind a NGINX proxy requiring client
certificate authentication is supported both locally and via URI matching.

### [Git Cert Auth for Repo Site](https://stackoverflow.com/questions/9008309/how-do-i-set-git-ssl-no-verify-for-specific-repos-only)

~/.gitconfig (1)
{ .annotate }

1. 0400 {USER}:{USER}

``` ini
[http "https://git.example.com"]
sslCert = /home/user/{MACHINE}.crt.pem
sslKey = /home/user/{MACHINE}.key.pem
```

### [Git Cert Auth for Specific Repo](http://www.wakoond.hu/2013/07/using-git-with-https-client-certificate.html)
``` bash
git config --local http.sslCert "/home/user/{MACHINE}.crt.pem"
git config --local http.sslKey "/home/user/{MACHINE}.key.pem"
```

!!! note
    **--global** will force certification authentication for all repositories.
    This is probably not what you want to do.

.. _service-nginx-chrome-client-certificate:

## Chrome Client Certificate
[Setup chrome](https://www.tbs-certificates.co.uk/FAQ/en/installer_certificat_client_google_chrome.html)
to auto present correct certificate when challenged by proxy server.


!!! example "Import Client Certificate to Chrome"
    chrome://settings ➔ Settings ➔ Advanced ➔ Privacy and security ➔ Manage certificates ➔ Import

    * Enable strong private key protection: ✘
    * Mark this key as exportable: ✘
    * Include all extended properties: ✔
    * Place all certificates in the following store: Personal ✔

!!! note
    Use export password to decrypt and import.

Restart Chrome. Navigate to a proxied site and the certificate prompt should
appear to select which cert to authenticate with. If NGINX has been reloaded
and setup, then this should allow you to passthrough.

## Auto-select Client Certificate
Auto selecting the [correct certificate](https://blogs.sap.com/2014/01/30/avoid-certification-selection-popup-in-chrome/)
will enable transparent authentication for proxied sites. Enabled via Group
Policy or Registry.

!!! example "Auto-select Client Certificate (Windows)"
    `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls`

    Key: **1**  # Resolution order for multiple certificates.

    Type: **SZ**

    Value: **{"pattern":"https://[\*.]example.com","filter":{"ISSUER":{"O":"{SERVER}"}}}**

* **O** is used to match the **Organizational Name** of the server CA
  **{SERVER}**. This will use this certificate for all **{SERVER}** cert auth
  requests.

!!! info "Regedit files require proper escaping"
    ``` regedit
    "1"="{\"pattern\":\"https://[*.]example.com\",\"filter\":{\"ISSUER\":{\"O\":\"{SERVER}\"}}}"
    ```

Reference:

* https://chromeenterprise.google/policies/#AutoSelectCertificateForUrls

Auto-select Client Certificate (Linux)

/etc/opt/chrome/policies/managed/auto_select_certificate.json (1)
{ .annotate }

1. 0644 root:root (all directories on path **must** be readable by others).

``` json
{
  "AutoSelectCertificateForUrls": [
    "{\"pattern\":\"https://[*.]example.com\",\"filter\":{\"ISSUER\":{\"O\":\"{SERVER}\"}}}"
  ]
}
```

Restarting chrome will pickup the configuration changes.

## Firefox Client Certificate
Setup Firefox to auto present correct certificate when challenged by proxy
server.

!!! example "Import Client Certificate to Firefox"
    about:preferences#privacy ➔ Certificates ➔ OSCP ➔ View Certificates ➔ Your Certificates ➔ Import

    Use export password to decrypt and import.


!!! example "Disable client certificate syncing"
    about:config ➔ Accept the Risk and Continue ➔
    services.sync.prefs.sync.security.default_personal_cert

    Value: **False**.

Restart Firefox. Navigate to a proxied site and the certificate prompt should
appear to select which cert to authenticate with. If NGINX has been reloaded
and setup, then this should allow you to passthrough. Remember decision to
prevent additional certificate prompts on revisit.

Reference:

* https://stackoverflow.com/questions/27864553/how-can-i-choose-a-different-client-certificate-in-firefox
