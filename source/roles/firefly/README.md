# Firefly
Firefly installation from public release.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_firefly/blob/main/defaults/main/main.yml).

[defaults/config.yml](https://github.com/r-pufky/ansible_firefly/blob/main/defaults/main/config.yml).

## Dependencies
N/A

## Example Playbook
host_vars/firefly.example.com/vars/firefly.yml
``` yaml
firefly_version: 'latest'
firefly_delete_old_versions: true
firefly_link_storage: '/data'
firefly_proxy_hostname: 'firefly.pufky.com'
```

site.yml
``` yaml
- name:   'firefly server'
  hosts:  'firefly.example.com'
  become: true
  roles:
     - 'r_pufky.firefly'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_firefly/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
