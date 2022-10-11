# Unifi
Unifi installation from public release tarball.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_unifi/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_unifi/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
Default role setting will deploy a vanilla Unifi Controller instance.

site.yml
``` yaml
- name:   'unifi server'
  hosts:  'unifi.example.com'
  become: true
  roles:
     - 'r_pufky.unifi'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_unifi/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
