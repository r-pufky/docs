Let's Encrypt Setup
-------------------
Setting up a stand-alone signed SSL certificate for use on personal systems,
using Let's Encrypt.

Note: This is for personal use only, and doesn't account for specific
nation-state attacks, which could include MITM or a compromise of Let's
Encrypt servers or the ACME protocol. [Don't consider this secure][1]. It is
better than having people get used to accepting self-signed certificates,
and it enables use of verifed SSL for things like mail and web services.

1. [Ports Exposed](#ports-exposed)
3. [Important File Locations](#important-file-locations)
4. [Installing](#installing)
5. [Generate a Certificate](#generate-a-certificate)
6. [Renewing Certificates](#renewing-certificates)

Port Exposed
------------

| Port | Protocol | Purpose                                                                        |
|------|----------|--------------------------------------------------------------------------------|
| 443  | TCP      | External port ACME protocol verifies domain ownership with. Cannot be changed. |
| 4343 | TCP      | Internal port certbot listens on for ACME challenge/response.                  |

Important File Locations
------------------------
| File             | Purpose                                |
|------------------|----------------------------------------|
| /etc/letsencrypt | All certbot state and certs. root:root |

Installing
----------
certbot maintains [a PPA specifically for ubuntu][2], just use that. Certbot
documentation [is located here][3].

```bash
sudo apt update && sudo apt install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt update && sudo apt install certbot 
```

### Generate a certificate
We want to specify a specific port to use for the challenge so we don't have
to do any specifc changes for webservers. Also force https (tls-sni-01) and
generate a 4096bit RSA key instead of the default 2048bit key.
```bash
certbot certonly --standalone --preferred-challenges tls-sni --tls-sni-01-port 4343 --rsa-key-size 4096 --agree-tos --email **YOUR-EMAIL** --domains example.com,mail.example.com,example2.com,subdomain.example2.com
```
* Make sure port is set properly on router/firewall
* DNS-01 is a more secure method, but your DNS host must support it
* Without an email specified, if you lose your generated keys, the domain is
  effectively locked out
* Port 443 is still required to be forwarded to whatever port is set here, if
  your cert server is not publically facing.

Note: TLS-SNI-01 authenication has been disabled due to vulnerabilities with
shared hosting resources. See [here][4] and [here][5].

### Renewing Certificates
Renewing certificates will automatically refresh all current certificates up for
renewal unless you want to manually specify a domain to renew.

First test the renewal to make sure that you can reach the servers and they can
read your challenge responses. This will not count against your number of
renewal attempts, and will verify your configuration is good to go.

```bash
certbot renew --dry-run --tls-sni-01-port 4343
```

Renew your certificates.
```bash
certbot renew --tls-sni-01-port 4343
```
* All stipulations from generating a certificate apply here

[1]: https://www.reddit.com/r/PFSENSE/comments/4qwp8i/do_we_really_have_to_lock_every_thread_that/d4wuymx/?st=iwy5oece&sh=a2a3c939
[2]: https://certbot.eff.org/#ubuntuxenial-other
[3]: https://certbot.eff.org/all-instructions
[4]: https://community.letsencrypt.org/t/important-what-you-need-to-know-about-tls-sni-validation-issues/50811
[5]: https://community.letsencrypt.org/t/2018-01-11-update-regarding-acme-tls-sni-and-shared-hosting-infrastructure/50188
