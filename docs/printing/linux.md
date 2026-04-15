# Linux

## Install Packages
=== "CachyOS"

    ``` bash
    # Printer
    pacman -S cups system-config-printer
    paru -S brother-mfc-l2750dw
    systemctl enable cups
    systemctl restart --now cups
    # Scanner
    paru -S brscan4 brscan-skey
    pacman -S sane colord-sane
    ```

    !!! example "⌘ ➔ Print Settings"
        * Add ➔ Enter URI:
            * Enter Device URI: **https://{HOST}/ipp/port1**
        * Select printer from database: **Brother** ➔ **MFCL2750DW for CUPS**
        * Describe Printer:
            * Short name: **{PRINTER NAME}**
            * Description: **{LONG NAME}**

=== "Debian"
    Debian [packages are here][a].

## Enable CUPS
``` bash
sudo systemctl enable cups
sudo systemctl restart --now cups
```

## Add Printer
!!! tip
    Verify correct installation by checking the printing resolution which
    should allow up to **1200dpi**.

!!! example "⌘ ➔ System Settings ➔ Printers ➔ Add Printer"
    * Manual URI: **https://{HOST}/ipp/port1**
        * Choose the driver from the list: **brother › MFCL2750DW for CUPS**
            * Name: **{PRINTER NAME}**
            * Name: **{PRINTER DESCRIPTION}**
            * Share this printer: ✘

## [Add Scanner][b]
Scanner device is added using the brother utility through xsane.

``` bash
# Scanning uses TCP port 54921. Max scanning resolution is 1200x1200dpi.
brsaneconfig4 -a name=scany model=MFC-L2750DW ip={IP}
```

## GIMP
GIMP can be used to scan and export images/PDF's as well. Preferred.

=== "CachyOS"
    ``` bash
    paru -S xsane gimp
    ```

=== "Debian"
    ``` bash
    apt install colord-sane sane-utils xsane gimp
    ```

!!! example "File ➔ Create ➔ Xsane: Brother{#}:net{#};dev{#}"
    Verify scanning by acquiring a preview from the main xsane window that
    opens. This may pop under other windows or on different monitors based on
    GIMP configuration.

## gscan2pdf
Utility for processing scans alternative to GIMP.

gscan will scan but sometimes it will appear 'black' in the preview. Just save
the PDF, it will be saved correctly.

=== "CachyOS"
    ``` bash
    # Install all dependencies.
    paru -S gscan2pdf tesseract-data-eng
    ```

=== "Debian"
    ``` bash
    apt install gscan2pdf
    ```

!!! example "ctrl + g"
    Verify scanning by refreshing devices, running a scan, and saving it.

## [Web Services Device (Scanner)][c]
Web services may be used to connect the scanner, which is the same method that
Windows uses.

=== "CachyOS"
    ``` bash
    paru -S sane-airscan
    ```

=== "Debian"
    ``` bash
    apt install sane-airscan
    ```

!!! abstract "/etc/sane.d/airscan.conf"
    0644 root:root

    ``` conf
    'Brother MFC-L2750DW' = http://{IP}/WebServices/Device
    ```

[a]: https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfcl2750dw_us_eu_as
[b]: https://support.brother.com/g/b/faqend.aspx?c=us&lang=en&prod=ads2700w_us_eu_as&faqid=faq00100466_500
[c]: https://github.com/alexpevzner/sane-airscan
