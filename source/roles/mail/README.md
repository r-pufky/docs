# Mail
A secure-by-default, principled, fullstack mailserver focusing on minimizing
required configuration options while providing high-domain reputation.

Configures Mail:
* Amavis
* Clamav
* Dovecot
* OpenDKIM
* OpenDMARC
* Pflogsumm
* Policyd-SPF
* Postfix
* Postgrey
* Postsrsd
* Postwhite
* Pyzor
* Razor

## Requirements
Audience is a user who simply wants to turnup a self-hosted, secure-by-default,
high-domain reputation non-docker mailserver with minimal fuss.

This does not intend to be a 'one role fits all' mail server solution. If you
need more complex setups (ldap, db, kerberos, etc), or are a business/company;
you are not the intended audience. Please fork (or make an offer :D).

DNS control is needed to setup correct DNS records. Configuration of these
options are guided during role deployment if the option is enabled.

Feedback is appreciated. Please submit feedback and bugs to issues.

Hardware Requirements:
* OS:   Debian 11 Bullseye
* RAM:  4GB
* CPU:  4 Threads (2 cores, 4 threads or 4 cores)
* Disk: 4GB Disk (+mail space)

Intended to be used with a total mail load below:
* ~ <30 mails per second
* ~ 500k mails/day

## Role Variables
Minimum Configuration.
  Defaults will work for a majority of users out of box. Settings have been
  throughly documented for usage.

The first domain listed is considered the primary domain, the first user
listed is considered the mail admin (receives postmaster@, abuse@, and
reports).

```yaml
mail_domains:
  - 'example.com'
  - 'example1.com'

mail_users:
  - {user: 'admin@example.com', pass: '{{ vault_user_admin_pass }}'}
  - {user: 'user@example1.com', pass: '{{ vault_user_pass }}'}
```

SSL Certificates must exist.

[defaults/main.yml](https://github.com/r-pufky/ansible_mail/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_mail/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
Apply additional roles to support configuration needs as wanted. In this
example we configure the base debian system, configure certificates, apply this
mail role, and finally configure a firewall and fail2ban.

See defaults/main/ports.yml for a complete definition of ports used in this
role ready for firewall application.

host_vars/mail.example.com/vars/mail.yml
```yaml
mail_domains:
  - 'example.com'
  - 'example1.com'

mail_users:
  - {user: 'admin@example.com', pass: '{{ vault_user_admin_pass }}'}
  - {user: 'user@example1.com', pass: '{{ vault_user_pass }}'}
```

site.yaml
```yaml
- hosts: mail.example.com
  roles:
    - {debian-base-role}
    - {letsencrypt-cert-management-role}
    - mail
    - {firewall-role}
    - {fail2ban-role}
```

## Principals
Users just want mail.
  They don't want 3,000 options to fit all possible configurations, nor care
  about configuration minutiae. KISS/DRY principals apply for user settings.

Focus on a single task.
  Focus solely on secure mail delivery. Areas outside of mail delivery, such as
  certificate management, firewall configuration, and IP blocking should be
  left to tools which do those tasks better.

Tell the user what to do.
  Automate complexity. Users should not need to read RFC's, multiple tutorials,
  and sourceforge questions to configure required DNS settings for secure,
  high-domain reputation mail, such as SPF, DMARC, DKIM. Pick reasonable,
  secure defaults using user settings and explicitly guide them on what needs
  to be set outside of the mail server.

Document decisions.
  Users should be able to look at the code in the future and understand why
  decisions were made. Even 'trivial' decisions are lost without context after
  multiple years. Developers must document design decisions either in the task
  name or comments explaining the reasoning behind decisions.

Trust but verify.
  Users shoud not need to debug a configuration. Validate configuration within
  reason using tools to ensure mail configuration is correct.

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_mail/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
