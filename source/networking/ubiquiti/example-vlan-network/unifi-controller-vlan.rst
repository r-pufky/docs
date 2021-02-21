.. _unifi-controller-vlan-setup:

Unifi Controller VLAN Setup
###########################
This will be used to setup the Unifi managed switches and APs. See
:ref:`example-network-diagram`. Download and install the `Unifi Controller`_
onto the setup laptop.

.. danger::
  The most recent firmware update (~2019-10) has added `telemetry`_ to ubiquity
  devices; disabled by default.

  **Block or blackhole** ``trace.svc.ui.com``.

Basic Setup Wizard
******************
Connect to Unifi Controller @ http://localhost:8443.

.. note::
  **Skip** *device*, *wifi* and *cloud login* configuration during the intial
  configuration.

.. ubiquiti:: Basic Unifi Controller Setup
  :path:      Setup Wizard
  :value0:    Select your Country, {COUNTRY}
  :value1:    Select your Timezone, {TZ}
  :value2:    › ☑, Enable Auto Backup

.. ubiquiti:: Basic Unifi Controller Access Setup
  :path:      Setup Wizard --> Controller Access
  :value0:    Admin Name, {USER}
  :value1:    Admin Email, {EMAIL}
  :value2:    Admin Password, {PASS}
  :value3:    Device Authentication, {USER}
  :value4:    Device Password, {PASS}

  .. warning::
    The *admin name* account is the `super admin`_ for the controller, meaning
    that account can manage multiple sites as well as devices. The *device
    authentication* account is used to manage physical devices via the UI or
    SSH on that device.

.. _basic-controller-setup:

Basic Controller Setup
**********************
.. ubiquiti:: Basic Unifi Controller Setup
  :path:      ⚙ --> Controller --> Controller Settings
  :value0:    Controller Name, {HOST}
  :value1:    Controller Hostname/IP, {IP}
  :value2:    › ☐, Override inform host with controller hostname/IP
  :value3:    › ☑, Make controller discoverable on L2 network
  :value4:    Store, Disable store for all users
  :value5:    Support Messaging, Disable live support for all users
  :value6:    Real-time Updates in Web Browser, Automatically adapt rates of real-time updates
  :value7:    Analytics & Improvements, {OFF}
  :value8:    › ☐, Enable mail server

.. warning::
  L2 device discovery will help to adopt controllers which are not receiving a
  `unifi controller DHCP option`_. These settings are only for initial setup
  with the laptop and may be changed or disabled after initial configuration to
  rely on DHCP or set inform.

.. ubiquiti:: Remote Access Controller Setup
  :path:      ⚙ --> Remote Access --> Controller
  :value0:    Enable Remote Access, {OFF}
  :value1:    Enable Local Login with UBNT Account, {OFF}
  :value2:    Remote Access Status, {DISABLED}

.. ubiquiti::  Remote Access Owner Setup
  :path:       ⚙ --> Remote Access --> Owner
  :value0:     Configured for, Not Configured

.. ubiquiti:: Remote Access Advanced Setup
  :path:      ⚙ --> Remote Access --> Advanced Options
  :value0:    Report Errors to Ubiquiti, ☐

.. ubiquiti:: Site Configuration
  :path:      ⚙ --> Site --> Site Configuration
  :value0:    Site Name, {SITE}
  :value1:    Country, {COUNTRY}
  :value2:    Timezone, {TZ}

.. ubiquiti:: Service Configuration
  :path:      ⚙ --> Site --> Services
  :value0:    ☐, Advanced Features
  :value1:    ☑, Automatically upgrade AP firmware
  :value2:    ☐, Enable status LED
  :value3:    ☐, Enable alert emails
  :value4:    ☐, Enable periodic speed test every
  :value5:    ☑, Enable connectivity monitor and wireless uplink
  :value6:    ☑, Default gateway
  :value7:    ☐, Enable remote Syslog server
  :value8:    ☐, Enable Netconsole logging server

  .. warning::
    Alerts and advanced logging disabled for initial setup, change these after
    finishing configuration.

.. ubiquiti:: Provider Capabilities
  :path:    ⚙ --> Site --> Provider Capabilities
  :value0:       Download, 1 Gbps
  :value1:       Upload, 1 Gpbs

  .. warning::
    Upload/Download settings should be reflective of your Internet connection
    for proper scaling of graphing data. It is *not* a throttle.

