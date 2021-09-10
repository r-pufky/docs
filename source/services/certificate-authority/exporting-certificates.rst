.. _service-certificate-authority-exporting-certificates:

Exporting Certificates
######################
PKCS #12 PFX (Personal Information Exchange Certificate) is an encrypted
singular file archive format used to distribute a bundle of certificates
securely to a client. This is used to securely distribute key/cert material to
clients.

.. code-block:: bash
  :caption: Pack client certificates and private keys into pfx.

  openssl pkcs12 -export -out /root/ca/pfx/{CLIENT}.pfx -inkey /root/ca/inter/private/{CLIENT}.key.pem -in /root/ca/inter/certs/{CLIENT}.cert.pem -certfile /root/ca/inter/certs/ca-chain.cert.pem

* Set a **strong export** password **different** from and private key password
  -- this prevents the bundle from being installed and used without knowing
  password.
* ``ca-chain`` is included to provide chain of trust to the client using the
  certificate and validate the server.

Extract Public/Private Keys from PFX
************************************
Keys can be extracted from the PFX file for use if needed.

.. code-block:: bash
  :caption: Extract RSA private key (using PEM keypair)

  openssl pkcs12 -in {CLIENT}.pfx -nocerts -nodes | openssl rsa -out rsa.key

.. code-block:: bash
  :caption: Extract RSA public key 

  openssl pkcs12 -in {CLIENT}.pfx -clcerts -nokeys | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > rsa.pub
