.. _printing-brother-mfcl2750dw-windows:

Windows Setup
#############
Minimal installation to prevent software bloat. Downloads avaialable at the
`Support Site`_.

Ensure printer is configured first. See
:ref:`printing-brother-mfcl2750dw-config`.

.. _printing-brother-mfcl2750dw-windows-manual-install:

Manual Install
**************
Recommended. This will install the printer/scanner via the print management
console using only drivers and basic scanning software. Also applies to adding
printer across subnets. Requires SNMP and WebServices to be enabled.

.. gui:: Enable Internet Printing Client
  :nav:    ⌘ --> settings --> manage optional features -->
           more windows features
  :path:   print and document services
  :value0: ☑, Internet Printing Client
  :ref:    https://docs.microsoft.com/en-us/troubleshoot/windows-client/printing/cannot-install-secure-web-services-on-devices>
  :update: 2021-01-09

.. gui:: Add Printer
  :nav:    ⌘ --> run --> PrintManagement.msc
  :path:   print servers --> (local) --> printers --> add printer -->
           add a tcp/ip or web services printer by ip address or hostname
  :value0: Type of device, web services printer
  :value1: Host name or IP address, http://{IP}/WebServices/Device
  :ref:    https://docs.microsoft.com/en-us/troubleshoot/windows-client/printing/cannot-install-secure-web-services-on-devices>
  :update: 2021-01-09

.. gui:: Update Driver
  :nav:    ⌘ --> run --> PrintManagement.msc
  :path:   print servers --> (local) --> printers --> Brother --> RMB -->
           properties -> advanced -> new driver
  :value0: Driver, Have Disk
  :value1:     › , {EXTRACTED DRIVER LOCATION}
  :ref:    https://docs.microsoft.com/en-us/troubleshoot/windows-client/printing/cannot-install-secure-web-services-on-devices>
  :update: 2021-01-09

  Download and extract the **Printer Driver & Scanner Driver for Local
  Connection** from the `Support Site`_.

.. gui:: Remove Generic Driver
  :nav:    ⌘ --> run --> PrintManagement.msc
  :path:   print servers --> (local) --> drivers -->
           Brother Laser Type1 Class Driver --> RMB --> Delete
  :value0:  , {DELETE}
  :update: 2021-01-09

iPrint&Scan
===========
Enables all scanning options when using the scanning feature.

Download and extract **Brother iPrint&Scan** from the `Support Site`_. Install.

.. gui:: Disable Analytics Reporting
  :nav:    ⌘ --> iprint & scan
  :path:   settings -> product information
  :value0: ☐, send information
  :value1: ☐, check for software updates
  :update: 2021-01-09

  Read the disable wording carefully.

.. gui:: Disable Report Sharing
  :nav:    ⌘ --> iprint & scan --> select your machine --> Brother Analytics
  :path:   configure
  :value0:  , {DISABLE}
  :update: 2021-01-09

  Read the disable wording carefully.

Full Install
************
**Not** Recommended. Installs all additional software and requires SNMP with
the device on the local subnet to install correctly. WebServices must be
enabled.

.. dropdown:: Full Install
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. danger::
    Enabling SNMP on the printer exposes vulnerabilites which must be mitigated.
    Allow only access to devices that need it.

    :cmdmenu:`network --> network --> protocol --> SNMP --> Advanced Settings`

    * ☑ SNMPv3 read-write access and v1/v2c read-only access
    * User Name: {RANDOM HASH}
    * Key Type: {PASS}
    * Authentication Method: SHA1
    * Authentication Password: {16 CHARACTERS}
    * Privacy Password: {16 CHARACTERS}
    * Context Name: authNoPriv

    `Reference <https://www.webnms.com/simulator/help/sim_network/netsim_conf_snmpv3.html>`__

  Download and extract **Full Driver & Software Package** from the `Support
  Site`_. Run:

  * full software/driver package
  * ethernet
  * select machine (requires snmpv1/2 enabled)
  * CUSTOM installation

    * printer driver
    * scanner driver
    * ps driver
    * brother iprint&scan without desktop icon
  * additional software

    * do **not** install paperport
  * additional options

    * Brother Product Research and Support Program

      * customize: disable

  Printer should be autodetected via
  :cmdmenu:`⌘ --> settings --> printers --> add a printer or scanner` or Manual
  install, see :ref:`printing-brother-mfcl2750dw-windows-manual-install`.

