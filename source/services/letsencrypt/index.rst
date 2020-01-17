.. _service-letsencrypt:

`Let's Encrypt`_
################
Setting up a stand-alone signed SSL certificate for use on personal systems,
using Let's Encrypt Docker container with ``DNS-01`` verification.

This is for personal use only, and doesn't account for specific nation-state
attacks, which could include MITM or a compromise of Let's Encrypt servers or
the ACME protocol. `Don't consider this secure`_. It is better than having
people accepting self-signed certificates, and it enables use of verifed SSL for
things like mail and web services.

See `Let's Encrypt Docker and Documentation`_. `Source Documentation`_.

Ports (Let's Encrypt)
*********************
None. The container will automatically add a ``_acme_challenge`` ``TXT`` record
to your DNS server, confirming you own the domain, and download the signed
certificates. **No** exposed ports are required.

.. gflocation:: Important File Locations (Let's Encrypt)
  :file:    /etc/letsencrypt,
            /etc/letsencrypt/domains.conf,
            /etc/letsencrypt/lexicon_{PROVIDER}.yml
  :purpose: Standard letencrypt directory. Can be imported.,
            Domains to obtain certificates for.,
            DNS provider auth settings.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
This container will automatically pull new certificates if none are found in the
mapped ``/etc/letsencrypt`` directory. Renewal requests automatically happen
every **12 hours**. Be sure to restart the container if changes are made.

* ``LETSENCRYPT_STAGING`` will run requests against the staging server, allowing
  the ability to test setup.
* ``LEXICON_SLEEP_TIME`` is the delay in seconds to validate DNS after making
  auth challenge change to the domain. Set to ``150`` as Google Cloud DNS
  guarantees updates in 120 seconds.

.. code-block:: yaml
  :caption: Docker Compose

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

* Let's Encrypt local mount should just point the install location of let's
  encrypt, typically ``/etc/letsencrypt``.

Initial Setup
*************

.. _service-letsencrypt-domains:

Create Domains to Manage
========================
A certificate will be created for the contents of each line.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/letsencrypt/domains.conf``

  *.example.com
  *.example2.com
  *.example3.com *.example4.com

* This will produce three certificates:

   #. ``*.example.com``
   #. ``*.example2.com``
   #. ``*.example3.com,*.example4.com``

.. note::
  Changing or removing domains in this file will result in a request for new
  certificates (or deletion of existing ones) respectively on next renewal
  check.

Setup Auth for DNS Provider
===========================
This will cover `Google Cloud DNS`_ (**not** ``domains.google.com`` -- this has
no API). ``domains.google.com`` can be setup to use Google Cloud DNS servers for
a domain.

`Lexicon`_ is used to modify your domains, but requires specific authentication
for each differ provider.

.. code-block:: bash
  :caption: To find out your provider options.

  docker run -it --rm adferrand/letsencrypt-dns lexicon --help docker run -it --rm adferrand/letsencrypt-dns lexicon {PROVIDER} --help

* Find your provider in the list, then find the required AUTH items. Follow
  instructions.
* These options are passed either to the environment container as
  ``LEXICON_{PROVIDER}_AUTH_SOMEVAR`` or ``{provider}_auth_somevar`` in YAML.

.. danger::
  The provider options can be passed in container environment, or preferrably in
  ``/etc/letsencrypt/lexicon_{PROVIDER}.yml``. Be sure to secure (``0640``) this
  file as it gives full control over your domain.

Create base64 encoded auth token.

.. code-block:: yaml
  :caption: **0640 root root** ``/etc/letsencrypt/lexicon_googleclouddns.yml``

  auth_service_account_info: >-
    base64::asdfJDFDx99dsafd ...

.. note::
  Keys are ``lexicon`` provider options using ``lower_with_underscores``.

  Google Cloud auth token **requires** base64 encoding if used in YAML file (per
  lexicon). ``base64 cloud-dns-auth-token.json``.

Check Status
************
.. code-block:: bash
  :caption: Watch the container logs for renewal status and messages.

  docker logs -f letsencrypt

Checking Certificates
*********************
.. code-block:: bash
  :caption: See the current certificates that are being managed by the container.

  docker exec -it letsencrypt sh
  certbot certificates

.. _Let's Encrypt: https://letsencrypt.org
.. _Don't consider this secure: https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939
.. _Let's Encrypt Docker and Documentation: https://hub.docker.com/r/adferrand/letsencrypt-dns
.. _Source Documentation: https://github.com/adferrand/docker-letsencrypt-dns
.. _Google Cloud DNS: cloud.google.com
.. _Lexicon: https://github.com/AnalogJ/lexicon