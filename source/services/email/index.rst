.. _service-email:

Email
#####
Self-hosted email services (:term:`MDA`, :term:`MTA`, :term:`MUA`).

You must be able to setup DNS for your domain to use the security options.

Setup focuses on running a :term:`MTA` using the latest security options, with
a proxy authentication webface; disabling POP3 and IMAP access.

See `Email Docker and Documentation`_.

#. :ref:`service-email-mta-setup`.
#. :ref:`service-email-mta-configuration`.
#. :ref:`service-email-mta-testing`.
#. :ref:`service-email-mua-setup`.

.. _Email Docker and Documentation: https://hub.docker.com/r/tvial/docker-mailserver/

.. toctree::
   :hidden:
   :maxdepth: -1

   mta/index
   mua/setup
