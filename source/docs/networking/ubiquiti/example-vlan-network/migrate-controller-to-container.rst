.. _migration-controller-to-container:

Migrate Unifi Controller to Container
#####################################

See :ref:`service-unifi-controller` for container creation.

* Reset Unifi Controller to fresh install.
* Setup Unifi `Container IP on DHCP <https://help.ui.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7>`_.
* Connect to Edgerouter GUI @ http://10.1.1.1.

.. gui::   Add Container IP for Controller
  :label:  Ubiquiti
  :path:   Services --> DHCP Server --> Management --> Action -->
           View Details
  :value0: Unifi Controller, {IP}

  Be sure to use the unifi container IP.

Export laptop Unifi Controller settings.

.. gui::   Add Container IP on Original Unifi Controller
  :label:  Ubiquiti
  :path:   ⚙ --> Maintenance --> Backup
  :value0: Backup Data Rentention, Settings Only

  .. note::
    Download the backup and ``shutdown`` the original Unifi Controller.

Startup Unifi Controller and import config, then set the correct inform
IP in container.

.. gui::   Set Inform IP on Unifi Controller
  :label:  Ubiquiti
  :path:   ⚙ --> Controller
  :value0: Controller Hostname/IP, {IP}

.. note::
  If the Controller IP is different, manually update inform URI for each device
  that was previously connected to the original Controller and set correct
  inform URI. These should now auto adopt when they contact the new inform URI.

  .. code-block:: bash
    :caption: Manually Update Controller Inform IP on Device (SSH to Unifi
              Devices).

    info
    set-inform http://{UNIFI CONTAINER IP}:8080/inform

