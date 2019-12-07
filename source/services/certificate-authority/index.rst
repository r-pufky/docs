.. _service-certificate-authority:

`Certificate Authority`_
########################
Run your own Ceritificate Authority which provides authentication and
authorization for services you own. An excellent reference for `basic CA setup
and usage`_ is here and should be well understood before proceeding.

This will setup a functional root CA, intermediate CA and client/server
certificate signing.

.. tip::
  Only minimal certificate fields are used, any actual public usage should
  provide all fields.

#. :ref:`service-certificate-authority-setup`.
#. :ref:`service-certificate-authority-setup-root`.
#. :ref:`service-certificate-authority-setup-intermediate`.
#. :ref:`service-certificate-authority-server-certificate`.
#. :ref:`service-certificate-authority-machine-certificate`.
#. :ref:`service-certificate-authority-client-certificate`.
#. :ref:`service-certificate-authority-exporting-certificates`.
#. :ref:`service-certificate-authority-certificate-revocation-lists`.

.. _Certificate Authority: https://www.openssl.org/
.. _basic CA setup and usage: https://jamielinux.com/docs/openssl-certificate-authority/introduction.html

.. toctree::
  :hidden:
  :includehidden:
  :maxdepth: -1

  setup
  setup-root
  setup-intermediate
  server-certificates
  machine-certificates
  client-certificates
  exporting-certificates
  certificate-revocation-lists