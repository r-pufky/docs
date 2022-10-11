# Plex
Plex Media Server supporting plexpass entitlements.

## Requirements
No additional requirements. See [Clean Setup](#clean-setup) for new plex
installs.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_plex/blob/main/defaults/main/main.yml).

### Plex Preferences
If you do **not** have a pre-existing configuration: install without preferences
set and set those values after plex is configured.

Reasonable defaults have been provided but must be updated for your setup before
use.

Location: `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server`

Pull configured values from `Preferences.xml`.

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_plex/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
host_vars/plex.example.com/vars/plex.yml
``` yaml
plex_library: '/data/media'

ports:
  - {proto: 'tcp', from_ip: 'any', to_port: 32400, direction: 'in', comment: 'plex media server access'}

plex_machine_identifier:                '{{ vault_plex_machine_identifier }}'
plex_processed_machine_identifier:      '{{ vault_plex_processed_machine_identifier }}'
plex_accepted_eula:                     '1'
plex_online_mail:                       'example@example.com'
plex_online_token:                      '{{ vault_plex_online_token }}'
plex_online_username:                   'example'
plex_publish_server_on_plex_online_key: '1'
```

site.yml
``` yaml
- name:   'plex media server'
  hosts:  'plex.example.com'
  become: true
  roles:
     - 'r_pufky.plex'
```

## Clean Setup
A new plex install (or one requiring a new access token after revocation)
requires the initial manual setup process to be run locally. Use a SSH tunnel
to access the server-side configuration page.

``` bash
ssh -L 32400:localhost:32400 {plex_host}
```

Then connect to http://localhost:32400/web and run through the configuration
steps.

1. Select media libraries to use.
1. Sign-in on server (upper right --> sign-in)
1. Select server and claim (claim now --> claim server)
1. Once claimed, the access token and configured preferences are located in
   `Preferences.xml` per [Plex Preferences](#plex-preferences).

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_plex/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
