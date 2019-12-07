.. _service-certificate-authority-machine-certificate:

`Machine Certificates`_
#######################
Special type of client certificate used to validate a *machine* hardware
identity. These are tied to a specific machine and only have ``clientAuth``
extensions added.

Create Machine Private Key and Certificate
******************************************
.. code-block:: bash
  :caption: Create the private key and certificate signing request.

  openssl genrsa -out /root/ca/inter/private/{MACHINE}.key.pem 4096
  chmod 0400 /root/ca/inter/private/{MACHINE}.key.pem
  openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{MACHINE}.key.pem -new -sha512 -out /root/ca/inter/csr/{MACHINE}.csr.pem

.. ggui:: Create Machine Signing Request.
  :option:  Country Name (2 letter code) [XX],
            State or Province Name [XX],
            Locality Name [XX],
            Organization Name [{CA NAME}],
            Organizational Unit Name [{CA NAME} Certificate Authority],
            Common Name [{CA NAME} Intermediate CA],
            Email Address [XX]
  :setting: {ENTER},
            {ENTER},
            {ENTER},
            {MACHINE},
            machine,
            {MACHINE}.machine,
            {ENTER}
  :no_key_title:
  :no_section:
  :no_launch:

.. warning::
  Requiring a password ``-aes256`` for the private key will require that
  password to be entered everytime the certifcate is used (e.g. authenticating
  to a service). Given the short lived nature of these certificates and that it
  is providing a machine identity, generally no password is used and CRL/OSCP
  are used to invalidate any exposed certifiates to prevent access.

.. code-block:: bash
  :caption: Sign certificate signing request.

  openssl ca -config /root/ca/inter/inter.ca -extensions machine_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{MACHINE}.csr.pem -out /root/ca/inter/certs/{MACHINE}.cert.pem
  chmod 444 /root/ca/inter/certs/{MACHINE}.cert.pem
  openssl x509 -noout -text -in /root/ca/inter/certs/{MACHINE}.cert.pem
  openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{MACHINE}.cert.pem

* Machine certificates should be much shorter lifetime that CA's. They should be
  revoked and re-created whenever a machine is new or re-installed.
* The verify command should return ``OK``.
* both ``ca-chain.cert.pem`` and ``{MACHINE}.cert.pem`` need to be distributed
  if Root CA is not in the trusted CA store.

.. _Machine Certificates: https://jamielinux.com/docs/openssl-certificate-authority/sign-server-and-client-certificates.html