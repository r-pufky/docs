.. _unifi-controller-vlan-setup:

Unifi Controller VLAN Setup
###########################
This will be used to setup the Unifi managed switches and APs. See
:ref:`example-network-diagram`. Download and install the `Unifi Controller`_
onto the setup laptop.

Basic Setup Wizard
******************
Connect to Unifi Controller @ http://localhost:8443.

.. note::
  **Skip** *device*, *wifi* and *cloud login* configuration during the intial
  configuration.

.. ucontroller:: Basic Unifi Controller Setup
  :key_title:    Setup Wizard
  :option:       Select your Country,
                 Select your Timezone,
                 › ☑
  :setting:      {COUNTRY},
                 {YOUR TIMEZONE},
                 Enable Auto Backup
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Basic Unifi Controller Access Setup
  :key_title:    Setup Wizard --> Controller Access
  :option:       Admin Name,
                 Admin Email,
                 Admin Password,
                 Device Authentication,
                 Device Password
  :setting:      {ADMIN USER},
                 {EMAIL},
                 {ADMIN PW},
                 {DEVICE USER},
                 {DEVICE PW}
  :no_section:
  :no_caption:
  :no_launch:

    .. warning::
      The *admin name* account is the `super admin`_ for the controller, meaning
      that account can manage multiple sites as well as devices. The *device
      authentication* account is used to manage physical devices via the UI or
      SSH on that device.

.. _basic-controller-setup:

Basic Controller Setup
**********************
.. ucontroller:: Basic Unifi Controller Setup
  :key_title:    ⚙ --> Controller --> Controller Settings
  :option:       Controller Name,
                 Controller Hostname/IP,
                 › ☐,
                 › ☑,
                 Store,
                 Support Messaging,
                 Real-time Updates in Web Browser,
                 › ☐
  :setting:      {CONTROLLER DNS NAME},
                 {CONTROLLER IP},
                 Override inform host with controller hostname/IP,
                 Make controller discoverable on L2 network,
                 Disable store for all users,
                 Disable live support for all users,
                 Automatically adapt rates of real-time updates,
                 Enable mail server
  :no_section:
  :no_caption:
  :no_launch:

.. warning::
  L2 device discovery will help to adopt controllers which are not receiving a
  `unifi controller DHCP option`_. These settings are only for initial setup
  with the laptop and may be changed or disabled after initial configuration to
  rely on DHCP or set inform.

.. ucontroller:: Site Configuration
  :key_title:    ⚙ --> Site --> Site Configuration
  :option:       Site Name,
                 Country,
                 Timezone
  :setting:      {YOUR SITE NAME},
                 {COUNTRY},
                 {LOCAL TIMEZONE}
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Service Configuration
  :key_title:    ⚙ --> Site --> Services
  :option:       ☐,
                 ☑,
                 ☐,
                 ☐,
                 ☐,
                 ☑,
                 ☑,
                 ☐,
                 ☐
  :setting:      Advanced Features,
                 Automatically upgrade AP firmware,
                 Enable status LED,
                 Enable alert emails,
                 Enable periodic speed test every,
                 Enable connectivity monitor and wireless uplink,
                 Default gateway,
                 Enable remote Syslog server,
                 Enable Netconsole logging server
  :no_section:
  :no_caption:
  :no_launch:

    .. warning::
      Alerts and advanced logging disabled for initial setup, change these after
      finishing configuration.

.. ucontroller:: Provider Capabilities
  :key_title:    ⚙ --> Site --> Provider Capabilities
  :option:       Download,
                 Upload
  :setting:      1 Gbps,
                 1 Gbps
  :no_section:
  :no_caption:
  :no_launch:

    .. warning::
      Upload/Download settings should be reflective of your Internet connection
      for proper scaling of graphing data. It is *not* a throttle.

.. ucontroller:: Device Authentication
  :key_title:    ⚙ --> Site --> Device Authentication
  :option:       ☑,
                 Username,
                 Password
  :setting:      Enable SSH Authentication,
                 {DEVICE USER},
                 {DEVICE PW}
  :no_section:
  :no_caption:
  :no_launch:

