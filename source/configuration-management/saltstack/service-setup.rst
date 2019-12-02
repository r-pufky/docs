.. _salt-service-setup:

`Service Setup`_
################
Salt can run on both Python 2 and 3. Use Python 3. See `Best Practices`_.

.. code-block::
  :caption: **0644 root root** ``/etc/apt/sources.list.d/saltstack.list``

  deb http://repo.saltstack.com/py3/ubuntu/16.04/amd64/latest bionic main

.. code-block:: bash
  :caption: Add the salt repository signing key.

  wget -O - https://repo.saltstack.com/py3/ubuntu/18.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -

.. code-block:: bash
  :caption: Install salt. A minion can be installed on the master as well to
            have the master manage itself.

  sudo apt update && sudo apt install salt-master

.. _salt-tls-protocol:

`Use TLS for protocol encryption`_
**********************************
Communication is automatically encrypted, but TCP is not. Force TLS encryption.

.. code-block:: bash
  :caption: Generate a 4096 bit certificate for TLS.

  mkdir -p /etc/salt/pki/certs && cd /etc/salt/pki/certs
  openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out salt.crt -keyout salt.key
  chmod 0400 salt.key

.. _salt-non-root-user:

`Non-root User`_
****************
By default salt-master runs as root. Nothing the master does requires root.

.. code-block:: bash
  :caption: Create ``salt`` user for master and set permissions.

  adduser --shell /bin/bash --no-create-home --disabled-password --disabled-login salt
  chown -R salt:salt /etc/salt /var/cache/salt /var/log/salt /var/run/salt /srv/salt
  systemctl restart salt-master

.. note::
  Verify any custom directories are modified as well. ``salt-master`` does
  require a shell to run commands such as ``salt-run``.

Minions **require root** to properly install software, update apt and execute
commands.

.. _Service Setup: https://repo.saltstack.com/#ubuntu
.. _Use TLS for protocol encryption: https://www.linode.com/docs/security/ssl/create-a-self-signed-tls-certificate
.. _Non-root User: https://docs.saltstack.com/en/2017.7/ref/configuration/nonroot.html
.. _Best Practices: https://docs.saltstack.com/en/latest/topics/best_practices.html