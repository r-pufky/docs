.. _salt-requirements:

`Requirements`_
###############
There are no specific requirements for Salt Open Source. Enterprise requirements
are defined here. Most users report actual usage minimum requirements as:

+---------------+---------------+
| < 500 minions | > 500 minions |
+===============+===============+
| RAM: 2GB      | RAM: 4GB      |
+---------------+---------------+
| CPU: 1        | CPU: 4        |
+---------------+---------------+
| DISK: 20GB    | DISK: 20GB    |
+---------------+---------------+

`Ports Exposed`_
****************
By default ``salt`` should resolve to the master IP for the minion, this can be
configured in the minion as a DNS name or IP address.

+------+----------+-------------------------------------------------+
| Port | Protocol | Purpose                                         |
+======+==========+=================================================+
| 4505 | TCP      | Minion listen port for pubsub messages.         |
+------+----------+-------------------------------------------------+
| 4506 | TCP      | Master file/data push, Minion push result data. |
+------+----------+-------------------------------------------------+

Important File Locations
************************
+-----------------------+------------------------------------------------------+
| File                  | Purpose                                              |
+=======================+======================================================+
| /etc/salt             | Salt configuration, both master and minion.          |
+-----------------------+------------------------------------------------------+
| /etc/salt/gpgkeys     | Master private GPG keys for decrypting data. Hard    |
|                       | coded.                                               |
+-----------------------+------------------------------------------------------+
| /etc/salt/master      | Master configuration flat file. This should be       |
|                       | untouched for sane defaults. Set custom              |
|                       | configuration in the master configuration directory. |
+-----------------------+------------------------------------------------------+
| /etc/salt/master.d    | Master configuration directory.                      |
+-----------------------+------------------------------------------------------+
| /etc/salt/minion      | Minion configuration flat file. This should be       |
|                       | untouched for sane defaults. Set custom              |
|                       | configuration in the minion configuration directory. |
+-----------------------+------------------------------------------------------+
| /etc/salt/minion.d    | Minion configuration directory.                      |
+-----------------------+------------------------------------------------------+
| /etc/salt/pki/minions | Keyfile data for minions. Deleted minions should be  |
|                       | automatically removed.                               |
+-----------------------+------------------------------------------------------+
| /srv/salt             | Master service directory structure for hosting       |
|                       | files, forumlas and data. See                        |
|                       | :ref:`salt-service-directory-best-practices`         |
+-----------------------+------------------------------------------------------+
| /var/log/salt/master  | Master logging/error messages. Useful for debugging  |
|                       | module errors. When setup with encryption and        |
|                       | no-minion reporting, errors will appear here for     |
|                       | minions.                                             |
+-----------------------+------------------------------------------------------+
| /var/log/salt/minion  | Minion logging/error messages. Many minion errors    |
|                       | are logged on the server side, especially for        |
|                       | encrypted Pillar data.                               |
+-----------------------+------------------------------------------------------+
| c:/salt/conf/minion   | Minion configuration flat file for Windows. This     |
|                       | should be untouched for sane defaults. Set custom    |
|                       | configuration in the master configuration directory. |
+-----------------------+------------------------------------------------------+
| c:/salt/conf/minion.d | Minion configuration directory.                      |
+-----------------------+------------------------------------------------------+

.. _salt-service-directory-best-practices:

Service Directory Best Practices
********************************
This is the optimal directory structure for Salt based on actual usage and the
following requirements:

* Hard segregation of all data ``prod`` and ``dev`` for easy versioning,
  deployments, rollbacks and rollouts.
* Generic configuration management layout with common terms that remove the need
  to know salt-specific terminology.
* Focusing on pushing all minion configuration data to *Pillar* minimizing
  *static, globally avaliable unencrypted minion files*. Only minions with
  explicit access to data can read it.

+----------------------------------+-------------------------------------------+
| Service Directory                | Purpose                                   |
+==================================+===========================================+
| /srv/salt/data/{prod,dev}        | prod and dev Pillar data.                 |
+----------------------------------+-------------------------------------------+
| /srv/salt/template/{prod,dev}    | prod and dev salt formulas                |
+----------------------------------+-------------------------------------------+
| /srv/salt/static/{prod,dev,base} | prod, dev, and base globally avaliable    |
|                                  | static data. Base is ununsed other than   |
|                                  | to provide a catch-all for any minion not |
|                                  | in dev or prod.                           |
+----------------------------------+-------------------------------------------+

.. _Requirements: https://www.saltstack.com/saltstack-enterprise-system-requirements/
.. _Ports Exposed: https://docs.saltstack.com/en/getstarted/system/communication.html