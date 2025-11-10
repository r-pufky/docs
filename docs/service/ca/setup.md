# Setup

## Locations
Assumed locations for configuration.

 Path                 | Data
---------------------:|------------------------------------------------------------------
 /root/ca/root        | Root CA data (Assumes all CA data stored in **/root**)
 /root/ca/inter       | Intermediate CA data
 /root/ca/inter/certs | Certificates signed by Intermediate CA
 /root/ca/inter/crl   | Certification Revocation List for Intermediate CA
 /root/ca/pfx         | Exported and encrypted pkcs#12 pfx files for client distribution

## Create Structure
``` bash
# Setup basic structure required to operate CA for client authentication and revocation lists.
mkdir -p /root/ca/root/{certs,crl,newcerts,private} /root/ca/inter/{certs,crl,csr,newcerts,private} /root/ca/pfx
chmod 0700 /root/ca/{root,inter}/private
touch /root/ca/{root,inter}/index.txt
echo 1000 | tee /root/ca/root/serial /root/ca/inter/serial
echo 'unique_subject = no' | tee /root/ca/root/index.txt.attr /root/ca/inter/index.txt.attr
echo 1000 > /root/ca/inter/crlnumber
```

## Root CA
The root CA should **never** be used other than to create or revoke
intermediate CAs. It should always be kept offline and secured once
intermediate CAs are setup. A compromise of the root CA key will compromise
**all** child certificates.

