# Deluge
Deluge installation from public release tarball.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_deluge/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_deluge/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
host_vars/deluge.example.com/vars/deluge.yml
``` yaml
deluge_web_first_login: false
deluge_web_pwd_salt:    '{{ vault_deluge_web_pwd_salt }}'
deluge_web_pwd_sha1:    '{{ vault_deluge_web_pwd_sha1 }}'
deluge_web_port:        8112
```

site.yml
``` yaml
- name:   'deluge server'
  hosts:  'deluge.example.com'
  become: true
  roles:
     - 'r_pufky.deluge'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_deluge/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
