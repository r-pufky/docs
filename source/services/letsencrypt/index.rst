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

Files
*****
.. files:: Let's Encrypt Files
  :value0: /etc/letsencrypt, Standard letencrypt directory. Can be imported.
  :value1: /etc/dnsrobocert/config.yml, Certificate configuration settings
  :open:

Docker Creation
***************
This container will automatically pull new certificates if none are found in the
mapped ``/etc/letsencrypt`` directory. Renewal requests automatically happen
every **12 hours**. Be sure to restart the container if changes are made.

.. code-block:: yaml
  :caption: Docker Compose

  letsencrypt:
    image: adferrand/dnsrobocert:latest
    restart: unless-stopped
    environment:
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/dnsrobocert:/etc/dnsrobocert
      - /data/services/letsencrypt:/etc/letsencrypt
      - /etc/localtime:/etc/localtime:ro

* Let's Encrypt local mount should just point the install location of let's
  encrypt, typically ``/etc/letsencrypt``.

.. _service-letsencrypt-domains:

Initial Setup
*************
Set configuration file before starting container. See `Configuration Reference`_.

.. literalinclude:: source/config.yml
  :caption: **0400 root root** ``/etc/dnsrobocert/config.yml``

.. danger::
  Secure this file as it gives full control over your DNS domain. Changing or
  removing domains in this file will result in a request for new certificates
  (or deletion of existing ones) respectively on next renewal check.

.. important::
  `Lexicon`_ is used to modify your domains, but requires specific
  authentication for each differ provider.

  See `Lexicon Providers`_ for specific options for each supported DNS provider.

.. note::
  ``sleep_time`` is the delay in seconds to validate DNS after making auth
  challenge change to the domain. Set to ``150`` as Google Cloud DNS guarantees
  updates in 120 seconds.

  ``staging`` will run requests against the staging server, allowing the ability
  to test setup.

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
.. _Let's Encrypt Docker and Documentation: https://hub.docker.com/r/adferrand/dnsrobocert
.. _Source Documentation: https://dnsrobocert.readthedocs.io/en/latest/index.html
.. _Configuration Reference: https://dnsrobocert.readthedocs.io/en/latest/configuration_reference.html
.. _Lexicon Providers: https://dnsrobocert.readthedocs.io/en/latest/providers_options.html
.. _Lexicon: https://github.com/AnalogJ/lexicon
