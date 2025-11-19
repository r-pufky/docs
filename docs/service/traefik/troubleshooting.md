# Troubleshooting

## OIDC device_id and device_name are required for private IP
OIDC requires HTTPS with validate certificates. Internal IP's do not have
these.

!!! danger ""
    ``` bash

    device_id and device_name are required for private IP: https://{IP}/oauth2/callback Learn more about this error
    If you are a developer of Traefik Auth ...
    Error 400: invalid_request
    ```

Disable OIDC middleware if not using DNS names and certificates.

Or create separate routers specifically handling Internal IP's - however these
must be able to provide user identity to those backends.


## [Invalid state parameter (CSRF mismatch)][a]
Authentication cookies cannot be shared between subdomains by default.

!!! danger ""
    ``` bash
    Authentication Error

    Invalid state parameter (CSRF mismatch)
    ```

Explicitly enable a **common** cookie domain for sharing logins between
subdomains and services. Increase exposure as now any login on a subdomain will
not re-authenticate user when changing subdomains.

!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      middlewares:
        {NAME}:
          plugin:
            traefikoidc:
              cookieDomain: '.example.com'
    ```

[a]: https://github.com/lukaszraczylo/traefikoidc/tree/main?tab=readme-ov-file#with-cookie-domain-configuration-multi-subdomain-setup