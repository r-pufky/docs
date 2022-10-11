# Nzbget
Nzbget installation from public release binary.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_nzbget/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_nzbget/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
host_vars/nzbget.example.com/vars/nzbget.yml
``` yaml
nzbget_main_dir: '/data/nzbget'
nzbget_news_servers:
  - id: 1
    active:      'yes'
    name:        ''
    level:       0
    optional:    'no'
    group:       0
    srv_host:    'my.newsserver.com'
    srv_port:    119
    username:    '{{ vault_nzbget_news_user }}'
    password:    '{{ vault_nzbget_news_pass }}'
    join_group:  'no'
    encryption:  'no'
    cipher:      ''
    connections: 4
    retention:   0
    ip_version:  'auto'
    notes:       ''

nzbget_control_username: '{{ vault_nzbget_user }}'
nzbget_control_password: '{{ vault_nzbget_pass }}'
```

site.yml
``` yaml
- name:   'nzbget server'
  hosts:  'nzbget.example.com'
  become: true
  roles:
     - 'r_pufky.nzbget'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_nzbget/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
