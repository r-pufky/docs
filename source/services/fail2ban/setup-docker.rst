.. _service-fail2ban-docker:

fail2ban for Docker
###################
Automatically ban repeated failed authentication attempts across docker
services.

See `fail2ban for a docker based reverse-proxy`_.

.. code-block:: yaml
  :caption: Docker Compose

  f2b-docker:
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
      - F2B_IPTABLES_CHAIN=DOCKER-USER
      - TZ=America/Los_Angeles
    volumes:
      - /data/services/fail2ban/docker:/data
      - /etc/localtime:/etc/localtime:ro
      - /var/log:/var/log:ro

See :ref:`service-nginx-logs-to-system` for setting up NGINX proxy logs.

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
filters are `based off the default filters`_.

Detect Bad Bots
===============
.. literalinclude:: source/nginx-badbots.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-badbots.conf``
  :language: ini

.. note::
  This is a direct copy of the `apache-badbots filter`_.

Detect Bad NGINX Basic Auth Attempts
====================================
.. literalinclude:: source/nginx-http-auth.conf
  :caption: **0644 root root** ``/data/filter.d/nginx-http-auth.conf``
  :language: ini

.. note::
  This is the basic `nginx-http-auth filter`_ with an additional line to handle
  basic auth with no username or password.

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

.. _fail2ban for a docker based reverse-proxy: https://www.digitalocean.com/community/tutorials/how-to-protect-an-nginx-server-with-fail2ban-on-ubuntu-14-04
.. _based off the default filters: https://github.com/fail2ban/fail2ban/tree/master/config/filter.d
.. _nginx-http-auth filter: https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/nginx-http-auth.conf
.. _apache-badbots filter: https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/apache-badbots.conf