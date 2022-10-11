.. _service-certificate-authority-certificate-revocation-lists:

`Certificate Revocation Lists`_
###############################
Certificate Revocation Lists (CRLs) are used to invalidate certificates in the
wild which have been compromised. This covers server-side revocation
enforcement. A CRL should include all of the CRL's up to the Root CA.

.. code-block:: bash
  :caption: Create CRL.

  openssl ca -config /root/ca/root/root.ca -gencrl -out /root/ca/root/crl/root.crl.pem
  openssl ca -config /root/ca/inter/inter.ca -gencrl -out /root/ca/inter/crl/inter.crl.pem
  cat /root/ca/root/crl/root.crl.pem /root/ca/inter/crl/inter.crl.pem > /root/ca/ca-chain.crl.pem

.. note::
  Run these commands to regenerate the CRL's automatically with a new serial
  number and expiry date. Expired CRL's will lead to certificate authentication
  failures!

.. code-block:: bash
  :caption: Check Current CRL Status.

  openssl crl -in /root/ca/root/crl/root.crl.pem -noout -text
  openssl crl -in /root/ca/inter/crl/inter.crl.pem -noout -text
  openssl crl -in /root/ca/ca-chain.crl.pem -noout -text

Revoking Certificate
********************
This will prevent a compromised certificate (which is still valid) from being
used.

.. code-block:: bash
  :caption: Revoke Certificate and Update CRL.

  openssl ca -config /root/ca/inter/inter.ca -revoke /root/ca/inter/certs/{TARGET}.cert.pem
  openssl ca -config /root/ca/inter/inter.ca -gencrl -out /root/ca/inter/crl/inter.crl.pem
  cat /root/ca/root/crl/root.crl.pem /root/ca/inter/crl/inter.crl.pem > /root/ca/ca-chain.crl.pem

* The new CRL needs to be deployed to any service using the Intermediate CA.
* This can also be applied at the Root CA level to revoke intermediate CA's.
* The combined CRL needs to be re-created as well.

.. _Certificate Revocation Lists: https://jamielinux.com/docs/openssl-certificate-authority/certificate-revocation-lists.html
