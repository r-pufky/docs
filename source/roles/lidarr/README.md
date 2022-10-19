# Lidarr
Lidarr installation from public release tarball.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_lidarr/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_lidarr/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
host_vars/lidarr.example.com/vars/lidarr.yml
``` yaml
lidarr_api_key:              '{{ vault_lidarr_api_key }}'
lidarr_update_automatically: true
lidarr_port:                 '8989'
```

site.yml
``` yaml
- name:   'lidarr server'
  hosts:  'lidarr.example.com'
  become: true
  roles:
     - 'r_pufky.lidarr'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_lidarr/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
