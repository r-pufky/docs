[Let's][3g] Encrypt
===================
Setting up a stand-alone signed SSL certificate for use on personal systems,
using Let's Encrypt Docker container with _DNS-01_ verification.

This is for personal use only, and doesn't account for specific nation-state
attacks, which could include MITM or a compromise of Let's Encrypt servers or
the ACME protocol. [Don't consider this secure][tu]. It is better than having
people accepting self-signed certificates, and it enables use of verifed SSL for
things like mail and web services.

1. [Ports](#ports)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Checking Certificates](#checking-certificates)

Ports
-----
None. The container will automatically add a `_acme_challenge` `TXT` record to
your DNS server, confirming you own the domain, and download the signed
certificates. No exposed ports are required.

Important File Locations
------------------------
Relative to docker container.

| File                                    | Purpose                                         |
|-----------------------------------------|-------------------------------------------------|
| /etc/letsencrypt                        | Standard letencrypt directory. Can be imported. |
| /etc/letsencrypt/domains.conf           | Domains to obtain certificates for.             |
| /etc/letsencrypt/lexicon_{PROIVDER}.yml | DNS provider auth settings.                     |

Docker Creation
---------------
This container will automatically pull new certificates if none are found in the
mapped _/etc/letsencrypt_ directory. Renewal requests automatically happen every
_12 hours_. Be sure to restart the container if changes are made.

* `LETSENCRYPT_STAGING` will run requests against the staging server, allowing
  the ability to test setup.
* `LEXICON_SLEEP_TIME` is the delay in seconds to validate DNS after making
  auth challenge change to the domain. Set to `150` as Google Cloud DNS
  guarantees updates in 120 seconds.

Docker Compose:
```yaml
letsencrypt:
  image: adferrand/letsencrypt-dns:latest
  restart: unless-stopped
  environment:
    - LETSENCRYPT_STAGING=True
    - LEXICON_SLEEP_TIME=150
    - LETSENCRYPT_USER_EMAIL=user@account.com
    - CERTS_DIRS_MODE=0750
    - CERTS_FILES_MODE=0640
    - CERTS_USER_OWNER=root
    - CERTS_GROUP_OWNER=root
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/letsencrypt:/etc/letsencrypt
    - /etc/localtime:/etc/localtime:ro
```
* Let's Encrypt local mount should just point the install location of let's
  encrypt, typically _/etc/letsencrypt_.

Initial Setup
-------------
### Create Domains to Manage
[Read Documentation][3g]. A certificate will be created for the contents of each
line.

/etc/letsencrypt/domains.conf `root:root 0644`
```
*.example.com
*.example2.com
*.example3.com *.example4.com
```
* This will produce three certificates:
  1. *.example.com
  1. *.example2.com
  1. *.example3.com,*.example4.com
* Changing or removing domains in this file will result in a request for new
  certificates (or deletion of existing ones) respectively on next renewal
  check.

### Setup Auth for DNS Provider.
This will cover [Google Cloud DNS][wp] (**not** domains.google.com; that has no
API). domains.google.com can be setup to use Google Cloud DNS servers for a
domain.

[Lexicon][iv] is used to modify your domains, but requires specific
authentication for each differ provider. To find out your provider options:
```bash
docker run -it --rm adferrand/letsencrypt-dns lexicon --help
docker run -it --rm adferrand/letsencrypt-dns lexicon <PROVIDER> --help
```
* Find your provider in the list, then find the required AUTH items. Follwo
  instructions.
* These options are passed either to the environment container as
  `LEXICON_{PROVIDER}_AUTH_SOMEVAR` or `{provider}_auth_somevar` in YAML.

The provider options can be passed in container environment, or preferrably in
`/etc/letsencrypt/lexicon_{PROVIDER}.yml`. Be sure to secure (`0750`) this file
as it gives full control over your domain.

/etc/letsencrypt/lexicon_googleclouddns.yml `root:root 0640`
```yaml
auth_service_account_info: >-
  base64::asdfJDFDx99dsafd ...
```
* Keys are `lexicon` provider options using lower_with_underscores.
* Google Cloud auth token requires base64 encoding if used in YAML file (per
  lexicon). `base64 cloud-dns-auth-token.json`.

### View Status
Watch the container logs for renewal status and messages:
```bash
docker logs -f letsencrypt
```

Checking Certificates
---------------------
See the current certificates that are being managed by the container:
```bash
docker exec -it letsencrypt sh
certbot certificates
```

[tu]: https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939
[3g]: https://github.com/adferrand/docker-letsencrypt-dns
[wp]: cloud.google.com
[iv]: https://github.com/AnalogJ/lexicon