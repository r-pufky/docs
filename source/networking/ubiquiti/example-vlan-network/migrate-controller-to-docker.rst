.. _migration-controller-to-docker:

Migrate Unifi Controller to Docker
##################################
* Reset Unifi Controller to fresh install on Docker.

Setup Unifi Docker `Container IP on DHCP`_.
* Connect to Edgerouter GUI @ ``http://10.1.1.1``.

.. uctree:: Add Docker Container IP for Controller.
  :key:    services --> dhcp server --> management --> action --> view details
  :names:  Unifi Controller
  :data:   {DOCKER UNIFI CONTAINER IP}
  :no_section:

Export laptop Unifi Controller settings.

.. ucontroller:: Add Docker Container IP on Original Unifi Controller.
  :key:        settings --> maintenance --> backup
  :names:      Backup Data Rentention
  :data:       Settings Only
  :no_section:

    .. note::
      Download the backup and ``shutdown`` the original Unifi Controller.

Startup Docker Unifi Controller and import config, then set the correct inform
IP in docker container.

.. ucontroller:: Set Inform IP on docker Unifi Controller.
  :controller: http://{DOCKER UNIFI CONTAINER IP}:8443
  :key:        settings --> controller
  :names:      Controller Hostname/IP
  :data:       {DOCKER UNIFI CONTROLLER IP}
  :no_section:

.. note::
  If the Controller IP is different, manually update inform URI for each device
  that was previously connected to the original Controller and set correct
  inform URI. These should now auto adopt when they contact the new inform URI.

  .. code-block:: bash
    :caption: Manually Update Controller Inform IP on Device (SSH to Unifi
              Devices).

    info
    set-inform http://{DOCKER UNIFI CONTAINER IP}:8080/inform

.. _Container IP on DHCP: https://help.ubnt.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7