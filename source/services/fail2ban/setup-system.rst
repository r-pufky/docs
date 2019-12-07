.. _service-fail2ban-system:

fail2ban for System
###################
Automatically ban repeated failed authentication attempts across system
services.

Docker Creation
***************
.. code-block:: yaml
  :caption: Docker Compose

  f2b-system:
    image: crazymax/fail2ban:latest
    restart: unless-stopped
    network_mode: host
    cap_add:
      - NET_ADMIN
      - NET_RAW
    environment:
      - F2B_LOG_LEVE=DEBUG
      - F2B_DB_PURGE_AGE=30d
      - F2B_MAX_RETRY=5
      - F2B_ACTION=%(action_)s
      - F2B_IPTABLES_CHAIN=INPUT
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/fail2ban/system:/data
      - /etc/localtime:/etc/localtime:ro
      - /var/log:/var/log:ro

See :ref:`service-nginx-logs-to-system` for setting up NGINX proxy logs.

System Setup
************
Enable `fail2ban for sshd`_ system service.

.. code-block:: ini
  :caption: **0644 root root** ``/data/jail.d/sshd.conf``

  [sshd]
  enabled  = true
  port     = ssh
  filter   = sshd[mode=aggressive]
  logpath  = /var/log/auth.log
  bantime  = -1
  findtime = 86400
  maxretry = 5

* Restart ``f2b-system``.
* Attempt an invalid SSH login and watch the docker logs to see if ssh is
  getting properly identified ``docker logs f2b-system``.
* ``bantime`` of ``-1`` means forever.
* ``findtime`` of ``86400`` is one day.

.. _fail2ban for sshd: https://github.com/crazy-max/docker-fail2ban/tree/master/examples/jails/sshd