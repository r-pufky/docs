[Certificate Authority][3k]
===========================
Run your own Ceritificate Authority which provides authentication and
authorization for services you own. An [**excellent reference** for basic CA
setup and usage][kx] is here and should be well understood before proceeding.

This will setup a functional root CA, intermediate CA and client/server
certificate signing.

> :thought_balloon:  
> Only minimal certificate fields are used, any actual public usage should
> provide all fields.

1. [Important File Locations](#important-file-locations)
1. [Initial Setup](#initial-setup)
1. [Setup Root CA](#setup-root-ca)
   * [Create Root CA Openssl Configuration](#create-root-ca-openssl-configuration)
   * [Create Root CA Private Key and Certificate](#create-root-ca-private-key-and-certificate)
1. [Setup Intermediate CA](#setup-intermediate-ca)
   * [Create Intermediate CA Openssl Configuration](#create-intermediate-ca-openssl-configuration)
   * [Create Intermediate CA Private Key and Certificate](#create-intermediate-ca-private-key-and-certificate)
   * [Create Intermediate Chain of Trust](#create-intermediate-chain-of-trust)
1. [Server Certificates](#server-certificates)
   * [Create Server Private Key and Certificate](#create-server-private-key-and-certificate)
1. [Machine Certificates](#machine-certificates)
   * [Create Machine Private Key and Certificate](#create-machine-private-key-and-certificate)
1. [Client Certificates](#client-certificates)
   * [Create Client Private Key and Certificate](#create-client-private-key-and-certificate)
1. [Exporting Certificates](#exporting-certificates)
1. [Certificate Revocation Lists](#certificate-revocation-lists)
   * [Revoking Certificates](#revoking-certificates)

Important File Locations
------------------------
Relative to docker container.

| File                 | Purpose                                                        |
|----------------------|----------------------------------------------------------------|
| /root/ca/root        | Root CA data.                                                  |
| /root/ca/inter       | Intermediate CA data.                                          |
| /root/ca/inter/certs | Certificates signed by Intermediate CA.                        |
| /root/ca/inter/crl   | Certification Revocation List for Intermediate CA.             |
| /root/ca/pfx         | Exported, encrypted pkcs#12 pfx files for client distribution. |

Initial Setup
-------------
Setup the basic structure required to operate your own CA to enforce client
authentication and revocation lists.

```bash
mkdir -p /root/ca/root/{certs,crl,newcerts,private} /root/ca/inter/{certs,crl,csr,newcerts,private} /root/ca/pfx
chmod 0700 /root/ca/{root,inter}/private
touch /root/ca/{root,inter}/index.txt
echo 1000 | tee /root/ca/root/serial /root/ca/inter/serial
echo 'unique_subject = no' | tee /root/ca/root/index.txt.attr /root/ca/inter/index.txt.attr
echo 1000 > /root/ca/inter/crlnumber
```
* Assumes all CA data will be stored in `/root/`

[Setup Root CA][c7]
-------------------
The root CA should **never** be used other than to create or revoke intermediate
CAs. It should always be kept offline and secured once intermediate CAs are
setup. A compromise of the root CA key will compromise **all** child
certificates.

### Create Root CA Openssl Configuration
A good [default][c8] is here. This configuration should only contain relevant
sections for the required Root CA actions. Configuration file _must_ be
specified when issuing Root CA operations otherwise the systemwide
`openssl.conf` default configuration will be used.

/root/ca/root/root.ca `root:root 0600`
```openssl
# OpenSSL root CA configuration file.
# Stripped down to just Root CA functionality.
# https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html

[ ca ]
default_ca = CA_default

[ CA_default ]
# Directory and file locations.
dir               = /root/ca/root
certs             = $dir/certs
crl_dir           = $dir/crl
new_certs_dir     = $dir/newcerts
database          = $dir/index.txt
serial            = $dir/serial
RANDFILE          = $dir/private/.rand

# The root key and root certificate.
private_key       = $dir/private/root.key.pem
certificate       = $dir/certs/root.cert.pem

# For certificate revocation lists.
crlnumber         = $dir/crlnumber
crl               = $dir/crl/root.crl.pem
crl_extensions    = crl_ext
default_crl_days  = 375

default_md        = sha512
name_opt          = ca_default
cert_opt          = ca_default
default_days      = 375
preserve          = no
policy            = policy_strict

[ policy_strict ]
# The root CA should only sign intermediate certificates that match.
countryName             = match
stateOrProvinceName     = match
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ req ]
# Applied when creating / signing certificates.
default_bits        = 4096
distinguished_name  = req_distinguished_name
string_mask         = utf8only
default_md          = sha512
x509_extensions     = v3_ca

[ req_distinguished_name ]
# CSR information required, prompts and defaults.
countryName                     = Country Name (2 letter code)
stateOrProvinceName             = State or Province Name
localityName                    = Locality Name
0.organizationName              = Organization Name
organizationalUnitName          = Organizational Unit Name
commonName                      = Common Name
emailAddress                    = Email Address

# Default values for certification generation.
countryName_default             = XX
stateOrProvinceName_default     = XX
localityName_default            = XX
0.organizationName_default      = {CA NAME}
organizationalUnitName_default  = {CA NAME} Certificate Authority
commonName_default              = {CA NAME} Root CA
emailAddress_default            = XX

[ v3_ca ]
# Root CA extenstions: man x509v3_config '-extensions v3_ca'
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ v3_intermediate_ca ]
# Intermediate CA extensions: man x509v3_config '-extensions v3_intermediate_ca'
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true, pathlen:0
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ crl_ext ]
# Certificate revocation list extensions: man x509v3_config
authorityKeyIdentifier=keyid:always

[ ocsp ]
# OCSP signing certificate extensions: man ocsp
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, digitalSignature
extendedKeyUsage = critical, OCSPSigning
```

### Create Root CA Private Key and Certificate
Should be done on an air-gapped machine and stored encrypted offline once the
intermediate CA is setup. Root CA should rarely be used.

Create the private key:
```bash
openssl genrsa -aes256 -out /root/ca/root/private/root.key.pem 4096
chmod 0400 /root/ca/root/private/root.key.pem
```

Create the Root CA Certficate:
```bash
openssl req -config /root/ca/root/root.ca -key /root/ca/root/private/root.key.pem -new -x509 -days 7300 -sha512 -extensions v3_ca -out /root/ca/root/certs/root.cert.pem
chmod 444 /root/ca/root/certs/root.cert.pem
openssl x509 -noout -text -in /root/ca/root/certs/root.cert.pem
```
* A long lifetime (7300 days, 20 years) for an offline Root CA is OK. When the
  Root CA expires, all child certificates become invalid.
* Defaults from root.ca will autofill CA certificate fields.

[Setup Intermediate CA][j2]
---------------------------
The Intermediate CA is the workhorse for certificate authorities. This will be
the main CA used for issuing and revoking server / client certificates.

### Create Intermediate CA Openssl Configuration
A good [default][j3] is here. This configuration should only contain relevant
sections for the required Intermediate CA actions. Configuration file _must_ be
specified when issuing Intermediate CA operations otherwise the systemwide
`openssl.conf` default configuration will be used.

/root/ca/inter/inter.ca `root:root 0600`
```openssl
# OpenSSL intermediate CA configuration file.
# Stripped down to just Intermediate CA functionality.
# https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html

[ ca ]
default_ca = CA_default

[ CA_default ]
# Directory and file locations.
dir               = /root/ca/inter
certs             = $dir/certs
crl_dir           = $dir/crl
new_certs_dir     = $dir/newcerts
database          = $dir/index.txt
serial            = $dir/serial
RANDFILE          = $dir/private/.rand

# The root key and root certificate.
private_key       = $dir/private/inter.key.pem
certificate       = $dir/certs/inter.cert.pem

# For certificate revocation lists.
crlnumber         = $dir/crlnumber
crl               = $dir/crl/inter.crl.pem
crl_extensions    = crl_ext
default_crl_days  = 375

default_md        = sha512
name_opt          = ca_default
cert_opt          = ca_default
default_days      = 375
preserve          = no
policy            = policy_loose

[ policy_loose ]
# Allow the intermediate CA to sign a more diverse range of certificates.
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ req ]
# Options for the 'openssl req' tool: man req
default_bits        = 4096
distinguished_name  = req_distinguished_name
string_mask         = utf8only
default_md          = sha512
x509_extensions     = v3_intermediate_ca

[ req_distinguished_name ]
# CSR information required, prompts and defaults.
countryName                     = Country Name (2 letter code)
stateOrProvinceName             = State or Province Name
localityName                    = Locality Name
0.organizationName              = Organization Name
organizationalUnitName          = Organizational Unit Name
commonName                      = Common Name
emailAddress                    = Email Address

# Default values for certification generation.
countryName_default             = XX
stateOrProvinceName_default     = XX
localityName_default            = XX
0.organizationName_default      = {CA NAME}
organizationalUnitName_default  = {CA NAME} Certificate Authority
commonName_default              = {CA NAME} Intermediate CA
emailAddress_default            = XX

[ user_cert ]
# User certificate extensions: man x509v3_config '-extensions user_cert'
basicConstraints = CA:FALSE
nsCertType = client, email
nsComment = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth, emailProtection

[ machine_cert ]
# Machine certificate extensions: man x509v3_config '-extensions machine_cert'
basicConstraints = CA:FALSE
nsCertType = client
nsComment = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth

[ server_cert ]
# Server certificate extensions: man x509v3_config '-extensions server_cert'
basicConstraints = CA:FALSE
nsCertType = server
nsComment = "OpenSSL Generated Server Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth

[ crl_ext ]
# Certificate revocation list extensions: man x509v3_config
authorityKeyIdentifier=keyid:always

[ ocsp ]
# Extension for OCSP signing certificates: man ocsp
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, digitalSignature
extendedKeyUsage = critical, OCSPSigning
```

### Create Intermediate CA Private Key and Certificate
Private key should be kept offline of live services, but accessible to enable
changes. Lifetimes for Intermediate CAs should be shorter than Root CAs.

Create the private key:
```bash
openssl genrsa -aes256 -out /root/ca/inter/private/inter.key.pem 4096
chmod 0400 /root/ca/inter/private/inter.key.pem
```

Create the Intermediate CA Certficate:
```bash
openssl req -config /root/ca/inter/inter.ca -new -sha512 -key /root/ca/inter/private/inter.key.pem -out /root/ca/inter/csr/inter.csr.pem
openssl ca -config /root/ca/root/root.ca -extensions v3_intermediate_ca -days 3650 -notext -mb sha512 -in /root/ca/inter/csr/inter.csr.pem -out /root/ca/inter/certs/inter.cert.pem
chmod 444 /root/ca/inter/certs/inter.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/inter.cert.pem
openssl verify -CAfile /root/ca/root/certs/root.cert.pem /root/ca/inter/certs/inter.cert.pem
```
* Defaults from inter.ca will autofill Intermediate CA certificate fields.
* The Root CA is used to sign the Intermediate CA. This creates a chain of
  trust.
* Lifetime is half (3650 days, 10 years) for an Intermediate CA. When the
  Intermediate CA expires, all child certificates become invalid.
* The `verify` command should return _OK_. This means that the Intermediate
  certificate is currently valid.

### Create Intermediate Chain of Trust
The chain of trust is used to validate all certificates up to the Root CA. This
is usually deployed with server/client certificates if the Root CA is not added
to each machine's Trusted CA store.

```bash
cat /root/ca/inter/certs/inter.cert.pem /root/ca/root/certs/root.cert.pem > /root/ca/inter/certs/ca-chain.cert.pem
chmod 444 /root/ca/inter/certs/ca-chain.cert.pem
```

[Server Certificates][kd]
-------------------------
Used for providing SSL connections with services / servers. The Root CA must be
in the trusted Root CAs or the ca-chain deployed with clients for servers
presenting these SSL connections to be validate (green lock). These certificates
only have `serverAuth` extensions added.

Letsencrypt certificates should be used here instead of self-signed certs.

### Create Server Private Key and Certificate

Create the private key and certificate signing request:
```bash
openssl genrsa -out /root/ca/inter/private/{SERVER}.key.pem 4096
chmod 0400 /root/ca/inter/private/{SERVER}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{SERVER}.key.pem -new -sha512 -out /root/ca/inter/csr/{SERVER}.csr.pem
```
* Country Name (2 letter code) [XX]:
* State or Province Name [XX]:
* Locality Name [XX]:
* Organization Name [{CA NAME}]:
* Organizational Unit Name [{CA NAME} Certificate Authority]: `{SERVER}`
* Common Name [{CA NAME} Intermediate CA]: `*.example.com`
* Email Address [XX]:

> :warning:  
> Requiring a password `-aes256` for the private key will require that password
> to be entered everytime the certifcate is used (e.g. service is started).
> Given the short lived nature of these certificates, generally no password is
> used and CRL/OSCP are used to invalidate any exposed certifiates.

Sign certificate signing request:
```bash
openssl ca -config /root/ca/inter/inter.ca -extensions server_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{SERVER}.csr.pem -out /root/ca/inter/certs/{SERVER}.cert.pem
chmod 444 /root/ca/inter/certs/{SERVER}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{SERVER}.cert.pem
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{SERVER}.cert.pem
```
* Server certificates should be much shorter lifetime that CA's. Typically a
  little over a year.
* The verify command should return `OK`.
* both `ca-chain.cert.pem` and `{SERVER}.cert.pem` need to be distributed if
  Root CA is not in the trusted CA store.

[Machine Certificates][kd]
--------------------------
Special type of client certificate used to validate a 'machine' hardware
identity. These are tied to a specific machine and only have `clientAuth`
extensions added.

### Create Machine Private Key and Certificate

Create the private key and certificate signing request:
```bash
openssl genrsa -out /root/ca/inter/private/{MACHINE}.key.pem 4096
chmod 0400 /root/ca/inter/private/{MACHINE}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{MACHINE}.key.pem -new -sha512 -out /root/ca/inter/csr/{MACHINE}.csr.pem
```
* Country Name (2 letter code) [XX]:
* State or Province Name [XX]:
* Locality Name [XX]:
* Organization Name [{CA NAME}]: `{MACHINE}`
* Organizational Unit Name [{CA NAME} Certificate Authority]: `machine`
* Common Name [{CA NAME} Intermediate CA]: `{MACHINE}.machine`
* Email Address [XX]:

> :warning:  
> Requiring a password `-aes256` for the private key will require that password
> to be entered everytime the certifcate is used (e.g. authenticating to a
> service). Given the short lived nature of these certificates and that it is
> providing a machine identity, generally no password is used and CRL/OSCP are
> used to invalidate any exposed certifiates to prevent access.

Sign certificate signing request:
```bash
openssl ca -config /root/ca/inter/inter.ca -extensions machine_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{MACHINE}.csr.pem -out /root/ca/inter/certs/{MACHINE}.cert.pem
chmod 444 /root/ca/inter/certs/{MACHINE}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{MACHINE}.cert.pem
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{MACHINE}.cert.pem
```
* Machine certificates should be much shorter lifetime that CA's. They should be
  revoked and re-created whenever a machine is new or re-installed.
* The verify command should return `OK`.
* both `ca-chain.cert.pem` and `{MACHINE}.cert.pem` need to be distributed if
  Root CA is not in the trusted CA store.

[Client Certificates][kd]
-------------------------
Client certificate to validate client identity. These are tied to a specific
user and only have `clientAuth`, `emailProtection` extensions added.

### Create Client Private Key and Certificate

Create the private key and certificate signing request:
```bash
openssl genrsa -aes256 -out /root/ca/inter/private/{USER EMAIL}.key.pem 4096
chmod 0400 /root/ca/inter/private/{USER EMAIL}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{USER EMAIL}.key.pem -new -sha512 -out /root/ca/inter/csr/{USER EMAIL}.csr.pem
```
* Country Name (2 letter code) [XX]:
* State or Province Name [XX]:
* Locality Name [XX]:
* Organization Name [{CA NAME}]: `{ORG OR CA NAME}`
* Organizational Unit Name [{CA NAME} Certificate Authority]: `{ORG OR CA NAME}`
* Common Name [{CA NAME} Intermediate CA]: `{USER NAME}`
* Email Address [XX]: `{USER EMAIL}`

> :warning:  
> This identifies a user and needs to contain enough information to identify
> that person. Certificate should also require a password to prevent identity
> impersonation.

Sign certificate signing request:
```bash
openssl ca -config /root/ca/inter/inter.ca -extensions user_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{USER EMAIL}.csr.pem -out /root/ca/inter/certs/{USER EMAIL}.cert.pem
chmod 444 /root/ca/inter/certs/{USER EMAIL}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{USER EMAIL}.cert.pem
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{USER EMAIL}.cert.pem
```
* Client certificates should be much shorter lifetime that CA's.
* Clients can create their own CSR requests to be signed, meaning that the CA
  never needs to see the client private key.
* The verify command should return `OK`.
* both `ca-chain.cert.pem` and `{USER EMAIL}.cert.pem` need to be distributed if
  Root CA is not in the trusted CA store.

Exporting Certificates
----------------------
PKCS #12 PFX (Personal Information Exchange Certificate) is an encrypted
singular file archive format used to distribute a bundle of certificates
securely to a client. This is used to securely distribute key/cert material to
clients.

Pack client certificates and private keys into pfx:
```bash
openssl pkcs12 -export -out /root/ca/pfx/{CLIENT}.pfx -inkey /root/ca/inter/private/{CLIENT}.key.pem -in /root/ca/inter/certs/{CLIENT}.cert.pem -certfile /root/ca/inter/certs/ca-chain.cert.pem
```
* Set a strong _export password_ different from and private key password used.
  Prevents bundle from being installed and used without knowing password.
* _ca-chain_ is included to provide chain of trust to the client using the
  certificate and validate the server.

[Certificate Revocation Lists][r4]
----------------------------------
Certificate Revocation Lists (CRLs) are used to invalidate certificates in the
wild which have been compromised. This covers server-side revocation
enforcement.

Create CRL:
```bash
openssl ca -config /root/ca/inter/inter.ca -gencrl -out /root/ca/inter/crl/inter.crl.pem
```

Check Current CRL Status:
```bash
openssl crl -in ca/inter/crl/inter.crl.pem -noout -text
```

### Revoking Certificate
This will prevent a compromised certificate (which is still valid) from being
used.

Revoke Certificate and Update CRL:
```bash
openssl ca -config /root/ca/inter/inter.ca -revoke /root/ca/inter/certs/{TARGET}.cert.pem
openssl ca -config /root/ca/inter/inter.ca -gencrl -out /root/ca/inter/crl/inter.crl.pem
```
* The new CRL needs to be deployed to any service using the Intermediate CA.
* This can also be applied at the Root CA level to revoke intermediate CA's.

[docker-service-template.md|c9067f2][XX]

[3k]: https://www.openssl.org/
[kx]: https://jamielinux.com/docs/openssl-certificate-authority/introduction.html
[c7]: https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html
[c8]: https://jamielinux.com/docs/openssl-certificate-authority/appendix/root-configuration-file.html
[j2]: https://jamielinux.com/docs/openssl-certificate-authority/create-the-intermediate-pair.html
[j3]: https://jamielinux.com/docs/openssl-certificate-authority/appendix/intermediate-configuration-file.html
[kd]: https://jamielinux.com/docs/openssl-certificate-authority/sign-server-and-client-certificates.html
[r4]: https://jamielinux.com/docs/openssl-certificate-authority/certificate-revocation-lists.html

[refss]: proxy-control.conf
[refew]: ..