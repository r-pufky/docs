.. _service-fail2ban-custom-filters:

Custom Filters
##############

Enable NGINX Jails
******************
This will enable jails for proxy auth, bad bots, home directories, open proxy,
and open scripts.

.. literalinclude:: source/nginx.conf
  :caption: **0644 root root** ``/data/jail.d/nginx.conf``
  :language: ini

:download:`Example nginx.conf <source/nginx.conf>`

Enable NGINX Filters
********************
This will allow fail2ban to take action on matches and ban IPs. Most of these
filters are `based off the default filters <https://github.com/fail2ban/fail2ban/tree/master/config/filter.d>`_.

Detect Bad Bots
===============
.. literalinclude:: source/nginx-badbots.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-badbots.conf``
  :language: ini

This is a direct copy of the `apache-badbots filter <https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/apache-badbots.conf>`_.

Detect Bad NGINX Basic Auth Attempts
====================================
.. literalinclude:: source/nginx-http-auth.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-http-auth.conf``
  :language: ini

This is the basic `nginx-http-auth filter <https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/nginx-http-auth.conf>`_
with an additional line to handle basic auth with no username or password.

Detect Access to Home Directories VIA Web
=========================================
.. literalinclude:: source/nginx-nohome.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-nohome.conf``
  :language: ini

Detect Use of Server as a Ad-hoc Proxy
======================================
.. literalinclude:: source/nginx-noproxy.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-noproxy.conf``
  :language: ini

Detect Attempts to Directly Access/Execute Scripts
==================================================
.. literalinclude:: source/nginx-noscript.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-noscript.conf``
  :language: ini

Detect Access to Forbidden Indexes
==================================
.. literalinclude:: source/nginx-forbidden.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-forbidden.conf``
  :language: ini

Detect Attempts to Access Invalid Files/Directories
===================================================
.. literalinclude:: source/nginx-no-file-directory.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-no-file-directory.conf``
  :language: ini

Detect Multiple Client Error Codes
==================================
.. literalinclude:: source/nginx-errors.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-errors.conf``
  :language: ini

Restart fail2ban.

System Setup
************
Enable fail2ban for sshd system service.

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

* Attempt an invalid SSH login and watch logs to see if ssh is getting properly
  identified.