.. ubiquiti:: Device Authentication
  :path:      ⚙ --> Site --> Device Authentication
  :value0:    ☑, Enable SSH Authentication
  :value1:    Username, {USER}
  :value2:    Password, {PASS}

Apply changes.

VLAN Configuration
******************
Add all VLANS using the :ref:`VLAN Table <vlan-table>`.

.. ubiquiti:: Default LAN Network
  :path:    ⚙ --> Networks --> LAN
  :value0:       ☑, Corporate
  :value1:       ☑, LAN
  :value2:       Gateway/Subnet, 10.1.1.1/24
  :value3:       Domain Name, {DOMAIN}
  :value4:       › ☐, Enable IGMP Snooping
  :value5:       DHCP Server, {NONE}
  :value6:       › ☐, Enable DHCP gaurding
  :value7:       › ☐, Enable UPnP LAN
  :value8:       IPv6 Interface Type, {NONE}

  .. warning::
    This will be the default network when new devices are discovered before
    they are adopted. This is also the untagged :term:`Management VLAN`
    network. Configure with :term:`Management VLAN` settings.

.. ubiquiti:: Create All VLAN Networks
  :path:      ⚙ --> Networks --> Create New Network
  :value0:    Name, Wired
  :value1:    ☑, VLAN Only
  :value2:    VLAN, 2

  .. note::
    Add all VLANS using the :ref:`VLAN Table <vlan-table>`. :term:`Management
    VLAN` is not explicitly defined as a VLAN -- untagged traffic coming into
    *eth0* IS management traffic.

Add Trunk Port Profiles
***********************
.. ubiquiti:: Add AP Wireless Trunk Port Profiles
  :path:      ⚙ -->
              Profiles -->
              Switch Ports -->
              Add New Port Profile -->
              Create New Switch Port Profile
  :value0:    Profile Name, trunk-wifi
  :value1:    › POE, PoE/PoE+
  :value2:    Networks/VLANs,
  :value3:    › Native Network, LAN
  :value4:    › Tagged Networks, wifi
  :value5:    › Voice Network, {NONE}

.. ubiquiti:: Add Wired Trunk Port Profiles
  :path:      ⚙ -->
              Profiles -->
              Switch Ports -->
              Add New Port Profile -->
              Create New Switch Port Profile
  :value0:    Profile Name, trunk-wired
  :value1:    › POE, {OFF}
  :value2:    Networks/VLANs,
  :value3:    › Native Network, LAN
  :value4:    › Tagged Networks, wifi wired
  :value5:    › Voice Network, {NONE}

.. ubiquiti:: Add Server Trunk Port Profiles
  :path:      ⚙ -->
              Profiles -->
              Switch Ports -->
              Add New Port Profile -->
              Create New Switch Port Profile
  :value0:    Profile Name, trunk-server
  :value1:    › POE, {OFF}
  :value2:    Networks/VLANs,
  :value3:    › Native Network, LAN
  :value4:    › Tagged Networks, server infrastructure
  :value5:    › Voice Network, {NONE}

.. rubric:: References

#. `Using VLANs with Unifi Wireless Routing <https://help.ui.com/hc/en-us/articles/219654087-UniFi-Using-VLANs-with-UniFi-Wireless-Routing-Switching-Hardware>`_
#. `Tagging and Untagging Traffic <https://help.ui.com/hc/en-us/articles/204962144#1>`_
#. `Lessons Learned from Deploying a Unifi Network <https://www.douglasisaksson.com/lessons-learned-from-deploying-a-unifi-network-at-home/>`_
#. `Unifi Switch 8 and VLANs <https://www.youtube.com/watch?v=JblnjsnJNJU>`_

.. _Unifi Controller: https://www.ui.com/download/?q=controller
.. _super admin: https://help.ui.com/hc/en-us/articles/204909374-UniFi-Accounts-and-Passwords-for-Controller-Cloud-Key-and-Other-Devices 
.. _unifi controller DHCP option: https://help.ui.com/hc/en-us/articles/204909754-UniFi-Device-Adoption-Methods-for-Remote-UniFi-Controllers#7
.. _telemetry: https://community.ui.com/questions/Update-UniFi-Phone-Home-Performance-Data-Collection/f84a71c9-0b81-4d69-a3b3-45640aba1c8b
