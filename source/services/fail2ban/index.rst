.. _service-fail2ban:

fail2ban
########
Automatically ban repeated failed authentication attempts across system and
docker services.

See `fail2ban Docker and Documentation`_.

.. gtable:: Docker Capabilities
  :header: Capability,
           Action
  :c0:     NET_ADMIN,
           NET_RAW
  :c1:     ADD,
           ADD
  :no_key_title:
  :no_launch:

.. gflocation:: Important File Locations (fail2ban)
  :file:    /data/jail.d,
            /data/filter.d,
            /var/log
  :purpose: Defines how services are watched.,
            Defines actions on services.,
            Mapped log location to watch.
  :no_key_title:
  :no_caption:
  :no_launch:

* Other containers may map their **logging** directories to the system
  ``/var/log`` which will enable ``fail2ban`` to monitor docker container
  services.
* Containers should be separated from everything else. No need for external
  network access.
* Add capabilities are needed to modify ``iptable`` rules for the system and
  docker.

#. :ref:`service-fail2ban-system`.
#. :ref:`service-fail2ban-docker`.
#. :ref:`service-fail2ban-common-commands`.
#. :ref:`service-fail2ban-troubleshooting`.

.. _fail2ban Docker and Documentation: https://hub.docker.com/r/crazymax/fail2ban

.. toctree::
   :hidden:
   :maxdepth: -1

   setup-system
   setup-docker
   common-commands
   troubleshooting