# Roundcube
Roundcube installation from public release.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_roundcube/blob/main/defaults/main.yml).

## Dependencies
N/A

## Example Playbook
host_vars/roundcube.example.com/vars/roundcube.yml
``` yaml
roundcube_version: '1.5.0'
roundcube_delete_old_versions: true
roundcube_product_name: 'mail'
roundcube_username_domain: 'example.com'
roundcube_skin: 'larry'
roundcube_proxy_whitelist:
  - '10.5.5.254'
roundcube_ssl_enable: true
roundcube_ssl_fullchain: '/etc/ssl/certs/ssl-cert-snakeoil.pem'
roundcube_ssl_private: '/etc/ssl/private/ssl-cert-snakeoil.key'

roundcube_db_type:     'sqlite' # supports pgsql, mysql, sqlite; see defaults.

roundcube_imap_host: 'ssl://mail.example.com'
roundcube_smtp_server: 'tls://mail.example.com'
roundcube_des_key: '{{ vault_roundcube_des_key }}'
```

site.yml
``` yaml
- name:   'roundcube server'
  hosts:  'roundcube.example.com'
  become: true
  roles:
     - 'r_pufky.roundcube'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_roundcube/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
