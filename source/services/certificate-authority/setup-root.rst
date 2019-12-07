.. _service-certificate-authority-setup-root:

`Setup Root CA`_
################
The root CA should **never** be used other than to create or revoke intermediate
CAs. It should always be kept offline and secured once intermediate CAs are
setup. A compromise of the root CA key will compromise **all** child
certificates.

Create Root CA OpenSSL Configuration
************************************
A `good default`_ is here. This configuration should only contain relevant
sections for the required Root CA actions. Configuration file **must** be
specified when issuing Root CA operations otherwise the systemwide
``openssl.conf`` default configuration will be used.

.. literalinclude:: source/root.ca
  :caption: **0600 root root** ``/root/ca/root/root.ca``

Create Root CA Private Key and Certificate
******************************************
Should be done on an **air-gapped** machine and stored encrypted offline once
the intermediate CA is setup. Root CA should rarely be used.

.. code-block:: bash
  :caption: Create the private key.

  openssl genrsa -aes256 -out /root/ca/root/private/root.key.pem 4096
  chmod 0400 /root/ca/root/private/root.key.pem

.. code-block:: bash
  :caption: Create the Root CA Certficate.

  openssl req -config /root/ca/root/root.ca -key /root/ca/root/private/root.key.pem -new -x509 -days 7300 -sha512 -extensions v3_ca -out /root/ca/root/certs/root.cert.pem
  chmod 444 /root/ca/root/certs/root.cert.pem
  openssl x509 -noout -text -in /root/ca/root/certs/root.cert.pem

* A long lifetime (7300 days, 20 years) for an offline Root CA is OK. When the
  Root CA expires, **all** child certificates become invalid.
* Defaults from ``root.ca`` will autofill CA certificate fields.

.. _Setup Root CA: https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html
.. _good default: https://jamielinux.com/docs/openssl-certificate-authority/appendix/root-configuration-file.html