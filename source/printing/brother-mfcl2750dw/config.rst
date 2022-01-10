.. _printing-brother-mfcl2750dw-config:

Printer Configuration
#####################
Configuration is done through the webface to minimize bloatware installation on
any system.

Login using http(s)://{PRINTER} with admin account. Any section not listed is
left at defaults.

.. danger::
  Use defense in depth security practices and disable any printing services not
  being used. **Always** set non-default passwords and enforce restrictions on
  the device as well as firewall rules.

  It is assumed that the printer is on an isolated VLAN with no SNMP services
  with all Wifi disabled.

Administrator
*************
.. gui:: Login Password
  :nav:    administrator
  :path:   login password
  :value0: Password, {PASS}
  :update: 2021-01-09

  New password can be at least 25 characters with all alphanumerics and
  symbols. The default password is on the back of the machine or ``initpass``.

.. gui:: User Restriction Function
  :nav:    administrator
  :path:   user restriction function
  :value0: User Restriction Function, {OFF}
  :update: 2021-01-09

.. gui:: Setting Lock
  :nav:    administrator
  :path:   setting lock
  :value0: Setting Lock, {OFF}
  :update: 2021-01-09

.. gui:: Date & Time
  :nav:    administrator
  :path:   date & time
  :value0:    Clock Type, 24h Clock
  :value1:     Time Zone, {TZ}
  :value2: Auto Daylight, {ON}
  :value3:             ☑, Synchronize with SNTP server
  :update: 2021-01-09

.. gui:: Panel Logout Time
  :nav:    administrator
  :path:   panel logout time
  :value0: Logout, 60 seconds
  :update: 2021-01-09

.. gui:: Firmware Update
  :nav:    administrator
  :path:   firmware update
  :value0: Firmware Update, Check for new firmware
  :update: 2021-01-09

  Update to the latest firmware. If there is a new version apply and re-apply
  all settings.

.. gui:: Firmware Auto Check
  :nav:    administrator
  :path:   firmware auto check
  :value0: Firmware Auto Check, {OFF}
  :update: 2021-01-09

.. gui:: Stored Print Jobs
  :nav:    administrator
  :path:   stored print jobs
  :value0: Auto Delete, {ON}
  :value1:         Day, 0 days
  :value2:        Time, 0 hours
  :update: 2021-01-09

.. _printing-brother-mfcl2750dw-config-network:

Network
*******
Always remove unused services and apply filtering on device as well as network
equipment.

.. gui:: Interface
  :nav:    network --> network
  :path:   interface
  :value0: Interface, NC-9300h Ethernet 10/100BASE-TX
  :value1: Wi-fi Direct, {DISABLED}
  :update: 2021-01-09

.. gui:: Protocol
  :nav:     network --> network
  :path:    protocol
  :value0:  ☑, Web Based Management (Web Server)
  :value1:  ☐, SNMP
  :value2:  ☐, Remote Setup
  :value3:  ☐, LPD
  :value4:  ☐, Raw Port (jetdirect)
  :value5:  ☑, IPP
  :value6:  ☐, AirPrint
  :value7:  ☐, Mopria
  :value8:  ☑, Web Services (WSD)
  :value9:  ☐, Mobile printing for Windows
  :value10: ☐, Google Cloud Print
  :value11: ☐, Proxy
  :value12: ☑, Network Scan (network scanning device)
  :value13: ☐, PC Fax Receive
  :value14: ☐, SMTP
  :value15: ☐, FTP Server
  :value16: ☐, FTP Client
  :value17: ☐, TFTP
  :value18: ☐, CIFS
  :value19: ☐, mDNS
  :value20: ☐, LLMNR
  :value21: ☑, SNTP
  :update: 2021-01-09

  Must apply changes at this level. Changes applied within protocols (settings)
  will not save unsaved changes at this level.

.. gui:: Protocol (HTTP Server Settings)
  :nav:     network --> network --> protocol
  :path:    HTTP Server Settings
  :value0:  Select the Certificate, Preset
  :value1:    Web Based Management,  
  :value2:                     › ☑, {HTTPS}
  :value3:                     › ☐, {HTTP}
  :value4:                     IPP,  
  :value5:                     › ☑, {HTTPS}
  :value6:                     › ☐, {HTTP}
  :value7:                   › › ☐, Port 80
  :value8:                   › › ☐, Port 631
  :value9:            Web Services,  
  :value10:                    › ☑, {HTTP}
  :update: 2021-01-09

  All HTTP Server Settings links go to the same settings page.

.. gui:: Web Services Advanced Settings
  :nav:    network --> network --> protocol
  :path:   Web Services --> Advanced Settings
  :value0: Web Services Name, Brother MFC-L2750DW
  :update: 2021-01-09

