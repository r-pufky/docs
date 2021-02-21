.. _service-certificate-authority-server-certificate:

`Server Certificates`_
######################
Used for providing SSL connections with services / servers. The Root CA must be
in the trusted Root CAs or the ca-chain deployed with clients for servers
presenting SSL connections using these certificates to be validated (green
lock). These certificates only have ``serverAuth`` extensions added.

Letsencrypt certificates should be used here instead of self-signed certs.

Create Server Private Key and Certificate
*****************************************
.. code-block:: bash
  :caption: Create the private key and certificate signing request.

  openssl genrsa -out /root/ca/inter/private/{SERVER}.key.pem 4096
  chmod 0400 /root/ca/inter/private/{SERVER}.key.pem
  openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{SERVER}.key.pem -new -sha512 -out /root/ca/inter/csr/{SERVER}.csr.pem

.. gui::   Create Server Signing Request
  :path:   Create Server Signing Request
  :value0:                          Country Name (2 letter code) [XX], {ENTER}
  :value1:                                State or Province Name [XX], {ENTER}
  :value2:                                         Locality Name [XX], {ENTER}
  :value3:                              Organization Name [{CA NAME}], {ENTER}
  :value4: Organizational Unit Name [{CA NAME} Certificate Authority], {SERVER}
  :value5:                    Common Name [{CA NAME} Intermediate CA], *.example.com
  :value6:                                         Email Address [XX], {ENTER}

.. warning::
  Requiring a password ``-aes256`` for the private key will require that
  password to be entered everytime the certifcate is used (e.g. service is
  started). Given the short lived nature of these certificates, generally no
  password is used and CRL/OSCP are used to invalidate any exposed certificates.

.. code-block:: bash
  :caption: Sign certificate signing request.

  openssl ca -config /root/ca/inter/inter.ca -extensions server_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{SERVER}.csr.pem -out /root/ca/inter/certs/{SERVER}.cert.pem
  chmod 444 /root/ca/inter/certs/{SERVER}.cert.pem
  openssl x509 -noout -text -in /root/ca/inter/certs/{SERVER}.cert.pem
  openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{SERVER}.cert.pem

* Server certificates should be much shorter lifetime that CA's. Typically a
  little over a year.
* The verify command should return ``OK``.
* both ``ca-chain.cert.pem`` and ``{SERVER}.cert.pem`` need to be distributed if
  Root CA is not in the trusted CA store.

.. _Server Certificates: https://jamielinux.com/docs/openssl-certificate-authority/sign-server-and-client-certificates.html
