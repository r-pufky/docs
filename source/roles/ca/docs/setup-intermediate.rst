.. _service-certificate-authority-setup-intermediate:

`Setup Intermediate CA`_
########################
The Intermediate CA is the workhorse for certificate authorities. This will be
the main CA used for issuing and revoking server / client certificates.

Create Intermediate CA Openssl Configuration
********************************************
A `good default`_ is here. This configuration should only contain relevant
sections for the required Intermediate CA actions. Configuration file **must**
be specified when issuing Intermediate CA operations otherwise the systemwide
``openssl.conf`` default configuration will be used.

.. literalinclude:: source/inter.ca
  :caption: **0600 root root** ``/root/ca/inter/inter.ca``

Create Intermediate CA Private Key and Certificate
**************************************************
Private key should be kept offline of live services, but accessible to enable
changes. Lifetimes for Intermediate CAs should be shorter than Root CAs.

.. code-block:: bash
  :caption: Create the private key.

  openssl genrsa -aes256 -out /root/ca/inter/private/inter.key.pem 4096
  chmod 0400 /root/ca/inter/private/inter.key.pem

.. code-block:: bash
  :caption: Create the Intermediate CA Certficate.

  openssl req -config /root/ca/inter/inter.ca -new -sha512 -key /root/ca/inter/private/inter.key.pem -out /root/ca/inter/csr/inter.csr.pem
  openssl ca -config /root/ca/root/root.ca -extensions v3_intermediate_ca -days 3650 -notext -md sha512 -in /root/ca/inter/csr/inter.csr.pem -out /root/ca/inter/certs/inter.cert.pem
  chmod 444 /root/ca/inter/certs/inter.cert.pem
  openssl x509 -noout -text -in /root/ca/inter/certs/inter.cert.pem
  openssl verify -CAfile /root/ca/root/certs/root.cert.pem /root/ca/inter/certs/inter.cert.pem

* Defaults from ``inter.ca`` will autofill Intermediate CA certificate fields.
* The Root CA is used to sign the Intermediate CA. This creates a chain of
  trust.
* Lifetime is half (3650 days, 10 years) for an Intermediate CA. When the
  Intermediate CA expires, **all** child certificates become invalid.
* The ``verify`` command should return **OK**. This means that the Intermediate
  certificate is currently valid.

Create Intermediate Chain of Trust
**********************************
The chain of trust is used to validate all certificates up to the Root CA. This
is usually deployed with server/client certificates if the Root CA is not added
to each machine's Trusted CA store.

.. code-block:: bash
  :caption: Create Intermediate Chain of Trust.

  cat /root/ca/inter/certs/inter.cert.pem /root/ca/root/certs/root.cert.pem > /root/ca/inter/certs/ca-chain.cert.pem
  chmod 444 /root/ca/inter/certs/ca-chain.cert.pem

.. _Setup Intermediate CA: https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html
.. _good default: https://jamielinux.com/docs/openssl-certificate-authority/appendix/intermediate-configuration-file.html