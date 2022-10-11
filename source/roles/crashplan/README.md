# Crashplan
Crashplan installation from public release tarball.

## Requirements
Pre-existing crashplan.com account. Approximately 1GB of RAM per 1TB for
largest backup set.

## Role Variables
Settings have been throughly documented for usage, including version updates.

[defaults/main.yml](https://github.com/r-pufky/ansible_crashplan/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_crashplan/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
host_vars/crashplan.example.com/vars/crashplan.yml
``` yam
crashplan_memory: 6144
```

site.yml
``` yaml
- name:   'crashplan server'
  hosts:  'crashplan.example.com'
  become: true
  roles:
     - 'r_pufky.crashplan'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_crashplan/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
