# DB
Manage Maria and Postgres DB's.

## Requirements
No additional requirements.

## Role Variables
Settings have been throughly documented for usage.

* [defaults/maria.yml](https://github.com/r-pufky/ansible_db/blob/main/defaults/main/maria.yml).
* [defaults/postgres.yml](https://github.com/r-pufky/ansible_db/blob/main/defaults/main/postgres.yml).
* [defaults/ports.yml](https://github.com/r-pufky/ansible_db/blob/main/defaults/main/ports.yml).

## Dependencies
None. Based on:

* https://github.com/geerlingguy/ansible-role-mysql
* https://github.com/geerlingguy/ansible-role-postgresql

With patches, postgres 13 support, bullseye support.

## Example Playbook

Maria (Mysql) Configuration
host_vars/db.example.com/vars/maria.yml
``` yaml
db_maria_root_home:     '/root'
db_maria_root_username: 'root'
db_maria_root_password: '{{ vault_db_maria_root_password }}'
db_maria_databases:
- name: 'digikam'
- name: 'firefly'

db_maria_users:
- name:     'digikam'
  host:     '%' # If recreated set to server host.
  password: '{{ vault_users_db_maria_digikam_password }}'
  priv:     'digikam.*:ALL'
- name:     'firefly'
  host:     '%' # If recreated set to server host.
  password: '{{ vault_users_db_maria_firefly_password }}'
  priv:     'firefly.*:ALL'
db_maria_mysqld_bind_address:          '*'
db_maria_mysqld_port:                  3306
```

Prostgres Configuration
host_vars/db.example.com/vars/postgres.yml
``` yaml
db_postgres_version:     '13'
db_postgres_data_dir:    '/var/lib/postgresql/{{ db_postgres_version }}/main'
db_postgres_backup_dir:  '/var/lib/postgresql-backup'
db_postgres_bin_path:    '/usr/lib/postgresql/{{ db_postgres_version }}/bin'
db_postgres_config_path: '/etc/postgresql/{{ db_postgres_version }}/main'
db_postgres_packages:
  - 'postgresql-{{ db_postgres_version }}'

db_postgres_databases:
  - name:  'gitea'
    owner: 'gitea'
  - name:  'roundcube'
    owner: 'roundcube'

db_postgres_users:
  - name:     'gitea'
    password: '{{ vault_users_db_postgres_gitea_password }}'
    priv:     'all'
    db:       'gitea'
  - name:     'roundcube'
    password: '{{ vault_users_db_postgres_roundcube_password }}'
    priv:     'all'
    db:       'roundcube'

db_postgres_ssl:          'off'
db_postgres_connections_authentication_extensions: |
  listen_addresses = '*'
  superuser_reserved_connections = 1
db_postgres_log_timezone: 'America/Los_Angeles'
db_postgres_timezone:     'America/Los_Angeles'
db_postgres_lc_messages:  'en_US.utf8'
db_postgres_lc_monetary:  'en_US.utf8'
db_postgres_lc_numeric:   'en_US.utf8'
db_postgres_lc_time:      'en_US.utf8'

db_postgres_hba:
  - {type: 'host',  database: 'sameuser', user: 'gitea',     address: 'samenet',      method: '{{ db_postgres_auth_method }}'}
  - {type: 'host',  database: 'sameuser', user: 'roundcube', address: 'samenet',      method: '{{ db_postgres_auth_method }}'}
  - {type: 'local', database: 'all',      user: 'postgres',  address: '',             method: 'peer'}
  - {type: 'local', database: 'all',      user: 'all',       address: '',             method: 'peer'}
  - {type: 'host',  database: 'all',      user: 'all',       address: '127.0.0.1/32', method: '{{ db_postgres_auth_method }}'}
  - {type: 'host',  database: 'all',      user: 'all',       address: '::1/128',      method: '{{ db_postgres_auth_method }}'}
```

site.yml
``` yaml
- name:   'db server'
  hosts:  'db.example.com'
  become: true
  roles:
     - 'r_pufky.db/postgres'
     - 'r_pufky.db/maria'
```

## Issues
Create a bug and provide as much information as possible.

Associate pull requests with a submitted bug.

## License
[AGPL-3.0 License](https://github.com/r-pufky/ansible_db/blob/main/LICENSE)

## Author Information
https://keybase.io/rpufky