### Create Root CA OpenSSL Configuration
A [good default](https://jamielinux.com/docs/openssl-certificate-authority/appendix/root-configuration-file.html)
is here. This configuration should only contain relevant sections for the
required Root CA actions. Configuration file **must** be specified when issuing
Root CA operations otherwise the systemwide **openssl.conf** default
configuration will be used.

**/root/ca/root/root.ca** (1)
{ .annotate }

1. 0600 root:root
``` bash
# OpenSSL root CA configuration file.
# Stripped down to just Root CA functionality.
# https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html

[ ca ]
default_ca                     = CA_default

[ CA_default ]
# Directory and file locations.
dir                            = /root/ca/root
certs                          = $dir/certs
crl_dir                        = $dir/crl
new_certs_dir                  = $dir/newcerts
database                       = $dir/index.txt
serial                         = $dir/serial
RANDFILE                       = $dir/private/.rand

# The root key and root certificate.
private_key                    = $dir/private/root.key.pem
certificate                    = $dir/certs/root.cert.pem

# For certificate revocation lists.
crlnumber                      = $dir/crlnumber
crl                            = $dir/crl/root.crl.pem
crl_extensions                 = crl_ext
default_crl_days               = 375

default_md                     = sha512
name_opt                       = ca_default
cert_opt                       = ca_default
default_days                   = 375
preserve                       = no
policy                         = policy_strict

[ policy_strict ]
# The root CA should only sign intermediate certificates that match.
countryName                    = match
stateOrProvinceName            = match
organizationName               = match
organizationalUnitName         = optional
commonName                     = supplied
emailAddress                   = optional

[ req ]
# Applied when creating / signing certificates.
default_bits                   = 4096
distinguished_name             = req_distinguished_name
string_mask                    = utf8only
default_md                     = sha512
x509_extensions                = v3_ca

[ req_distinguished_name ]
# CSR information required, prompts and defaults.
countryName                    = Country Name (2 letter code)
stateOrProvinceName            = State or Province Name
localityName                   = Locality Name
0.organizationName             = Organization Name
organizationalUnitName         = Organizational Unit Name
commonName                     = Common Name
emailAddress                   = Email Address

# Default values for certification generation.
countryName_default            = XX
stateOrProvinceName_default    = XX
localityName_default           = XX
0.organizationName_default     = {CA NAME}
organizationalUnitName_default = {CA NAME} Certificate Authority
commonName_default             = {CA NAME} Root CA
emailAddress_default           = XX

[ v3_ca ]
# Root CA extenstions: man x509v3_config '-extensions v3_ca'
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid:always,issuer
basicConstraints               = critical, CA:true
keyUsage                       = critical, digitalSignature, cRLSign, keyCertSign

[ v3_intermediate_ca ]
# Intermediate CA extensions: man x509v3_config '-extensions v3_intermediate_ca'
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid:always,issuer
basicConstraints               = critical, CA:true, pathlen:0
keyUsage                       = critical, digitalSignature, cRLSign, keyCertSign

[ crl_ext ]
# Certificate revocation list extensions: man x509v3_config
authorityKeyIdentifier         = keyid:always

[ ocsp ]
# OCSP signing certificate extensions: man ocsp
basicConstraints               = CA:FALSE
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid,issuer
keyUsage                       = critical, digitalSignature
extendedKeyUsage               = critical, OCSPSigning
```

### Create Root CA Private Key and Certificate
Should be done on an **air-gapped** machine and stored encrypted offline once
the intermediate CA is setup. Root CA should rarely be used.

A long lifetime (7300 days, 20 years) for an offline Root CA is OK. When Root
CA expires, **all** child certificates become invalid.

``` bash
# Create the private key.
openssl genrsa -aes256 -out /root/ca/root/private/root.key.pem 4096
chmod 0400 /root/ca/root/private/root.key.pem

# Create the Root CA Certificate.
# Defaults from root.ca will autofill CA certificate fields.
openssl req -config /root/ca/root/root.ca -key /root/ca/root/private/root.key.pem -new -x509 -days 7300 -sha512 -extensions v3_ca -out /root/ca/root/certs/root.cert.pem
chmod 444 /root/ca/root/certs/root.cert.pem
openssl x509 -noout -text -in /root/ca/root/certs/root.cert.pem
```

Reference:

* https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html

## Intermediate CA
The Intermediate CA is the workhorse for certificate authorities. This will be
the main CA used for issuing and revoking server / client certificates.

### Create Intermediate CA Openssl Configuration
A [good default](https://jamielinux.com/docs/openssl-certificate-authority/appendix/intermediate-configuration-file.html)
is here. This configuration should only contain relevant sections for the
required Intermediate CA actions. Configuration file **must** be specified when
issuing Intermediate CA operations otherwise the systemwide **openssl.conf**
default configuration will be used.

**/root/ca/inter/inter.ca** (1)
{ .annotate }

1. 0600 root:root
``` bash
# OpenSSL intermediate CA configuration file.
# Stripped down to just Intermediate CA functionality.
# https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html

[ ca ]
default_ca                     = CA_default

[ CA_default ]
# Directory and file locations.
dir                            = /root/ca/inter
certs                          = $dir/certs
crl_dir                        = $dir/crl
new_certs_dir                  = $dir/newcerts
database                       = $dir/index.txt
serial                         = $dir/serial
RANDFILE                       = $dir/private/.rand

# The root key and root certificate.
private_key                    = $dir/private/inter.key.pem
certificate                    = $dir/certs/inter.cert.pem

# For certificate revocation lists.
crlnumber                      = $dir/crlnumber
crl                            = $dir/crl/inter.crl.pem
crl_extensions                 = crl_ext
default_crl_days               = 375

default_md                     = sha512
name_opt                       = ca_default
cert_opt                       = ca_default
default_days                   = 375
preserve                       = no
policy                         = policy_loose

[ policy_loose ]
# Allow the intermediate CA to sign a more diverse range of certificates.
countryName                    = optional
stateOrProvinceName            = optional
localityName                   = optional
organizationName               = optional
organizationalUnitName         = optional
commonName                     = supplied
emailAddress                   = optional

[ req ]
# Options for the 'openssl req' tool: man req
default_bits                   = 4096
distinguished_name             = req_distinguished_name
string_mask                    = utf8only
default_md                     = sha512
x509_extensions                = machine_cert

[ req_distinguished_name ]
# CSR information required, prompts and defaults.
countryName                    = Country Name (2 letter code)
stateOrProvinceName            = State or Province Name
localityName                   = Locality Name
0.organizationName             = Organization Name
organizationalUnitName         = Organizational Unit Name
commonName                     = Common Name
emailAddress                   = Email Address

# Default values for certification generation.
countryName_default            = XX
stateOrProvinceName_default    = XX
localityName_default           = XX
0.organizationName_default     = {CA NAME}
organizationalUnitName_default = {CA NAME} Certificate Authority
commonName_default             = {CA NAME} Intermediate CA
emailAddress_default           = XX

[ user_cert ]
# User certificate extensions: man x509v3_config '-extensions user_cert'
basicConstraints               = CA:FALSE
nsCertType                     = client, email
nsComment                      = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid,issuer
keyUsage                       = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage               = clientAuth, emailProtection

[ machine_cert ]
# Machine certificate extensions: man x509v3_config '-extensions machine_cert'
basicConstraints               = CA:FALSE
nsCertType                     = client
nsComment                      = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid,issuer
keyUsage                       = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage               = clientAuth

[ server_cert ]
# Server certificate extensions: man x509v3_config '-extensions server_cert'
basicConstraints               = CA:FALSE
nsCertType                     = server
nsComment                      = "OpenSSL Generated Server Certificate"
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid,issuer:always
keyUsage                       = critical, digitalSignature, keyEncipherment
extendedKeyUsage               = serverAuth

[ crl_ext ]
# Certificate revocation list extensions: man x509v3_config
authorityKeyIdentifier         = keyid:always

[ ocsp ]
# Extension for OCSP signing certificates: man ocsp
basicConstraints               = CA:FALSE
subjectKeyIdentifier           = hash
authorityKeyIdentifier         = keyid,issuer
keyUsage                       = critical, digitalSignature
extendedKeyUsage               = critical, OCSPSigning
```

Reference:

* https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html

### Create Intermediate CA Private Key and Certificate
Private key should be kept offline of live services, but accessible to enable
changes. Lifetimes for Intermediate CAs should be shorter than Root CAs.

The Root CA is used to sign the Intermediate CA. This creates a chain of trust.
Lifetime is half (3650 days, 10 years) for an Intermediate CA. When the
Intermediate CA expires, **all** child certificates become invalid.

``` bash
# Create the private key.
openssl genrsa -aes256 -out /root/ca/inter/private/inter.key.pem 4096
chmod 0400 /root/ca/inter/private/inter.key.pem

# Create the Intermediate CA Certificate.
# Defaults from inter.ca will autofill CA certificate fields.
openssl req -config /root/ca/inter/inter.ca -new -sha512 -key /root/ca/inter/private/inter.key.pem -out /root/ca/inter/csr/inter.csr.pem
openssl ca -config /root/ca/root/root.ca -extensions v3_intermediate_ca -days 3650 -notext -md sha512 -in /root/ca/inter/csr/inter.csr.pem -out /root/ca/inter/certs/inter.cert.pem
chmod 444 /root/ca/inter/certs/inter.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/inter.cert.pem
# Should return **OK**. This means that the Intermediate certificate is valid.
openssl verify -CAfile /root/ca/root/certs/root.cert.pem /root/ca/inter/certs/inter.cert.pem
```

### Create Intermediate Chain of Trust
The chain of trust is used to validate all certificates up to the Root CA. This
is usually deployed with server/client certificates if the Root CA is not added
to each machine's Trusted CA store.

``` bash
# Create Intermediate Chain of Trust.
cat /root/ca/inter/certs/inter.cert.pem /root/ca/root/certs/root.cert.pem > /root/ca/inter/certs/ca-chain.cert.pem
chmod 444 /root/ca/inter/certs/ca-chain.cert.pem
```
