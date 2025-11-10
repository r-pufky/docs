# Windows
Minimal installation to prevent software bloat. [Driver
Downloads](https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfcl2750dw_us_eu_as).

## Manual Install
Recommended. This will install the printer/scanner via the print management
console using only drivers and basic scanning software. Also applies to adding
printer across subnets. Requires **SNMP** and **WebServices** to be enabled.

### Enable Internet Printing Client
!!! example "⌘ ➔ Settings ➔ Manage Optional Features ➔ More Windows Features ➔ Print and Document Services"
    * Internet Printing Client: ✔

### Add Printer
!!! example "⌘ ➔ run ➔ PrintManagement.msc ➔ Print Servers ➔ (local) ➔ Printers ➔ Add Printer ➔ Add a TCP/IP or Web Services Printer by IP Address or Hostname"
    * Type of device: **web services printer**
    * Host name or IP address: **http://{IP}/WebServices/Device**

### Update Driver
!!! info
    Requires **Printer Driver & Scanner Driver for Local Connection** extracted.

!!! example "⌘ ➔ run ➔ PrintManagement.msc ➔ Print Servers ➔ (local) ➔ Printers ➔ Brother ➔ RMB ➔ Properties ➔ Advanced ➔ New Driver"
    * Driver: **Have Disk**


### Remove Generic Driver
!!! example "⌘ ➔ run ➔ PrintManagement.msc ➔ Print Servers ➔ (local) ➔ Drivers ➔ Brother Laser Type1 Class Driver ➔ RMB ➔ Delete"

Reference:

* https://docs.microsoft.com/en-us/troubleshoot/windows-client/printing/cannot-install-secure-web-services-on-devices

## iPrint & Scan
Enables all scanning options when using the scanning feature.
!!! info
    Requires **Brother iPrint&Scan** extracted.

### Disable Analytics Reporting
!!! example "⌘ ➔ iPrint & Scan ➔ Settings ➔ Product Information"
    * Send information: ✘
    * Check for software updates: ✘

    Read the disable wording carefully.

### Disable Report Sharing
!!! example "⌘ ➔ iPrint & Scan ➔ {PRINTER} ➔ Brother Analytics"
    * Configure: ✘

    Read the disable wording carefully.

## Full Install
!!! danger
    **Not** Recommended. Installs all additional software and requires SNMP
    with the device on the local subnet to install correctly. WebServices must
    be enabled.

    Enabling SNMP on the printer exposes vulnerabilities which must be mitigated.
    Allow only access to devices that need it.

!!! info
    Requires **Full Driver & Software Package**.

### Configure Printer
!!! example "Printer WebUI ➔ Network ➔ Protocol ➔ SNMP ➔ Advanced Settings"
    * SNMPv3 read-write access and v1/v2c read-only access: ✔
    * User Name: **{RANDOM HASH}**
    * Key Type: **{PASS}**
    * Authentication Method: **SHA1**
    * Authentication Password: **{16 CHARACTERS}**
    * Privacy Password: **{16 CHARACTERS}**
    * Context Name: **authNoPriv**

    Reference:

    * https://www.webnms.com/simulator/help/sim_network/netsim_conf_snmpv3.html

### Install Software
* Full software/driver package.
* Ethernet.
* Select machine (requires snmpv1/2 enabled).
* CUSTOM installation:
    * Printer Driver
    * Scanner Driver
    * PS Driver
    * Brother iPrint & Scan without desktop icon.
* Additional software:
    * do **not** install paperport.
* Additional options:
    * Brother Product Research and Support Program:
      * Customize: disable

### Add Printer
!!! example "⌘ ➔ Settings ➔ Printers ➔ Add a printer or scanner"
    Printer should be auto detected.

### ControlCenter4
Advanced post-scanning options. Generally this can be done by other
applications. **Not** recommended.

!!! info
    Requires **Full Driver & Software Package** and **ControlCenter4 updater
    tool**. Do not install.

1. Extract packages.
2. Manually install from extracted package: **Msi/ControlCenter4.msi**.
3. Run ControlCenter4 Updater.
4. Reboot (required to launch).

Set Preferences
!!! example "⌘ ➔ Taskbar ➔ ControlCenter4 ➔ RMB ➔ Preferences"
    * Start ControlCenter on computer startup: ✔

      This needs to be left enabled otherwise cannot restart - manage through
      TaskManager.

    * Send Information: ✘

Disable Auto launch Services
!!! example "⌘ ➔ Taskbar ➔ TaskManager ➔ Startup"
    * TwDsUiLaunch.exe: ✘
    * ControlCenter Launcher: ✘

    Re-nable and reboot when control center needs to be used.

### Validate Install
!!! example "⌘ ➔ Settings ➔ Printers ➔ Brother MFC-L2750DW ➔ manage"
    Both printer and scanner will be listed in the dropdown.

    printer (dropdown) ➔ printer properties: Should open a window with a blue
    Brother bar.

!!! example "⌘ ➔ iPrint & Scan ➔ Scan ➔ 1200dpi"
    Properly installed scanner will allow > 300dpi scanning and show **all
    settings**.

## Complete Uninstall
Use the following to clean a system if brother utilities were installed and
need to be removed.

!!! info
    Requires **Uninstall Tools** downloaded and run.

### Remove driver with uninstall
!!! example "⌘ ➔ RMB ➔ device Manager"
    * Printer: **brother***
    * Imaging Devices: **brother***
    * WSD Print Device: **brother***

### Remove Printers
!!! example "⌘ ➔ Settings -> Printers"
    * brother
    * paperport image printer

### Uninstall Programs
!!! example "⌘ ➔ settings -> Programs"
    * nuance*
    * brother*
    * paperport*
    * httptousb*
    * (look at related installs on the same date)

### Confirm Services Disabled / Removed
!!! example "Taskbar ➔ RMB ➔ Task Manager"
    * PaperPort Scan Manager
    * Nuance Imaging Scanner TWAIN Client
    * PDFProFiltSrvPP (PDFPro IFilter Service)
    * Brother MFC Windows Software Standard Debug Log Receive Process
    * agent.exe
    * softwareupdatenotificationservice

### Delete Files From Disk
!!! note
    If you cannot delete **BrBFLogl.dll**, ensure it isn't in use with Process
    Explorer (Find ➔ Find Handle or DLL) and search for it.

    Force unload dll
    ``` powershell
    # Force unload dll (run as administrator)
    Regsvr32 /u /s c:\Program Files (x86)\brother\AppLogLib\BrBFLogl.dll
    ```

    Then delete normally.

1. **c:\Program Files (x86)\brother**
2. **c:\Program Files (x86)\ControlCenter4***
3. **c:\Program Files (x86)\browny02**
4. ⌘ ➔ run ➔ cleanmgr.exe (Disk Cleanup)
    * Cleanup system files.
    * Clean all files.
5. ⌘ ➔ run ➔ PrintManagement.msc ➔ Print Servers ➔ (local) ➔ Drivers ➔
   Brother* ➔ RMB ➔ Delete

Reboot to ensure memory is unloaded.
