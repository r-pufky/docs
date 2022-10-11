# Pi-Hole
Pi-Hole installation from public release.

## Requirements
Pi-Hole hosts should be configured with static IP's per Pi-Hole documentation.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_pihole/blob/main/defaults/main/main.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_pihole/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
For multiple Pi-Hole nodes apply configuration in group_vars and node specific
settings in host_vars. Singleton instances can be applied in host_vars.

group_vars/pihole/vars/pihole.yml
``` yaml
pihole_webpassword: '{{ vault_pihole_webpassword }}'
pihole_api_key:     '{{ vault_pihole_api_key }}'

pihole_ad_sources:
  - id: 2
    address: 'https://adaway.org/hosts.txt'
    enabled: true
    comment: 'ansible adlist'
  - id: 3
    address: 'https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt'
    enabled: true
    comment: 'ansible adlist'

pihole_domain_blocklists:
  - id: 1
    type: 1
    domain: 'choice.microsoft.com'
    enabled: true
    comment: 'ansible blacklist'
  - id: 2
    type: 1
    domain: 'events.gfe.nvidia.com'
    enabled: true
    comment: 'ansible blacklist'
```

host_vars/pihole.example.com/vars/pihole.yml
``` yaml
pihole_pihole_interface: 'eth0'
pihole_ipv4_address:     '10.9.9.2/24'
pihole_ipv6_address:     ''
pihole_pihole_dns_1:     '10.9.9.1#53'
pihole_pihole_dns_2:     ''
```

host_vars/pihole2.example.com/vars/pihole.yml
``` yaml
pihole_pihole_interface: 'eth0'
pihole_ipv4_address:     '10.9.9.3/24'
pihole_ipv6_address:     ''
pihole_pihole_dns_1:     '10.9.9.1#53'
pihole_pihole_dns_2:     ''
```

site.yml
``` yaml
- name:   'pihole servers'
  hosts:  'pihole'
  become: true
  roles:
     - 'r_pufky.pihole'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_pihole/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
