.. _service-certificate-authority-setup:

`Certificate Authority`_ Setup
##############################
.. gflocation:: Important File Locations (Certificate Authority)
  :file:    /root/ca/root,
            /root/ca/inter,
            /root/ca/inter/certs,
            /root/ca/inter/crl,
            /root/ca/pfx
  :purpose: Root CA data.,
            Intermediate CA data.,
            Certificates signed by Intermediate CA.,
            Certification Revocation List for Intermediate CA.,
            Exported and encrypted pkcs#12 pfx files for client distribution.
  :no_key_title:
  :no_caption:
  :no_launch:

.. code-block:: bash
  :caption: Setup basic structure required to operate CA for client authentication and revocation lists.

  mkdir -p /root/ca/root/{certs,crl,newcerts,private} /root/ca/inter/{certs,crl,csr,newcerts,private} /root/ca/pfx
  chmod 0700 /root/ca/{root,inter}/private
  touch /root/ca/{root,inter}/index.txt
  echo 1000 | tee /root/ca/root/serial /root/ca/inter/serial
  echo 'unique_subject = no' | tee /root/ca/root/index.txt.attr /root/ca/inter/index.txt.attr
  echo 1000 > /root/ca/inter/crlnumber

.. note::
  Assumes all CA data will be stored in ``/root/``.

.. _Certificate Authority: https://www.openssl.org/