Let's Encrypt
-------------
Setting up a stand-alone signed SSL certificate for use on personal systems,
using Let's Encrypt Docker container with DNS-01 verification.

This is for personal use only, and doesn't account for specific nation-state
attacks, which could include MITM or a compromise of Let's Encrypt servers or
the ACME protocol. [Don't consider this secure][1]. It is better than having
people get used to accepting self-signed certificates, and it enables use of
verifed SSL for things like mail and web services.

[Docker repository][2]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Initial Setup](#initial-setup)
1. [Checking Certificates](#checking-certificates)

Docker Ports Exposed
--------------------
None. The container will automatically add a `_acme_challenge` `TXT` record to
your DNS server, confirming you own the domain, and download the signed
certificates. No exposed ports are required.

Important File Locations
------------------------
Relative to docker container

| File                                    | Purpose                                         |
|-----------------------------------------|-------------------------------------------------|
| /etc/letsencrypt                        | Standard letencrypt directory. Can be imported. |
| /etc/letsencrypt/domains.conf           | Domains to obtain certificates for.             |
| /etc/letsencrypt/lexicon_<PROIVDER>.yml | DNS provider auth settings.                     |

Docker Creation
---------------
This container will automatically pull new certificates if none are found in the
mapped `/etc/letsencrypt` directory. Renewal requests automatically happen every
`12 hours`. Be sure to restart the contain if changes are made.

* `LETSENCRYPT_STAGING` will run requests against the staging server, allowing
  the ability to test setup.
* `LEXICON_SLEEP_TIME` is the delay in seconds to validate DNS after making
  auth challenge change to the domain. Set to `150` as Google Cloud DNS
  guarantees updates in 120 seconds.

### Independant Container
```bash
docker run -t -d \
  --name=letsencrypt \
  --restart=unless-stopped \
  -e LETSENCRYPT_STAGING=True \
  -e LEXICON_SLEEP_TIME=150 \
  -e LETSENCRYPT_USER_EMAIL=user@account.com \
  -e CERTS_DIRS_MODE=0750 \
  -e CERTS_FILES_MODE=0640 \
  -e CERTS_USER_OWNER=root \
  -e CERTS_GROUP_OWNER=root \
  -e TZ=America/Los_Angeles \
  -v /data/services/letsencrypt:/etc/letsencrypt \
  -v /etc/localtime:/etc/localtime:ro
  adferrand/letsencrypt-dns:latest
```
* Use `-t -d` is needed to keep the container in interactive mode otherwise as
  soon as the container is idle it will sleep, which will stop background
  running services.

### Docker Compose
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
  encrypt, typically `/etc/letsencrypt`.

Initial Setup
-------------
### Create Domains to Manage
[Read Documentation][2]. A certificate will be created for the contents of each
line.

/etc/letsencrypt/domains.conf
```
*.example.com
*.example2.com
*.example3.com *.example4.com
```
* This will produce three certificates, 1) *.example.com, 2) *.example2.com,
  3) *.example3.com,*.example4.com
* Changing or removing domains in this file will result in a request for new
  certificates (or deletion of existing ones) respectively on next renewal
  checkin.

### Setup Auth for DNS Provider.
This will cover [Google Cloud DNS][3] (**not** domains.google.com; that has no
API). Domains.google can be setup to use Google Cloud DNS servers for a domain.

[Lexicon][4] is used to modify your domains, but requires specific
authentication for each differ provider. To find out your provider options:

```bash
docker run -it --rm adferrand/letsencrypt-dns lexicon --help
docker run -it --rm adferrand/letsencrypt-dns lexicon <PROVIDER> --help
```
* Find your provider in the list, then find the required AUTH items. Follwo
  instructions.
* These options are passed either to the environment container as
  `LEXICON_<PROVIDER>_AUTH_SOMEVAR` or `<provider>_auth_somevar` in YAML.

The provider options can be passed in container environment, or preferrably in
`/etc/letsencrypt/lexicon_<PROVIDER>.yml`. Be sure to secure (`0750`) this file
as it gives full control over your domain.

/etc/letsencrypt/lexicon_googleclouddns.yml
```yaml
auth_service_account_info: >-
  base64::asdfJDFDx99dsafd ...
```
* Keys are `lexicon` provider options as lower_with_underscores.
* Google Cloud auth token requires base64 encoding if used in YAML file (per
  lexicon). `base64 cloud-dns-auth-token.json`.

### View Status
Watch the container logs for renewal status and messages.

```bash
docker logs -f letsencrypt
```

Checking Certificates
---------------------
See the current certificates that are being managed by the container.

```bash
docker exec -it letsencrypt sh
certbot certificates
```

[1]: https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939
[2]: https://github.com/adferrand/docker-letsencrypt-dns
[3]: cloud.google.com
[4]: https://github.com/AnalogJ/lexicon