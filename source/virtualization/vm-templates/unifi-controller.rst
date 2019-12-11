.. _unifi-controller-server:

Unifi AP Controller
###################
Uses :ref:`1804-server-base-install` and assumes post template setup scripts
have been run.

.. gport:: Ports Exposed (Unifi AP Controller)
  :port:     8443,
             8080
  :protocol: TCP,
             TCP
  :type:     External,
             External
  :purpose:  Webface management.,
             AP management / inform.
  :no_key_title:
  :no_caption:
  :no_launch:

Service Setup
*************
Add ubiquiti apt repository.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list.d/100-unifi-controller.list``

  deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti

.. code-block:: bash
  :caption: Install the service and start.

  sudo chmod 0644 /etc/apt/sources.list.d/100-unifi-controller.list
  sudo chown root:root /etc/apt/sources.list.d/100-unifi-controller.list
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50
  sudo apt update && sudo apt upgrade && sudo apt install unifi
  sudo service unifi start

If you have an existing backup of a controller, you can import it immediately
and not manually re-configure anything.

.. gflocation:: Important File Locations (Unifi AP Controller)
  :file:    /var/libs/unifi/backup/autobackup
  :purpose: Location of configuration backups.
  :no_key_title:
  :no_caption:
  :no_launch:

AP Configuration
****************
Run through the :ref:`example-vlan-network` for complete instructions setting up
a unifi controller.

Migrating existing AP's to a new controller
*******************************************
See :ref:`migration-controller-to-docker` for instructions on migrating to a new
controller. Platform is irrelevant.

.. rubric:: References

#. `Unifi Apt install with Ubuntu <https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-Update-via-APT-on-Debian-or-Ubuntu>`_
#. `Unifi Ports <https://help.ubnt.com/hc/en-us/articles/218506997-UniFi-Ports-Used>`_
#. `Migrating Unifi AP's to New Controller <https://community.ui.com/questions/9ca9d8e9-780d-404d-84df-e7762cb810fd>`_