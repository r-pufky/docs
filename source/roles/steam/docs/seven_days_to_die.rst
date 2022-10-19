.. _service-steam-seven-days-to-die:

7 Days to Die
#############
`7 Days to Die <https://7daystodie.com/>`_ dedicated server on steam.

.. role:: steam
  :service_doc: https://7daystodie.gamepedia.com/System_Requirements
  :ref:         https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server#Installation,
                https://www.gameserverkings.com/knowledge-base/7-days-to-die/7d2d-new-user-guide/
  :private:
  :update:      2022-10-10
  :open:

  7 Days to Die dedicated server.

  * Role handles all steps that are provided in this documentation.
  * If connecting on local network, use the private IP of the server, not the
    public IP address.
  * Control Panel and Telnet are insecure. **Disable** and **block** ports.
  * ``steam_7days_dir/saves`` contains server state information.

Ports
*****
.. literalinclude:: ../defaults/main/seven_days_to_die/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/seven_days_to_die/main.yml

Server Admin
************
.. literalinclude:: ../defaults/main/seven_days_to_die/serveradmin.xml.yml

Server Config
*************
.. literalinclude:: ../defaults/main/seven_days_to_die/serverconfig.xml.yml
