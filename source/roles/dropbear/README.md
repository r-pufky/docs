# Dropbear
Dropbear installation from public release tarball.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_dropbear/blob/main/defaults/main.yml).

## Dependencies
N/A

## Example Playbook
host_vars/dropbear.example.com/vars/dropbear.yml
``` yaml
dropbear_private_key: '{{ vault_dropbear_private_key }}'
dropbear_public_key:  '{{ vault_dropbear_public_key }}'

# Dropbear host identification key. This is a special format, not a standard
# SSH keypair. Generate a host key, encrypt, store in ansible outside of
# {host,group}_vars:
#
#   dropbearkey -t rsa -s 4096 -f dropbear_rsa_host_key
#   ansible-vault encrypt dropbear/{HOST}_rsa_host_key
#
# NOTE: Dropbear host keys are binary files and cannot be stored encrypted in
#       the {host,group}_vars directory. Ansible will try to automtically
#       decrypt this file and fail due to UTF-8 encoding issues. Storing within
#       ansible but outside of {host,group}_vars to prevent decryption until
#       the binary file is copied, wherein the decryption happens correctly.
#
# ERROR! 'utf-8' codec can't encode characters in position 23-24: surrogates
#        not allowed
dropbear_rsa_host_key_file: 'dropbear/qnap_rsa_host_key'
```

site.yml
``` yaml
- name:   'dropbear'
  hosts:  'dropbear.example.com'
  become: true
  roles:
     - 'r_pufky.dropbear'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_dropbear/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
