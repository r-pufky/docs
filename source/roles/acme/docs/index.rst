.. _service-letsencrypt:

Let's Encrypt
#############
Stand-alone signed SSL certificate for use on personal systems using Let's
Encrypt and ACME protocol with **DNS-01** verification.

.. role:: acme
  :service_doc: https://dnsrobocert.readthedocs.io/en/latest/index.html
  :ref:         https://letsencrypt.org
  :private:
  :update:      2022-10-09
  :open:

  This is for personal use only, and doesn't account for specific nation-state
  attacks, which could include MITM or a compromise of Let's Encrypt servers or
  the ACME protocol. `Don't consider this secure <https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939>`_.
  It is better than having people accepting self-signed certificates, and it
  enables use of verifed SSL for things like mail and web services.

  * Automatically adds a ``_acme_challenge`` ``TXT`` record to your DNS server,
    confirming you own the domain, and download the signed certificates. **No**
    exposed ports are required.
  * Automatically pulls new certificates if none are found in ``acme_cert``.
    Renewal requests automatically happen every **12 hours**. Be sure to
    restart if changes are made.
  * `Lexicon <https://github.com/AnalogJ/lexicon>`_ is used to modify your
    domains, but requires specific authentication for each differ provider. See
    `Lexicon Providers <https://dnsrobocert.readthedocs.io/en/latest/providers_options.html>`_
    for specific options for each supported DNS provider.
  * Use the `Configuration Reference <https://dnsrobocert.readthedocs.io/en/latest/configuration_reference.html>`_
    and the example config to setup for your specifc DNS providers.

Defaults
********
.. literalinclude:: ../defaults/main.yml

Example Config:
***************
.. literalinclude:: source/config.yml
