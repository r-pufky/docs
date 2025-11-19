# OIDC
Open Identity Connect provides open authentication for users in the form of JWT
claims without needing to handle passwords directly.

!!! danger "Authentication (authn) is **not** Authorization (authz)"
    This proves who the user is but not what they should have access to.
    Any valid user will successfully login to any proxied site.

    Additional middleware or per backend configuration needs to **authorize**
    those **authenticated** users to access that data.

!!! danger "OIDC does not require 2FA authentication"
    Users who do not have security keys / passkeys / SMS enabled on their OIDC
    account will still be able to provide valid authentication with only a
    **password** that meets the **minimum** provider OIDC requirements.

    Using [Google Identity Platform][b] can force 2FA but requires paying for
    the service on each domain.

    This provides the **identity** of entity making the client request but it
    does not **prove** who they **are** - 2FA should be used for that.

!!! warning "mTLS Highly Recommended"
    Consider using Mutual TLS (mTLS) as an additional layer of security in
    which both client and server validate each other.

## Traefik Oauth
Google Oauth is free.

### Create Google Cloud Project
!!! example "console.cloud.google.com ➔ ctrl + o ➔ New project"
    * Project name: **Traefik Forward Auth**
    * Location: **No organization**

### Configure Oauth Consent Screen
!!! example "console.cloud.google.com ➔ ctrl + o ➔ Traefik Forward Auth ➔ APIs & Services ➔ Oauth consent screen ➔ Get started"
    * App Information:
        * App name: **Traefik Auth**
        * User support email: **{GMAIL}**
    * Audience:
        * External: ✔
    * Contact Information: **{GMAIL}**  # Notifications about project changes.
    * Finish:
        * I agree to the Google API Services User Data Policy: ✔

### Add Authorized Domains and Publish Oauth
No restricted scopes or test users are required to be defined. User will be
filtered with Traefik plugins.

!!! example "console.cloud.google.com ➔ ctrl + o ➔ Traefik Forward Auth ➔ APIs & Services ➔ Oauth consent screen ➔ Branding"
    * Authorized domains: {DOMAIN}

    Be sure to **save** changes.

!!! example "console.cloud.google.com ➔ ctrl + o ➔ Traefik Forward Auth ➔ APIs & Services ➔ Oauth consent screen ➔ Audience"
    * Testing: **Publish App**

## Create Oauth credentials for Traefik Service
Creates a Traefik web application client ID used for requesting OIDC
authentication of a user.

!!! example "console.cloud.google.com ➔ ctrl + o ➔ Traefik Forward Auth ➔ APIs & Services ➔ Credentials ➔ Create credentials ➔ OAuth client ID"
    * Application type: **Web application**
    * Name: **Traefik Oauth**
    * authorized redirect URIs:
        * **https://example.com/oauth2/callback**
        * **https://{SUBDOMAIN}.example.com/oauth2/callback**

    Create a redirect URI for **all** domains and subdomains - Google Oauth2.0
    does not support wildcards.

    **Download** corresponding JSON file.

    Note Client ID and Client secret for next step.


## Whitelist Authenticated gmail users

!!! abstract "/etc/traefik/traefik.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    log:
      level: 'DEBUG'
      format: 'json'
    accessLog:
      format: 'json'
    api:
      dashboard: true
      disableDashboardAd: true
      insecure: false
      debug: true
    serversTransport:
      insecureSkipVerify: true
    entryPoints:
      web:
        address: ':80'
        http:
          redirections:
            entryPoint:
              to: 'webs'
              scheme: 'https'
              permanent: true
      webs:
        address: ':443'
        asDefault: true
        http:
          tls:
            certResolver: 'lets_encrypt'
            domains:
              - main: 'example.com'
                sans: '*.example.com'
          middlewares:
            - 'google_email_whitelist@file'  # Use ODIC to whitelist users.
            - 'default_error_page@file'
            - 'geoblock_cn_ru@file'

    certificatesResolvers:
      lets_encrypt:
        acme:
          email: 'contact@example.com'
          storage: '/var/lib/traefik/acme.json'
          caServer: 'https://acme-v02.api.letsencrypt.org/directory'
          dnsChallenge:
            provider: 'gcloud'
            resolvers:
              - 'ns-cloud-e1.googledomains.com.'
              - 'ns-cloud-e2.googledomains.com.'
              - 'ns-cloud-e3.googledomains.com.'
              - 'ns-cloud-e4.googledomains.com.'
            propagation:
              delayBeforeChecks: '120s'
              disableChecks: true

    providers:
      file:
        directory: '/etc/traefik/dynamic'
        watch: true

    experimental:
      plugins:
        geoblock:
          moduleName: 'github.com/PascalMinder/geoblock'
          version: 'v0.3.3'
        traefikoidc:
          moduleName: 'github.com/lukaszraczylo/traefikoidc'
          version: 'v0.7.10'
    ```

See [Auth0 audience guide][a] for token validation.
!!! abstract "/etc/traefik/dynamic/middleware.yml"
    0640 traefik:traefik
    ``` yaml
    ---
    http:
      middlewares:
        # Only allow authenticated Google users.
        google_email_whitelist:
          plugin:
            traefikoidc:
              providerURL: 'https://accounts.google.com'
              clientID: '{CLIENT_ID}'
              clientSecret: '{CLIENT_SECRET}'
              # Generate random key with: openssl rand -hex 16
              sessionEncryptionKey: '{RANDOM_KEY}'

              # When sharing services between multiple subdomains a shared
              # cookie domain is required to prevent CSRF token missing in
              # session errors. Reduces security posture.
              cookieDomain: '.example.com'

              # Redirect URI used in configuration.
              callbackURL: '/oauth2/callback'
              logoutURL: '/oauth2/logout'

              # Require HTTPS for redirect URI's.
              forceHTTPS: true

              # Reject sessions with audience mis-match.
              strictAudienceValidation: true

              # Opaque (non-JWT) detection and inspection.
              allowOpaqueTokens: true
              requireTokenIntrospection: true

              # Force re-auth every hour.
              sessionMaxAge: 3600

              scopes:
                - roles  # Appended to defaults: openid, profile, email, roles

              # Only Authenticated users below will be allowed.
              allowedUsers:
                - '{USER}@gmail.com'
    ```


## Reference[^1][^2]

[^1]: https://www.simplehomelab.com/google-oauth-traefik-forward-auth-2024/
[^2]: https://github.com/lukaszraczylo/traefikoidc

[a]: https://github.com/lukaszraczylo/traefikoidc/blob/main/docs/AUTH0_AUDIENCE_GUIDE.md
[b]: https://docs.cloud.google.com/identity-platform/docs/web/mfa