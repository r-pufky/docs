.. _service-certificate-authority-client-certificate:

`Client Certificates`_
######################
Client certificate to validate client identity. These are tied to a specific
user and only have ``clientAuth`` and ``emailProtection`` extensions added.

Create Client Private Key and Certificate
*****************************************
.. code-block:: bash
  :caption: Create the private key and certificate signing request.

  openssl genrsa -aes256 -out /root/ca/inter/private/{USER EMAIL}.key.pem 4096
  chmod 0400 /root/ca/inter/private/{USER EMAIL}.key.pem
  openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{USER EMAIL}.key.pem -new -sha512 -out /root/ca/inter/csr/{USER EMAIL}.csr.pem

.. gui::   Create Client Signing Request
  :path:   Create Client Signing Request
  :value0:                          Country Name (2 letter code) [XX], {ENTER}
  :value1:                                State or Province Name [XX], {ENTER}
  :value2:                                         Locality Name [XX], {ENTER}
  :value3:                              Organization Name [{CA NAME}], {ORG OR CA NAME}
  :value4: Organizational Unit Name [{CA NAME} Certificate Authority], {ORG OR CA NAME}
  :value5:                    Common Name [{CA NAME} Intermediate CA], {USER}
  :value6:                                         Email Address [XX], {EMAIL}

.. warning::
  This identifies a user and needs to contain enough information to identify
  that person. Certificate should also require a password to prevent identity
  impersonation.

.. code-block:: bash
  :caption: Sign certificate signing request.

  openssl ca -config /root/ca/inter/inter.ca -extensions user_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{USER EMAIL}.csr.pem -out /root/ca/inter/certs/{USER EMAIL}.cert.pem
  chmod 444 /root/ca/inter/certs/{USER EMAIL}.cert.pem
  openssl x509 -noout -text -in /root/ca/inter/certs/{USER EMAIL}.cert.pem
  openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{USER EMAIL}.cert.pem

* Client certificates should be much shorter lifetime that CA's.
* Clients can create their own CSR requests to be signed, meaning that the CA
  never needs to see the client private key.
* The verify command should return ``OK``.
* both ``ca-chain.cert.pem`` and ``{USER EMAIL}.cert.pem`` need to be
  distributed if Root CA is not in the trusted CA store.

See :ref:`service-nginx-chrome-client-certificate` to setup auto selection of
client certificate for matched sites.

.. _Client Certificates: https://jamielinux.com/docs/openssl-certificate-authority/sign-server-and-client-certificates.html
