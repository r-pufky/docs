Let's Encrypt Setup
-------------------
Setting up a stand-alone signed SSL certificate for use on personal systems,
using Let's Encrypt.

Note: **TLS-SNI-01 authenication has been disabled due to vulnerabilities with
shared hosting resources. See [here][4] and [here][5]**. You now must use ports
80 and 443.

This is for personal use only, and doesn't account for specific
nation-state attacks, which could include MITM or a compromise of Let's
Encrypt servers or the ACME protocol. [Don't consider this secure][1]. It is
better than having people get used to accepting self-signed certificates,
and it enables use of verifed SSL for things like mail and web services.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Installing](#installing)
1. [Generate a Certificate](#generate-a-certificate)
1. [Renewing Certificates](#renewing-certificates)
1. [Wildcard Certificates](#wildcard-certificates)
1. [Migrating from tls-sni-01 to nginx](#migrating-from-tls-sni-01-to-nginx)

Port Exposed
------------

| Port | Protocol | Purpose                                                          |
|------|----------|------------------------------------------------------------------|
| 443  | TCP      | ACME protocol verifies domain ownership with. Cannot be changed. |
| 80   | TCP      | Certbot listens ACME challenge/response.                         |

Important File Locations
------------------------
| File             | Purpose                                |
|------------------|----------------------------------------|
| /etc/letsencrypt | All certbot state and certs. root:root |

Installing
----------
Certbot documentation [is located here][3]. Install the auto-updating certbot,
which provides ACMEv2 enabling new features post `tls-sni-*` exploits.

Download [certbot-auto and verify][6]
```bash
wget -N https://dl.eff.org/certbot-auto.asc
gpg2 --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
wget https://dl.eff.org/certbot-auto
gpg2 --trusted-key 4D17C995CD9775F2 --verify certbot-auto.asc certbot-auto
chmod a+x ./certbot-auto
```

Install nginx for cert verification
```bash
apt install nginx
```

### Setup [nginx for domain validation][7]

/etc/nginx/conf.d
```nginx
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/html;
  server_name example.com www.example.com;
}
```

Verify syntax is ok and reload nginx:
```bash
nginx -t && nginx -s reload
```

## Generate a certificate
Using nginx validate a 4096bit key cert request for domains, using a given
email.

```bash
certbot --authenticator webroot --installer nginx --webroot-path /var/www/html --rsa-key-size 4096 --agree-tos --email **YOUR-EMAIL** --domains example.com,mail.example.com,example2.com,subdomain.example2.com
```
 * Make sure ports are set properly on router/firewall
 * [DNS-01 is][8] a more secure method, but your DNS host must support it
   (domains.google.com does not)
 * Without an email specified, if you lose your generated keys, the domain is
   effectively locked out

### Renewing Certificates
Renewing certificates will automatically refresh all current certificates up for
renewal unless you want to manually specify a domain to renew.

First test the renewal to make sure that you can reach the servers and they can
read your challenge responses. This will not count against your number of
renewal attempts, and will verify your configuration is good to go.

```bash
certbot renew --dry-run --authenticator webroot --installer nginx --webroot-path /var/www/html/
```

Renew your certificates.
```bash
certbot renew --authenticator webroot --installer nginx --webroot-path /var/www/html/
```
 * All stipulations from generating a certificate apply here


Wildcard Certificates
---------------------
Wildcard certificates were added recently and enable the easy use of multiple
sub-domains. This requires a [separate non-nginx setup][8] (ACME DNS-01) to
validate control of the DNS domains requested.

### DNS Pre-setup
The follow DNS records must be setup on the domain before requesting the certs.

| Name | Type  | TTL | DATA       |
|------|-------|-----|------------|
| @    | A     | 1h  | IP Address |
| *    | A     | 1h  | IP Address |
| www  | CNAME | 6h  | @          |
* www points to IP Address via @; this may be translated by your provider.
* both @ and * point to IP Address.

Request wildcard certs
```bash
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory --domains *.example.com,*.example2.com --manual --preferred-challenges dns-01 certonly
```
* There will be one request per host listed in domains, even if the same host,
  you only need to provide the wildcard; otherwise you will have to verify
  muiltple TXT records at once, which may not be supported by provider.
* Must update DNS TXT records with a hash to verify controls.
* This can be run from an existing letsencrypt/certbot setup with no changes
  (e.g. the nginx setup).

Migrating from tls-sni-01 to nginx
----------------------------------
Certs currently pulled with tls-sni-01 can be manully updated to enable nginx
validation. Once this is applied, no further changes are needed.

Follow [Setup nginx for domain validation](#setup-nginx-for-domain-validation).
When you get to renewal, follow these steps:

Add the following lines (replace with your information for domains).

/etc/letsencrypt/renewal/example.com.conf
```bash
installer = nginx
authenticator = webroot
pref_challs = http-01
webroot_path = /var/www/html
[[webroot_map]]
example.com = /var/www/html
mail.example.com = /var/www/html
example2.com = /var/www/html
subdomain.example2.com = /var/www/html
```

Comment out the following lines.
```bash
installer = None
authenticator = standalone
tls_sni_01_port = 4343
pref_challs = tls-sni-01
```
 * Keep this information until you confirm renewal works with the new setup.

Then force a renewal as specified in
[renewing certificates](#renewing-certificates).



[1]: https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939
[3]: https://certbot.eff.org/all-instructions
[4]: https://community.letsencrypt.org/t/important-what-you-need-to-know-about-tls-sni-validation-issues/50811
[5]: https://community.letsencrypt.org/t/2018-01-11-update-regarding-acme-tls-sni-and-shared-hosting-infrastructure/50188
[6]: https://certbot.eff.org/docs/install.html#certbot-auto
[7]: https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/
[7]: https://serverfault.com/questions/750902/how-to-use-lets-encrypt-dns-challenge-validation
[8]: https://medium.com/@utkarsh_verma/how-to-obtain-a-wildcard-ssl-certificate-from-lets-encrypt-and-setup-nginx-to-use-wildcard-cfb050c8b33f