Apply changes.

VLAN Configuration
******************
Add all VLANS using the :ref:`VLAN Table <vlan-table>`.

.. ucontroller:: Default LAN Network
  :key_title:    ⚙ --> Networks --> LAN
  :option:       ☑,
                 ☑,
                 Gateway/Subnet,
                 Domain Name,
                 › ☐,
                 DHCP Server,
                 › ☐,
                 › ☐,
                 IPv6 Interface Type
  :setting:      Corporate,
                 LAN,
                 10.1.1.1/24,
                 {YOUR DOMAIN},
                 Enable IGMP Snooping,
                 None,
                 Enable DHCP gaurding,
                 Enable UPnP LAN,
                 None
  :no_section:
  :no_caption:
  :no_launch:

    .. warning::
      This will be the default network when new devices are discovered before
      they are adopted. This is also the untagged :term:`Management VLAN`
      network. Configure with :term:`Management VLAN` settings.

.. ucontroller:: Create All VLAN Networks
  :key_title:    ⚙ --> Networks --> Create New Network
  :option:       Name,
                 ☑,
                 VLAN
  :setting:      Wired,
                 VLAN Only,
                 2
  :no_section:
  :no_caption:
  :no_launch:

    .. note::
      Add all VLANS using the :ref:`VLAN Table <vlan-table>`. :term:`Management
      VLAN` is not explicitly defined as a VLAN -- untagged traffic coming into
      *eth0* IS management traffic.

Add Trunk Port Profiles
***********************
.. ucontroller:: Add AP Wireless Trunk Port Profiles
  :key_title:    ⚙ -->
                 Profiles -->
                 Switch Ports -->
                 Add New Port Profile -->
                 Create New Switch Port Profile
  :option:       Profile Name,
                 › POE,
                 Networks/VLANs,
                 › Native Network,
                 › Tagged Networks,
                 › Voice Network
  :setting:      trunk-wifi,
                 PoE/PoE+,
                 ,
                 LAN,
                 wifi,
                 None
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Add Wired Trunk Port Profiles
  :key_title:    ⚙ -->
                 Profiles -->
                 Switch Ports -->
                 Add New Port Profile -->
                 Create New Switch Port Profile
  :option:       Profile Name,
                 › POE,
                 Networks/VLANs,
                 › Native Network,
                 › Tagged Networks,
                 › Voice Network
  :setting:      trunk-wired,
                 Off,
                 ,
                 LAN,
                 wifi wired,
                 None
  :no_section:
  :no_caption:
  :no_launch:

.. ucontroller:: Add Server Trunk Port Profiles
  :key_title:    ⚙ -->
                 Profiles -->
                 Switch Ports -->
                 Add New Port Profile -->
                 Create New Switch Port Profile
  :option:       Profile Name,
                 › POE,
                 Networks/VLANs,
                 › Native Network,
                 › Tagged Networks,
                 › Voice Network
  :setting:      trunk-server,
                 Off,
                 ,
                 LAN,
                 server infrastructure,
                 None
  :no_section:
  :no_caption:
  :no_launch:

.. rubric:: References

#. `Using VLANs with Unifi Wireless Routing <https://help.ubnt.com/hc/en-us/articles/219654087-UniFi-Using-VLANs-with-UniFi-Wireless-Routing-Switching-Hardware#UAP>`_
#. `Tagging and Untagging Traffic <https://help.ubnt.com/hc/en-us/articles/204962144#1>`_
#. `Lessons Learned from Deploying a Unifi Network <https://www.douglasisaksson.com/lessons-learned-from-deploying-a-unifi-network-at-home/>`_
#. `Unifi Switch 8 and VLANs <https://www.youtube.com/watch?v=JblnjsnJNJU>`_

.. _Unifi Controller: https://www.ui.com/download/?q=controller
.. _super admin: https://help.ubnt.com/hc/en-us/articles/204909374-UniFi-Accounts-and-Passwords-for-Controller-Cloud-Key-and-Other-Devices
.. _unifi controller DHCP option: https://help.ubnt.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7