.. gui:: SNTP Advanced Settings
  :nav:    network --> network --> protocol
  :path:   SNTP --> Advanced Settings
  :value0:            SNTP Server Method, Static
  :value1:   Primary SNTP Server Address, 0.pool.ntp.org
  :value2:      Primary SNTP Server Port, 123
  :value3: Secondary SNTP Server Address, 1.pool.ntp.org
  :value4:    Secondary SNTP Server Port, 123
  :value5:      Synchronization Interval, 24 hours
  :update: 2021-01-09

.. gui:: TCP/IP (Wired)
  :nav:    network --> wired
  :path:   tcp/ip (wired)
  :value0: Boot Method, {DHCP}
  :value1:          ☐, Enable APIPA
  :update: 2021-01-09

.. gui:: NetBIOS (Wired)
  :nav:    network --> wired
  :path:   NetBIOS (wired)
  :value0: NETBIOS/IP, ☑ Disabled
  :update: 2021-01-09

.. gui:: IPv6 (Wired)
  :nav:    network --> wired
  :path:   IPv6 (wired)
  :value0: IPv6, ☑ Disabled
  :update: 2021-01-09

.. gui:: Wireless (Personal)
  :nav:    network --> wireless
  :path:   wireless (personal)
  :value0: Wireless Network Name (SSID), {RANDOM HASH}
  :value1:        Authentication Method, WPA/WPA2-PSK
  :value2:              Encryption Mode, TKIP-AES
  :value3:                   Passphrase, {HASH 63 CHARACTERS}
  :update: 2021-01-09

  On committing settings prompt, do **not** enable wireless.

  Set security options even thought wireless is already disabled with
  :ref:`printing-brother-mfcl2750dw-config-network`.

.. gui:: IPv4 Filter
  :nav:    network --> security
  :path:   IPv4 Filter
  :value0: ☑, Use IP Filtering Service
  :value1: ☑, Accept the following Addresses
  :update: 2021-01-09

  Whitelist allowed IPs.

General
*******
Any section not listed is left at defaults.

.. gui:: Status
  :nav:    general
  :path:   status
  :value0: Automatic Refresh, {OFF}
  :value1:      Web Langauge, Auto
  :update: 2021-01-09

.. gui:: Sleep Time
  :nav:    general
  :path:   sleep time
  :value0: Sleep Time, 1 minute
  :update: 2021-01-09

.. gui:: Auto Power Off
  :nav:    general
  :path:   auto power off
  :value0: Auto Power Off, 1 hour
  :update: 2021-01-09

.. gui:: Volume
  :nav:    general
  :path:   volume
  :value0:    Ring, {OFF}
  :value1:    Beep, {OFF}
  :value2: Speaker, {OFF}
  :update: 2021-01-09

.. gui:: Panel
  :nav:    general
  :path:   panel
  :value0: Backlight, Dark
  :value1: Dim Timer, 30 secs
  :update: 2021-01-09

.. gui:: Replace Toner
  :nav:    general
  :path:   replace toner
  :value0: ☑, Stop
  :update: 2021-01-09

Print
*****
.. gui:: Print
  :nav:    print
  :path:   print
  :value0:      Eco Mode, {OFF}
  :value1:    Toner Save, {OFF}
  :value2:    Quiet Mode, {OFF}
  :value3: Continue Mode, Auto
  :update: 2021-01-09

.. gui:: Tray
  :nav:    print
  :path:   tray
  :value0: Check Size, {ON}
  :update: 2021-01-09

.. gui:: 2-sided
  :nav:    print
  :path:   2-sided
  :value0: 2-sided print, Long Edge
  :value1:  Single Image, 2-sided Feed
  :update: 2021-01-09

Scan
****
.. gui:: Scan File Name
  :nav:    scan
  :path:   scan file name
  :value0: File Name Style, Date_Name_Counter
  :value1: ☐, If a file with the same name already exists overwrite it.
  :value2: Date, yyyy/MM/dd
  :value3: time, {ON}
  :value4: Counter, Continous
  :update: 2021-01-09

.. gui:: Scan from PC
  :nav:    scan
  :path:   scan from pc
  :value0: Pull Scan, {ENABLED}
  :update: 2021-01-09

Common Endpoints
****************
May specify ports for all IP's as well.

Web Service: ``http://{HOST}/WebServices/Device``

IPP/IPPS: ``https://{IP}/ipp/``

IPP/IPPS (jetdirect compatibility): ``https://{IP}/ipp/port1/``

Specific endpoints as defined in :cmdmenu:`network --> network --> service`: ``https://{HOST}/{SERVICE}``