ControlCenter4
**************
Advanced post-scanning options. Generally this can be done by other
applications. **Not** recommended.

.. dropdown:: ControlCenter4 Install
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Download and extract **Full Driver & Software Package** and **controlcenter4
  updater tool** from the `Support Site`_. Cancel the installations.

  * Manually install from extracted package: ``Msi/ControlCenter4.msi``
  * Run the ControlCenter4 Updater
  * Reboot (required to launch.)
  * :cmdmenu:`⌘ --> taskbar --> controlcenter4 --> RMB --> preferences`

    * ☑ start ControlCenter on computer startup

      This needs to be left enabled otherwise cannot restart; manage through
      TaskManager, below.
    * ☐ Send Information
  * :cmdmenu:`⌘ --> taskbar --> TaskManager --> Startup`

    * Disable ``TwDsUiLaunch.exe``
    * Disable ``ControlCenter Launcher``

    .. note::
      Renable and reboot when control center needs to be used.

  .. note::
    Send information may be re-prompted on first start. Disable it.

.. _printing-brother-mfcl2750dw-windows-validate-install:

Validate Install
****************
* :cmdmenu:`⌘ --> settings --> printers --> Brother MFC-L2750DW --> manage`.
  Both printer and scanner will be listed in the dropdown.

* :cmdmenu:`manage --> printer (dropdown) --> printer properties` should open a
  window with a blue 'Brother' bar.
* :cmdmenu:`⌘ --> iprint & scan --> scan --> 1200dpi` properly installed
  scanner will allow > 300dpi scanning, and show **all settings**.

Complete Uninstall
******************
Use the following to clean a system if brother utilities were installed and
need to be removed.

.. dropdown:: Full Uninstall
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  * :cmdmenu:`⌘ --> RMB --> device manager` (remove driver with uninstall):

    * printer: brother*
    * imaging devices: brother*
    * WSD Print device: brother*
  * :cmdmenu:`⌘ --> settings -> printers` (remove if existing):

    * brother
    * paperport image printer
  * :cmdmenu:`⌘ --> settings -> programs` (uninstall):

    * nuance*
    * brother*
    * paperport*
    * httptousb*
    * (look at related installs on the same date)
  * :cmdmenu:`taskbar --> RMB --> Task Manager`

    * PaperPort Scan Manager
    * Nuance Imaging Scanner TWAIN Client
    * PDFProFiltSrvPP (PDFPro IFilter Service)
    * Brother MFC Windows Software Standard Debug Log Recieve Process
    * agent.exe
    * softwareupdatenotificationservice
  * Run Uninstall Tools from the `Support Site`_.
  * Delete:

    * ``c:\Program Files (x86)\brother``

      .. note::
        If you cannot delete ``BrBFLogl.dll``, ensure it isn't in use with
        `Process Explorer`_, :cmdmenu:`Find --> Find Handle or DLL` and search
        for it.

        .. code-block:: powershell
          :caption: Force unload dll (cmd as admin)

          Regsvr32 /u /s c:\Program Files (x86)\brother\AppLogLib\BrBFLogl.dll

        Then delete normally.
    * ``c:\Program Files (x86)\controlcenter4*``
    * ``c:\Program Files (x86)\browny02``

  * :cmdmenu:`⌘ --> run --> cleanmgr.exe (Disk Cleanup)` clean cached files

    * cleanup system files
    * clean all files
  * :cmdmenu:`⌘ --> run --> PrintManagement.msc --> print servers --> (local) --> drivers --> Brother* --> RMB --> Delete`
  * Reboot to ensure memory is unloaded

.. _Support Site: https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfcl2750dw_us_eu_as
.. _Process Explorer: https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer