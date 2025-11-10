# Certificates

## Server Certificates
Used for providing SSL connections with services / servers. The Root CA must be
in the trusted Root CAs or the ca-chain deployed with clients for servers
presenting SSL connections using these certificates to be validated (green
lock). These certificates only have **serverAuth** extensions added.

Let's encrypt certificates should be used here instead of self-signed certs.

!!! warning
    Requiring a password **-aes256** for the private key will require that
    password to be entered every time the certificate is used (e.g. service is
    started). Given the short lived nature of these certificates, generally no
    password is used and CRL/OSCP are used to invalidate any exposed
    certificates.

### Create Server Private Key and Certificate Signing Request
``` bash
openssl genrsa -out /root/ca/inter/private/{SERVER}.key.pem 4096
chmod 0400 /root/ca/inter/private/{SERVER}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{SERVER}.key.pem -new -sha512 -out /root/ca/inter/csr/{SERVER}.csr.pem
> Country Name (2 letter code): [XX]
> State or Province Name: [XX]
> Locality Name: [XX]
> Organization Name: [{CA NAME}]
> Organizational Unit Name: [{CA NAME} Certificate Authority]
> Common Name: [{CA NAME} Intermediate CA], *.example.com
> Email Address: [XX]
```

### Sign Certificate Signing Request
Server certificates should be much shorter lifetime that CA's. Typically a
little over a year. Both **ca-chain.cert.pem** and **{SERVER}.cert.pem** need
to be distributed if Root CA is not in the trusted CA store.

``` bash
openssl ca -config /root/ca/inter/inter.ca -extensions server_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{SERVER}.csr.pem -out /root/ca/inter/certs/{SERVER}.cert.pem
chmod 444 /root/ca/inter/certs/{SERVER}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{SERVER}.cert.pem
# Should return 'OK'.
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{SERVER}.cert.pem
```

## Machine Certificates
Special type of client certificate used to validate a machine hardware
identity. These are tied to a specific machine and only have **clientAuth**
extensions added.

!!! warning
    Requiring a password **-aes256** for the private key will require that
    password to be entered every time the certificate is used (e.g.
    authenticating to a service). Given the short lived nature of these
    certificates and that it is providing a machine identity, generally no
    password is used and CRL/OSCP are used to invalidate any exposed
    certificates to prevent access.

### Create Machine Private Key and Certificate
``` bash
openssl genrsa -out /root/ca/inter/private/{MACHINE}.key.pem 4096
chmod 0400 /root/ca/inter/private/{MACHINE}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{MACHINE}.key.pem -new -sha512 -out /root/ca/inter/csr/{MACHINE}.csr.pem
> Country Name (2 letter code): [XX]
> State or Province Name: [XX]
> Locality Name: [XX]
> Organization Name: [{CA NAME}], {MACHINE}
> Organizational Unit Name: [{CA NAME} Certificate Authority], machine
> Common Name: [{CA NAME} Intermediate CA], {MACHINE}.machine
> Email Address: [XX]
```

### Sign certificate signing request
Machine certificates should be much shorter lifetime that CA's. They should be
revoked and re-created whenever a machine is new or re-installed. Both
**ca-chain.cert.pem** and **{MACHINE}.cert.pem** need to be distributed if Root
CA is not in the trusted CA store.

``` bash
openssl ca -config /root/ca/inter/inter.ca -extensions machine_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{MACHINE}.csr.pem -out /root/ca/inter/certs/{MACHINE}.cert.pem
chmod 444 /root/ca/inter/certs/{MACHINE}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{MACHINE}.cert.pem
# Should return 'OK'.
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{MACHINE}.cert.pem
```

## Client Certificates
Client certificate to validate client identity. These are tied to a specific
user and only have **clientAuth** and **emailProtection** extensions added.

!!! warning
    This identifies a user and needs to contain enough information to identify
    that person. Certificate should also require a password to prevent identity
    impersonation.

### Create Client Private Key and Certificate Signing Request
``` bash
openssl genrsa -aes256 -out /root/ca/inter/private/{USER EMAIL}.key.pem 4096
chmod 0400 /root/ca/inter/private/{USER EMAIL}.key.pem
openssl req -config /root/ca/inter/inter.ca -key /root/ca/inter/private/{USER EMAIL}.key.pem -new -sha512 -out /root/ca/inter/csr/{USER EMAIL}.csr.pem
> Country Name (2 letter code): [XX]
> State or Province Name: [XX]
> Locality Name: [XX]
> Organization Name: [{CA NAME}], {ORG OR CA NAME}
> Organizational Unit Name: [{CA NAME} Certificate Authority], {ORG OR CA NAME}
> Common Name: [{CA NAME} Intermediate CA], {USER}
> Email Address: [XX], {EMAIL}
```

### Sign certificate signing request
Client certificates should be much shorter lifetime that CA's. Clients can
create their own CSR requests to be signed, meaning that the CA never needs to
see the client private key. Both **ca-chain.cert.pem** and
**{USER EMAIL}.cert.pem** need to be distributed if Root CA is not in the
trusted CA store.

``` bash
openssl ca -config /root/ca/inter/inter.ca -extensions user_cert -days 375 -notext -md sha512 -in /root/ca/inter/csr/{USER EMAIL}.csr.pem -out /root/ca/inter/certs/{USER EMAIL}.cert.pem
chmod 444 /root/ca/inter/certs/{USER EMAIL}.cert.pem
openssl x509 -noout -text -in /root/ca/inter/certs/{USER EMAIL}.cert.pem
# Should return 'OK'.
openssl verify -CAfile /root/ca/inter/certs/ca-chain.cert.pem /root/ca/inter/certs/{USER EMAIL}.cert.pem
```

See [Cert Based Authentication](../nginx/manual/cert_based_authentication.md)
to setup auto selection of client certificate for matched sites.

## Exporting Certificates
PKCS #12 PFX (Personal Information Exchange Certificate) is an encrypted
singular file archive format used to distribute a bundle of certificates
securely to a client. This is used to securely distribute key/cert material to
clients.

### Pack client certificates and private keys into PFX
``` bash
openssl pkcs12 -export -out /root/ca/pfx/{CLIENT}.pfx -inkey /root/ca/inter/private/{CLIENT}.key.pem -in /root/ca/inter/certs/{CLIENT}.cert.pem -certfile /root/ca/inter/certs/ca-chain.cert.pem
```

* Set a **strong export** password **different** from and private key password
  to prevent bundle from being installed and used without knowing password.
* **ca-chain** is included to provide chain of trust to the client using the
  certificate and validate the server.

See [Cert Based Authentication](../nginx/manual/cert_based_authentication.md)
to setup auto selection of client certificate for matched sites.

### Extract Public/Private Keys from PFX
Keys can be extracted from the PFX file for use if needed.

``` bash
# Extract RSA private key.
openssl pkcs12 -in {CLIENT}.pfx -nocerts -nodes | openssl rsa -out rsa.key

# Extract RSA public key.
openssl pkcs12 -in {CLIENT}.pfx -clcerts -nokeys | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > rsa.pub
```

## Reference

* https://jamielinux.com/docs/openssl-certificate-authority/sign-server-and-client-certificates.html
