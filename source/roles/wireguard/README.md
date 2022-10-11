# Wireguard
Wireguard installation with wireguard-initramfs support.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

[defaults/main.yml](https://github.com/r-pufky/ansible_wireguard/blob/main/defaults/main/main.yml).

[defaults/adapter.yml](https://github.com/r-pufky/ansible_wireguard/blob/main/defaults/main/adapter.yml).

[defaults/initramfs.yml](https://github.com/r-pufky/ansible_wireguard/blob/main/defaults/main/initramfs.yml).

### Ports
All ports and protocols have been defined for the role.

Hosts should only define firewall rules for ports they need.

[defaults/ports.yml](https://github.com/r-pufky/ansible_wireguard/blob/main/defaults/main/ports.yml).

## Dependencies
N/A

## Example Playbook
Store wireguard vault material in group_vars for client/server access.

### With wireguard-initramfs
host_vars/client.example.com/vars/wireguard.yml
``` yaml
wireguard_initramfs_enable: true
wireguard_boot_interface:             'client'
wireguard_boot_interface_address:     '172.31.255.11/32'
wireguard_boot_peer_public_key:       '{{ vault_wireguard_server_public_key }}'
wireguard_boot_peer_endpoint:         'wireguard-server.example.com:51820'
wireguard_boot_client_private_key:    '{{ vault_wireguard_client_boot_private_key }}'
wireguard_boot_persistent_keepalives: '25'
wireguard_boot_allowed_ips:           '172.31.255.254/32'
wireguard_adapter_config:
  - {adapter: 'client',
     interface: {
       Address: '172.31.255.10/32',
       SaveConfig: 'False',
       PrivateKey: '{{ vault_wireguard_client_private_key }}',
     },
     peers: [
       {
         PublicKey: '{{ vault_wireguard_server_public_key }}',
         AllowedIPs: '172.31.255.254/32,172.31.255.5/32',
         EndPoint: 'wireguard-server.example.com:51820',
         PersistentKeepalive: 25
       },
     ]
    }
```

### Without wireguard-initramfs
host_vars/client.example.com/vars/wireguard.yml
``` yaml
wireguard_initramfs_enable: true
wireguard_adapter_config:
  - {adapter: 'tunnel',
     interface: {
       Address: '172.31.255.10/32',
       SaveConfig: 'False',
       PrivateKey: '{{ vault_wireguard_client_private_key }}',
     },
     peers: [
       {
         PublicKey: '{{ vault_wireguard_server_public_key }}',
         AllowedIPs: '172.31.255.254/32,172.31.255.5/32',
         EndPoint: 'wireguard-server.example.com:51820',
         PersistentKeepalive: 25
       },
     ]
    }
```

host_vars/wireguard-server.example.com/vars/wireguard.yml
``` yaml
wireguard_adapter_config:
  - {adapter: 'tunnel',
     interface: {
       Address: '172.31.255.5/32',
       SaveConfig: 'False',
       PrivateKey: '{{ vault_wireguard_server_private_key }}',
     },
     peers: [
       {
         PublicKey: '{{ vault_wireguard_client_public_key }}',
         AllowedIPs: '172.31.255.254/32,172.31.255.10/32',
         EndPoint: '10.9.9.251:51820',
         PersistentKeepalive: 25
       },
     ]
    }
```

site.yml
``` yaml
- name:   'wireguard server'
  hosts:  'wireguard-server.example.com'
  become: true
  roles:
     - 'r_pufky.wireguard'

- name:   'wireguard client'
  hosts:  'client.example.com'
  become: true
  roles:
     - 'r_pufky.wireguard'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_wireguard/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
