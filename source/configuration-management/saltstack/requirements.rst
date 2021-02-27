.. _salt-requirements:

`Requirements`_
###############
There are no specific requirements for Salt Open Source. Enterprise requirements
are defined here. Most users report actual usage minimum requirements as:

.. gtable:: Saltstack Minimum Requirements.
  :header: < 500 Minions,
           > 500 Minions
  :c0:     RAM: 2GB,
           CPU: 1,
           DISK: 20GB
  :c1:     RAM: 4GB,
           CPU: 4,
           DISK: 20GB
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

Ports
*****
.. ports:: Saltstack Ports
  :value0: 4505; {TCP}; {PUBLIC}; Minion listen port for pubsub messages
  :value1: 4506; {TCP}; {PUBLIC}; Master file/data push, Minion push result data
  :delim: ;
  :open:

  By default ``salt`` should resolve to the master IP for the minion, this can
  be configured in the minion as a DNS name or IP address.

Files
*****
.. files::  Saltstack Files
  :value0:  /etc/salt, Salt configuration; both master and minion
  :value1:  /etc/salt/gpgkeys,
            Master private GPG keys for decrypting data. Hard coded.
  :value2:  /etc/salt/master, 
            Master configuration flat file. This should be untouched for sane
            defaults. Set custom configuration in the master configuration
            directory.
  :value3:  /etc/salt/master.d, Master configuration directory
  :value4:  /etc/salt/minion,
            Minion configuration flat file. This should be untouched for sane
            defaults. Set custom configuration in the minion configuration
            directory.
  :value5:  /etc/salt/minion.d, Minion configuration directory
  :value6:  /etc/salt/pki/minions,
            Keyfile data for minions. Deleted minions should be automatically
            removed.
  :value7:  /srv/salt,
            Master service directory structure for hosting files/forumlas and
            data. See best practices (below).
  :value8:  /var/log/salt/master,
            Master logging/error messages. Useful for debugging module errors.
            When setup with encryption and no-minion reporting errors will
            appear here for minions.
  :value9:  /var/log/salt/minion,
            Minion logging/error messages. Many minion errors are logged on the
            server side; especially for encrypted Pillar data.
  :value10: c:\salt\conf\minion,
            Minion configuration flat file for Windows. This should be untouched
            for sane defaults. Set custom configuration in the master
            configuration directory.
  :value11: c:\salt\conf\minion.d, Minion configuration directory
  :open:

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

.. gtable:: Service Directory Best Practice.
  :header: Service Directory;
           Purpose
  :c0:     /srv/salt/data/{prod,dev};
           /srv/salt/template/{prod,dev};
           /srv/salt/static/{prod,dev,base}
  :c1:     prod and dev Pillar data.;
           prod and dev salt formulas.;
           prod, dev, and base globally avaliable static data. Base is ununsed other than to provide a catch-all for any minion not in dev or prod.
  :delim: ;
  :no_key_title:
  :no_section:
  :no_caption:
  :no_launch:

.. rubric:: References

#. `Saltstack Ports Exposed <https://docs.saltstack.com/en/getstarted/system/communication.html>`_

.. _Requirements: https://www.saltstack.com/saltstack-enterprise-system-requirements/
