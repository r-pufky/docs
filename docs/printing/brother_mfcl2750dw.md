# Brother MFC-L2750DW
[Driver Downloads](https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfcl2750dw_us_eu_as).

!!! danger "Use Defense in Depth"
    Disable any printing services not being used. **Always** set non-default
    passwords and enforce restrictions on the device as well as firewall rules.

    It is assumed that the printer is on an isolated VLAN with all Wifi
    disabled.

## Common Endpoints
Commonly used endpoints for networking printing.

 Service     | Address
-------------|------------------------------------------------------
 Web Service | **http://{HOST}/WebServices/Device**
 IPP/IPPS    | **https://{IP}/ipp/**
 IPP/IPPS    | **https://{IP}/ipp/port1/** (jetdirect compatibility)

Additional enabled endpoints found at: network ➔ network ➔ service.

## Printer Configuration
!!! tip
    Any section not listed is left at defaults. Save on each page before moving
    into sub pages or new tabs.

### Login to WebUI
Default login is typically on a label on the underside or backside of printer.
Common default passwords are **initpass** or **access**.

=== "Administrator"
    * Login Password:
        * Password: **{PASS}**
        !!! note
            New password can be at least 25 characters with all alphanumerics
            and symbols.

    * User Restriction Function: ✘
    * Setting Lock: ✘
    * Date & Time:
        * Clock Type: **24h Clock**
        * Time Zone: **{TZ}**
        * Auto Daylight: ✔
        * Synchronize with SNTP server: ✔
    * Panel Logout Time: **60 seconds**
    * Firmware Update: ✘
    * Firmware Auto Check: ✘

        !!! warning
            Do not update unless there are actual issues printing. Recent
            Brother firmware updates have disabled printers with third-party
            cartridges.

            Reference:

            * https://consumerrights.wiki/w/Brother_printers_causing_issues_with_third_party_inks
    * Stored Print Jobs:
        * Auto Delete: ✔
        * Day: **0 days**
        * Time: **0 hours**

=== "Network"
    * Interface:
        * Interface: **NC-9300h Ethernet 10/100BASE-TX**
        * Wi-fi Direct: ✘
    * Protocol:
        * Web Based Management (Web Server): ✔
            * HTTP Server Settings:
                * Select the Certificate: **Preset**
                * Web Based Management:  
                    * HTTPS: ✔
                    * HTTP: ✘
                * IPP:  
                    * HTTPS: ✔
                    * HTTP: ✘
                        * Port 80: ✘
                        * Port 631: ✘
                * Web Services:
                    * HTTP: ✔
        * SNMP: ✔
            * Advanced Settings:
                * SNMP Mode of Operation: **SNMPv3 read-write access and v1/v2c read-only access**
                * Username: **{USER}**
                * Key Type: **Password**
                * Authentication Method: **SHA1**
                * Authentication Password: **{PASS}**
                * Privacy Password: **{PASS}**
                * Context Name: **authNoPriv**
        * Remote Setup: ✘
        * LPD: ✘
        * Raw Port (jetdirect): ✘
        * IPP: ✔
        * AirPrint: ✘
        * Mopria: ✘
        * Web Services (WSD): ✔
            * Advanced Settings:
                * Web Services Name: **Brother MFC-L2750DW**
        * Mobile printing for Windows: ✘
        * Google Cloud Print: ✘
        * Proxy: ✘
        * Network Scan (network scanning device): ✔
        * PC Fax Receive: ✘
        * SMTP: ✘
        * FTP Server: ✘
        * FTP Client: ✘
        * TFTP: ✘
        * CIFS: ✘
        * mDNS: ✘
        * LLMNR: ✘
        * SNTP: ✔
            * Advanced Settings:
                * SNTP Server Method: **Static**
                * Primary SNTP Server Address: **0.pool.ntp.org**
                * Primary SNTP Server Port: **123**
                * Secondary SNTP Server Address: **1.pool.ntp.org**
                * Secondary SNTP Server Port: **123**
                * Synchronization Interval: **24 hours**

=== "Network (Wired)"
    * TCP/IP (wired):
        * Boot Method: **{DHCP}**
        * Enable APIPA: ✘
    * NetBIOS (Wired):
        * NETBIOS/IP: ✘
    * IPv6 (Wired):
        * IPv6: ✘
    * Wireless (Personal):
        * Wireless Network Name (SSID): **{RANDOM HASH}**
        * Authentication Method: **WPA/WPA2-PSK**
        * Encryption Mode: **TKIP-AES**
        * Passphrase: **{HASH 63 CHARACTERS}**

=== "Network (Security)"
    * IPv4 Filter:
        * Use IP Filtering Service: ✔
        * Accept the following Addresses: ✔ (Whitelist allowed IPs)

=== "General"
    * Status:
        * Automatic Refresh: ✘
        * Web Langauge: **Auto**
    * Sleep Time: **1 minute**
    * Auto Power Off: **1 hour**
    * Volume:
        * Ring: ✘
        * Beep: ✘
        * Speaker: ✘
    * Panel:
        * Backlight: **Dark**
        * Dim Timer: **30 secs**
    * Replace Toner:
        * Stop: ✔

=== "Print"
    * Eco Mode: ✘
    * Toner Save: ✘
    * Quiet Mode: ✘
    * Continue Mode: **Auto**
    * Tray:
        * Check Size: ✔
    * 2-sided:
        * 2-sided print: **Long Edge**
        * Single Image: **2-sided Feed**

=== "Scan"
    * Scan File Name:
        * File Name Style: **Date_Name_Counter**
        * If a file with the same name already exists overwrite it: ✘
        * Date: **yyyy/MM/dd**
        * time: ✔
        * Counter: **Continuous**
    * Scan from PC:
        * Pull Scan: ✔

!!! warning
    SNMP v1/2 must be enabled for scanner to be detected across
    subnets. Password limit is **16** characters.

    Password     | Context
    --------------|------------
     auth         | authNoPriv
     privacy      | authPriv
     context name | authNoPriv

    Reference:

    * https://www.webnms.com/simulator/help/sim_network/netsim_conf_snmpv3.html
