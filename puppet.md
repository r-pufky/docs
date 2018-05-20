Puppet Server Setup
-------------------
Puppet: Everything works great, until it doesn't. God I hate Ruby.

1. [Requirements](#requirements)
2. [Ports Exposed](#ports-exposed)
3. [Important File Locations](#important-file-locations)
4. [Service Setup](#service-setup)
5. [Installing Puppet Modules](#installing-puppet-modules)
6. [Setup Agents](#setup-agents)
7. [Signing Cert Requests](#signing-cert-requests)
8. [Revoking Certs](#revoking-certs)
9. [Manually Running Agents](#manually-running-agents)
10. [Module Development References](#module-development-references)


[Requirements][1]
-----------------

| < 1000   | > 1000   |
|----------|----------|
| RAM: 2GB | RAM: 2GB |
| CPU: 2   | CPU: 2-4 |


[Ports Exposed][2]
------------------

| Port | Protocol | Purpose                                                |
|------|----------|--------------------------------------------------------|
| 8410 | TCP      | Agent CSR requests, management                         |
| 53   | UDP      | Forward/Reverse DNS for 'puppet' lookup. Must Resolve. |

Forward and Reverse DNS must work for `puppet`.


Important File Locations
------------------------

| File                                                            | Purpose                                                       |
|-----------------------------------------------------------------|---------------------------------------------------------------|
| /var/log/puppetlabs/puppetserver/puppetserver.log               | Serverside error messages. Useful for debuggin module errors. |
| /etc/puppetlabs/code/environments/production/manifests          | All site node configuration information.                      |
| /etc/puppetlabs/code/environments/production/modules            | Install modules. Both custom and puppet provided.             |
| /etc/puppetlabs/code/environments/production/manifests/profiles | Defines profiles to use for nodes.                            |
| /etc/puppetlabs/code/environments/production/manifests/roles    | Defines roles to use for nodes.                               |


[Service Setup][3]
------------------
Install [puppetmaster from package][4]. By default will use 2GB of ram for JVM.

Puppet server hostname should resolve to `puppet`.

```bash
wget https://apt.puppetlabs.com/puppet5-release-<CODENAME>.deb
sudo dpkg -i puppet5-release-<CODENAME>.deb
sudo apt update
sudo apt install puppetserver
```

Start the service and enable [start at boot][5]
```bash
sudo service puppetserver start
sudo systemctl enable puppetserver
```


[Installing Puppet Modules][6]
------------------------------
Modules are pre-defined puppet manifests that are defined by users. Usually
easier than writing your own.

Installing Published Puppet Modules
```bash
puppet module search
puppet module install <module>
```

You can install your own private modules by copying them to the `modules`
location specified in [Important File Locations](#important-file-locations)


[Setup Agents][5]
-----------------
All agents need to be able to resolve the `puppet` hostname to the puppet
server.

### [Ubuntu][7]
An agent will not send the initial cert request until the `puppet-agent` service
is started. Packages are named by ubuntu release.

Be sure execute any puppet commands as __root__; don't use `sudo`. If you have
just installed puppet-agent, logout/login to apply path changes to find puppet.

```bash
wget https://apt.puppetlabs.com/puppet5-release-<CODENAME>.deb
sudo dpkg -i puppet5-release-<CODENAME>.deb
sudo apt update
sudo apt install puppet-agent
sudo systemctl start puppet
sudo systemctl enable puppet
```

### [Windows][8]
Download the [latest puppet agent installer][10]. See parent directory for
non-latest releases.

You can execute from the commandline, or the GUI.

```powershell
msiexec /qn /norestart /i puppet-agent-<VERSION>-x64.msi PUPPET_MASTER_SERVER=puppet.example.com
```

### [OSX][9]
Download the [latest puppet installer for OSX version][12]. See latest installer
for version of OSX.

Run GUI installer and setup host and puppet server name.


Signing Cert Requests
---------------------
A puppet agent cannot connect and apply puppet manifests until the cert is
approved on the puppet server.

Show all *unapproved* certs and sign one.
```bash
puppet cert list
puppet cert sign <host>
```

### Show All Certs
Show *all* certs on server. A *+* indicates the certificate is already signed.
```bash
puppet cert list -all
```


[Revoking Certs][11]
--------------------
To disable puppet access for a specific agent, or remove non-approved certs.

See [Show All Certs](#show-all-certs) for getting a cert list.

```bash
puppet cert --revoke <host>
puppet cert --clean <host>
```

If that doesn't work, use a hammer. This is deprecated.
```bash
puppet ca destroy <host>
```


Manually Running Agents
-----------------------
Useful for testing as well as immediately applying changes outside of the run
window.

This requires you to be __root__ on the system; don't use `sudo`.

### Manual Agent Run
```bash
puppet agent -t
```

### Manual Agent Run with Debugging
```bash
puppet agent -t -d
```

Module Development References
-----------------------------
 * [Writing Modules][13]
 * [How puppet works overview][14]


[1]: https://puppet.com/docs/puppet/5.5/system_requirements.html
[2]: https://puppet.com/docs/puppet/5.5/install_pre.html
[3]: https://puppet.com/docs/puppet/5.5/puppet_platform.html
[4]: https://puppet.com/docs/puppetserver/5.2/install_from_packages.html
[5]: https://www.digitalocean.com/community/tutorials/how-to-install-puppet-4-on-ubuntu-16-04
[6]: https://puppet.com/docs/puppet/5.5/modules_installing.html
[7]: https://puppet.com/docs/puppet/5.5/install_linux.html
[8]: https://puppet.com/docs/puppet/5.5/install_windows.html
[9]: https://puppet.com/docs/puppet/5.5/install_osx.html
[10]: https://downloads.puppetlabs.com/windows/puppet5/puppet-agent-x64-latest.msi
[11]: https://superuser.com/questions/784471/how-to-reject-certificate-request-on-puppet-master
[12]: http://downloads.puppetlabs.com/mac/
[13]: https://www.digitalocean.com/community/tutorials/getting-started-with-puppet-code-manifests-and-modules
[14]: https://www.example42.com/tutorials/PuppetTutorial/#slide-57