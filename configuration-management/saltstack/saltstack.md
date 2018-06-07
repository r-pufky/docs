SaltStack Setup
-------------------
Configuration management for Linux, Windows, OSX.

Salt encrypts data communications, as well as providing only minion data needed
to minions. Supports GPG encryption of sensitive data out of the box, no special
services required.

1. [Requirements](#requirements)
2. [Ports Exposed](#ports-exposed)
3. [Important File Locations](#important-file-locations)
4. [Service Setup](#service-setup)
5. [Salt-Master Setup](#salt-master-setup)
6. [Managing States](#managing-states)
7. [Using Pillar](#using-pillar)
   * [Setup GPG](#setup-gpg)
     * [GPG encrypting shadow passwords](#gpg-encrypting-shadow-passwords)
8. [Installing Formulae](#installing-formulae)
9. [Setup Minions](#setup-minions)
10. [Signing Cert Requests](#signing-cert-requests)
11. [Revoking Certs](#revoking-certs)
12. [Master Frequent Commands](#master-frequent-commands)
12. [Manually Running Minions](#manually-running-minions)
13. [Development References](#development-references)


[Requirements][1]
-----------------
There are no specific requirements for Salt Open Source. [Enterprise
requirements are defined here][1]. Most users report actual usage minimum
requirements as:

| < 500      | > 500      |
|------------|------------|
| RAM: 2GB   | RAM: 4GB   |
| CPU: 1     | CPU: 4     |
| DISK: 20GB | DISK: 20GB |


[Ports Exposed][2]
------------------

| Port | Protocol | Purpose                                         |
|------|----------|-------------------------------------------------|
| 4505 | TCP      | Minion listen port for pubsub messages.         |
| 4506 | TCP      | Master file/data push, Minion push result data. |

By default `salt` should resolve, although this can be configured in the minion
as a DNS name or IP address.


Important File Locations
------------------------

| File                                                            | Purpose                                                                                                           |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| /var/log/salt/master  | Master logging/error messages. Useful for debugging module errors. When setup with encryption and no-minion reporting, errors will appear here for minions. |
| /var/log/salt/minion  | Minion logging/error messages. Less useful if using encrpytion (check server)                                                                               |
| /etc/salt             | Salt configuration, both master and minion                                                                                                                  |
| /etc/salt/gpgkeys     | Master private GPG keys for decrypting data. Hard coded.                                                                                                    |
| /srv/salt             | Master file directory for hosting files, forumlae and data.                                                                                                 |
| /etc/salt/pki/minions | Keyfile data for minions. Deleted minions should be automatically removed.                                                                                  |

[Service Setup][3]
------------------
Salt can run on both Python 2 and 3. This install prefers Python 3. See [Best
Practices][7]

/etc/apt/sources.list.d/saltstack.list
```bash
deb http://repo.saltstack.com/py3/ubuntu/16.04/amd64/latest xenial main
```

Add the salt repository signing key
```
wget -O - https://repo.saltstack.com/py3/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
```

Install salt. A minion can be installed on the master as well to have the master
manage itself.
```bash
sudo apt update && sudo apt install salt-master
```

### [Use TLS for protocol encryption][6]
Communication is automatically encrypted, but TCP is not. Force TLS encryption.

```bash
mkdir -p /etc/salt/pki/certs && cd /etc/salt/pki/certs
openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out salt.crt -keyout salt.key
chmod 0400 salt.key
```

### [Non-root User][6]
By default salt-master runs as root. Nothing the master does requires root.

Create `salt` user for master and set permissions.
```bash
adduser --shell /bin/bash --no-create-home --disabled-password --disabled-login salt
chown -R salt:salt /etc/salt /var/cache/salt /var/log/salt /var/run/salt /srv/salt
systemctl restart salt-master
```
* verify any custom directories are modified as well.

salt-master does require a shell, to run commands such as `salt-run`

Minions require root to properly install software, update apt and execute
commands.


[Salt-Master Setup][4]
----------------------
Changes can be made in `/etc/salt/master`, however making changes in
`/etc/salt/master.d/` is preferred to clarify server changes, as well as
enabling easy management on the config. Any file with `.conf` will be loaded.

### File Roots
/etc/salt/master.d/file.conf
```saltstack
file_roots:
  base:
    - /srv/salt/env/base
  dev:
    - /srv/salt/env/dev
    - /srv/salt/env/formulae/<formulae1>
    - /srv/salt/env/formulae/<formulae2>
  prod:
    - /srv/salt/env/prod
    - /srv/salt/env/formulae/<formulae1>
    - /srv/salt/env/formulae/<formulae2>
top_file_merging_strategy: same
default_top: dev
hash_type: sha512
```
This will create three branches, layering the single `formulae/<dir>` directory on
those environments for shared formulas. Base is applied to all environments and
is unused in this config.

Formula's can be directly checked out from a revision system (like git) into
/formulae. Once added to file roots, this can be directly accessed in these
environments with no additional changes.

### [Pillar Roots][9]
/etc/sale/master.d/pillar.conf
```saltstack
pillar_roots:
  dev:
    - /srv/salt/pillar/dev
  prod:
    - /srv/salt/pillar/prod
pillar_save_render_error: True
pillarenv_from_saltenv: True
pillar_raise_on_missing: True
```
Pillar defines the client data sent to minions, and acts as an ACL to who gets
access to that data. This setups two data environments, forces errors to halt
a formula application, and prevents error messages on minions (reported on
server). This prevents leaking potentially sensitive data users shouldn't have
access to if a formula fails.

### Primary Configuration
/etc/salt/master.d/primary.conf
```saltstack
user: salt
verify_env: True
enable_gpu_grains: True
ping_on_rotate: True
allow_minion_key_revoke: False
```
Primary configuration for salt-master. This forces the master to run as `salt`,
ensures the master is validated before started (perms, etc), pings minions on
AES key rotation and prevents minions from unmanaging themselves. See
[non-root user](#non-root-user) for setup instructions.

### Security
/etc/salt/master.d/security.conf
```saltstack
keysize: 4096
autosign_timeout: 0
sign_pub_messages: True
require_minion_sign_messages: True
drop_messages_signature_fail: False
ssl:
  keyfile: /etc/salt/pki/certs/salt.key
  certfile: /etc/salt/pki/certs/salt.crt
  ssl_version: PROTOCOL_TLSv1_2
```
Security configuration. Required 4096bit keys for signing. All messages are
signed. All minions added require manaul approval. Use SSL/TLS1.2 for protcol
encryption. See [TLS setup](#use-tls-for-protocol-encryption) for cert
creation.

`drop_messages_signature_fail` is False, as this requires those minions to have
verifiable signing certs, which self-signed certs cannot provide. Otherwise this
option will drop any message that does not verify.

### State
/etc/salt/master.d/state.conf
```saltstack
failhard: True
```
State applicatin to minions. Minions will immediately fail is there is an error,
instead of continuing to apply state.


[Managing States][12]
---------------------
States apply specific configurations to minions. See [State Reference][13].

Any `.sls` file in the [File Roots](#file-roots) will be evaluated as a SaLt
State file. Subdirectories can be referenced as packages if there is an
`init.sls` file (this will be accessed via the dir name). Directories do not
require `.sls` files for traversal.

These can be directly applied on CLI as

```bash
salt '*' state.sls <state_file_name>
```

Any state files may be referenced in other state files, using dotted access
notation from that environments root to access them.

```bash
ls -1 /srv/salt/env/prod/other/app/
init.sls
```

/srv/salt/env/prod/top.sls
```saltstack
prod:
  'my_host';
    - other.app
```

#### Install a package

```saltstack
apache2:
  pkg:
    - installed
```

#### Set a file with contents from server

```bash
ls -1 /srv/salt/env/prod/config
.bashrc
```

/srv/salt/env/prod/top.sls
```bash
prod:
  /root/.bashrc
    file.managed:
      - user: root
      - group: root
      - mode: 0600
      - source: salt://bachrc/bashrc
```


[Using Pillar][8]
-----------------
Pillar manages client data sent to minions; it also can handle GPG encrypted
blocks and only decrypt those blocks for minions who have access. This also
enables you to store your configuration in a repository without worrying about
leaking secrets. See [Pillar Roots](#pillar-roots) for master pillar directory
setup.

### Pillar top.sls
These specify minion matching to determine what environment a minion gets data
for. These should be matched to the structure in [File Roots](#file-roots).
`top.sls` files must exist for each environment, and additional ones may be used
to [logically categorize data to be consumed.][8]

By default data is merged and applied based on where the minion is defined in
top files.

### [Setup GPG][10]
[Alternative Reference][11]. [CLI Reference][19]

`/etc/salt/gpgkeys` is a required hard-coded directory. Ensure only the
salt-master user has access to this.

Note: salt-master requires no password for GPG decryption to work. Secure your
certs. You may want to enforce expiration on certs as well.

If entropy generation is slow (typical on VM's), install [`haveged`][18] to
speed up entropy collection.

#### Generate GPG keys for salt-master encryption/decryption
```bash
mkdir -p /etc/salt/gpgkeys
chmod 0700 /etc/salt/gpgkeys
gpg --gen-key --homedir /etc/salt/gpgkeys
```
 * use NO password for salt-master. secure your keys.
 * default option (RSA/RSA)
 * 4096 bit key
 * 0 (cert does not expire)
 * salty (salt@example.com)
 * no password.

#### Export public key for signing data.
```bash
gpg --homedir /etc/salt/gpgkeys --armor --export > public_key.gpg
```
This (`public_key.gpg`) is used by anyone on any system to created encrypted
data that only the server can read.

Import the public key for siginng usage
```bash
gpg --import public_key.gpg
```
These are stored in `~/.gnupg/`

### Using encrypted data in Pillar

#### Encrypting Data

##### A password or text material
```bash
echo -n "super_secret_server_stuff" | gpg --armor --batch --trust-model always --encrypt --recipient salty
```

##### A cert or file material
```bash
gpg --armor --batch --trust-model always --encrypt --recipient salty <file>
```
`salty` is the name of the recipient of the data (see GPG key creation).

##### GPG encrypting shadow passwords
The [salt user state documentation][20] recommends using `openssl passwd -1` to
generate a bash passwd hash. This **only hashes MD5**, modern distributuions of
linux hash **sha512**. Use the [python script][21] below to generate a _salted, sha512
hash_ in the correct format for consumption in `/etc/shadow`. Then just run that
through the GPG encryption to store in pillar.

_storing password hashes in pillar that are not additionally GPG encrypted is
probably a **BAD** idea._

###### Using utility
```bash
apt install whois
mkpasswd -m sha-512
```

###### Python3 version
```bash
python3 -c "import crypt, getpass; print(crypt.crypt(getpass.getpass('password to hash: '), crypt.mksalt(crypt.METHOD_SHA512)))"
```

#### Add to Pillar

Prefix any Pillar file using GPG encryped data with:
```yaml
#!yaml|gpg
```

Insert the GPG message block as the value for the key. Use a pipe (|) to denote
GPG message. Indentation matters.

```yaml
secret-stuff: |
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v2.0.22 (GNU/Linux)

  hQEMA4Pr9QJhL3umAQgAnZtS7lTyDR3kjr+VjCIADutmxyjrxbyaNnPEs3eJRi9G
  N6LtiFlUt24Jgdgupu/CG2IS815V0Vx3EbBknpNNwq0Yrs2joMnm92ZRv4AI6ZTo
  yQqGICetmBOS+vGk4jS8mj9qRjLamvPDOBPyNpKiRCFqu1TPKYw0a8xssO/j/pzW
  TJ39WsHXjtOWLkfYOaf7SKffYL9EsdU5tqXASe5UvjR1Gbj7wdjPl+vMZxRhzfOn
  YQ3fq3wNrGkuz2PpE7n77mmvYGVlXemw4o6tITZMa3MIFZqGTPbCCnh4OubqWGqd
  MtMNgPD2EeZ6wfEWkf1LGrrFy9POmdpssiU92J5dsNJQAdTAZVP4gtoyjWRtHJQB
  3FNarZY210P1o16s1n05ZbkVnz2FeZW/ClB6FqiewDe2EoXcVbXT5WgSZTHFi3mJ
  dFXQZGtReJL4vt8Iq8jSwRI=
  =wJ+K
  -----END PGP MESSAGE-----
some-other-key: data
```

#### Refresh Pillar and Push Data
Pillar will automatically refresh and push, however this allows you to
immediately regenerate pillar data and push new values to minions.

```bash
salt '*' saltutil.refresh_pillar
salt pillar.items
```
 * You should see the decrypted original text in the items list.

### Pillar Environment Data
By default data is merged and applied based on where the minion is defined in
top files. You can specify a specific environment (and are required to when
using `pillar_source_merging_strategy: none`) to get pillar values for that
environment:

```bash
pillarenv=dev
```

```bash
pillarenv=prod
```


[Installing Formulae][6]
------------------------
Forumlas are pre-defined salt modules that are defined by users to manage a
service or setup. [A curated list from Saltstack is here.][14]

These are stored in `srv/salt/env/formulae` and are directly accessing from the
same base scope, based on configuration:

```bash
ls -1 /srv/salt/env/formulae/some_formula
init.sls
pillar_config.sls
service.sls
```

top.sls
```
dev:
  'my_host':
    - some_formula

  'other_host':
    - some_formula
    - some_formula.pillar_config
    - some_formual.service
```


[Setup Minions][5]
-----------------
All minions by default need to be able to resolve the `salt` hostname to the
salt-master. This can be changed.

Minions should be run as `root`. Minions require root to properly install
software, update apt and execute commands.

Note: if you plan on installing docker, you need to use
`source_interface_name` or `source_address` when configuring the minion,
otherwise it could pick up the Docker interface and try to use that. This will
cause the minion to be unable to respond to the master.

### [Ubuntu][7]
A minion will not send the initial cert request until the minion is started.
By default `salt` should resolve, though this can be changes in the minion
configuration file.

Generally, you should manage the minion configuration file via salt after the
initial install / connection.

/etc/apt/sources.list.d/saltstack.list
```bash
deb http://repo.saltstack.com/py3/ubuntu/16.04/amd64/latest xenial main
```

Add the salt repository signing key
```
wget -O - https://repo.saltstack.com/py3/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
```

Install salt.
```bash
sudo apt update && sudo apt install salt-minion
```

Setup minion security requirements
```bash
verify_env: True
hash_type: 512
keysize: 4096
minion_sign_messages: True
```

### [Windows][16]
Download the latest [version of salt-minion here][15].

You can execute the installer from the CLI or GUI. If any dependencies are
needed, they can be downloaded and installed from `dependencies` as well.

[CLI][17]
```powershell
Salt-Minion-2018.3.0-Py3-AMD64-Setup.exe /S /master=<yoursaltmaster> /minion-name=<yourminionname> /start-minion-delayed
```

[GUI][17]
 * Specify the master name.
 * Specify the minion name.
 * Optionally provide a default configuration file.
 * Enable delayed start (allows highstates requiring reboots to work)

The minion will be installed to `c:\salt`

salt-minion can be managed like a normal windows service:
```powershell
sc start salt-minion
net start salt-minion
```


Signing Cert Requests
---------------------
A minion cannot connect and apply salt states until the cert is approved on the
salt-master.

Show all *unaccepted* certs and sign one.
```bash
salt-key -l unaccepted
salt-key -a <host>
```
Globbing is supported.

### Show All Certs
Show *all* certs on server.
```bash
salt-key -L
```


[Revoking Certs][11]
--------------------
To disable salt access for a specific minion, or remove non-approved certs.

See [Show All Certs](#show-all-certs) for getting a cert list.

```bash
salt-key -d <host>
```
Salt should remove the key automatically.


Master Frequent Commands
------------------------
Most commands support globbing and regex matching on minions, as well as on
Grains to match minions to execute commands.

### Run command on minions
```bash
salt '*' cmd.run 'ifconfig'

salt -G os:ubuntu cmd.run 'df -h'
```

### Get status of all minions
```bash
salt-run manage.status
```

### Show minions on a subnet
```bash
salt -S '10.5.5.0/24' network.ip_addrs
```

### Show avaliable grains on minions
```bash
salt '*' grains.items
```

### Debug level logging on salt-master
```bash
salt-master -l debug
```


Manually Running Minions
------------------------
Useful for testing as well as immediately applying changes outside of the run
window.

### Manual minion run
Just match the minion and apply the highstate. By default it will apply the
current environments.

```bash
salt 'my_minion' state.highstate
```

### Manual minion run, with specific environment
```bash
salt 'my_minion' state.highstate pillarenv=dev stateenv=dev
```

### Manual Agent Run with Debugging
```bash
salt-minion -l debug
```

### Show avaliable files to minions
```bash
salt-run fileserver.file_list saltenv=dev
```


Development References
----------------------

### Raw notes
using chocolately for windows.

This will use iexplore to download chocolatey and install it via a powershell
command
```powershell
salt '*' cmd.run "iex ((new-object new.webclient).DownloadString('https://chocolatey.org/install.ps1'))" shell=powershell
```

Install it
```powershell
salt '*' cmd.run 'choco install sublimetext3' shell=powershell
```

- can set cron job to execute state.highstate on server boot, as well as
  nightly, etc. outside of minion check time period.

salt-minion -d -> run as daemon. You can change /etc/salt/minion.d/ conf files
and restart this to change name (systemctl salt-minion restart)


[1]: https://saltstack.com/saltstack-enterprise-system-requirements/#
[2]: https://docs.saltstack.com/en/getstarted/system/communication.html
[3]: https://repo.saltstack.com/#ubuntu
[4]: https://docs.saltstack.com/en/latest/ref/configuration/master.html
[5]: https://www.linode.com/docs/security/ssl/create-a-self-signed-tls-certificate
[6]: https://docs.saltstack.com/en/2017.7/ref/configuration/nonroot.html
[7]: https://docs.saltstack.com/en/latest/topics/best_practices.html
[8]: https://docs.saltstack.com/en/latest/topics/tutorials/pillar.html
[9]: https://docs.saltstack.com/en/latest/topics/pillar/
[10]: http://joshbolling.com/2017/05/28/protect-pillar-data-with-gpg/
[11]: https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html
[12]: https://docs.saltstack.com/en/2016.11/topics/tutorials/starting_states.html
[13]: https://docs.saltstack.com/en/latest/ref/states/
[14]: https://github.com/saltstack-formulas
[15]: https://repo.saltstack.com/windows/
[16]: https://repo.saltstack.com/#windows
[17]: https://docs.saltstack.com/en/latest/topics/installation/windows.html
[18]: https://www.digitalocean.com/community/tutorials/how-to-setup-additional-entropy-for-cloud-servers-using-haveged
[19]: http://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/
[20]: https://docs.saltstack.com/en/latest/ref/states/all/salt.states.user.html
[21]: https://serverfault.com/questions/330069/how-to-create-an-sha-512-hashed-password-for-shadow
