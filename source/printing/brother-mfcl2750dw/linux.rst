.. _printing-brother-mfcl2750dw-linux:

Linux Setup
###########
Manjaro drivers are provided via AUR, no need for brother specific downloads.
Debian and Redhat `packages are here. <https://support.brother.com/g/b/downloadtop.aspx?c=us&lang=en&prod=mfcl2750dw_us_eu_as>`__

Ensure printer is configured first. See
:ref:`printing-brother-mfcl2750dw-config`.

.. code-block:: bash
  :caption: Install printing packages

  pacman -Syu manjaro-printer xsane colord-sane
  pamac install brother-mfcl2750dw brscan4 brscan-skey

.. code-block:: bash
  :caption: Enable and force restart cups service

  sudo systemctl enable cups
  sudo systemctl restart --now cups

Add Printer
***********
Correct installation may be verified by checking the printing resolution
options, which should allow upto ``1200dpi``.

.. gui:: Add Printer
  :nav:    ⌘ --> system settings --> printers
  :path:   add printer
  :value0:                        Manual URI, https://{HOST}/ipp/port1
  :value1: › Choose the driver from the list, brother › MFCL2750DW for CUPS (en)
  :value2:                          › › Name, {PRINTER NAME}
  :value3:                          › › Name, {PRINTER DESCRIPTION}
  :value4:                             › › ☐, Share this printer
  :update: 2021-01-09

Add Scanner
***********
Scanner device is added using the brother utiltiy through xsane.

.. code-block:: bash
  :caption: Add brother scanner with xsane

  brsaneconfig4 -a name=scany model=MFC-L2750DW ip={IP}

.. note::
  Scanning uses TCXP port 54921. Max scanning resolution is 1200x1200dpi.

`Reference <https://support.brother.com/g/b/faqend.aspx?c=us&lang=en&prod=ads2700w_us_eu_as&faqid=faq00100466_500>`__

GIMP
====
GIMP can be used to scan and export images/pdfs as well. Preferred.

.. code-block:: bash
  :caption: Install GIMP

  pacman -Syu colord-sane xsane xsane-gimp gimp

Scanning may be verified by navigating to
:cmdmenu:`file --> create --> Xsane: Brother{#}:net{#};dev{#}` and acquring and
preview from the main xsane window that opens. This may pop under other windows
or on different monitors based on GIMP configuration.

gscan2pdf
=========
Utility for processing scans alternative to GIMP.

gscan will scan but sometimes it will appear 'black' in the preview. Just save
the pdf, it will be saved correctly.

.. code-block:: bash
  :caption: Install gscan2pdf

  pamac install gscan2pdf tesseract-data-eng

.. note::
  Install **all** dependencies for ``gscan2pdf``: djvulibre, gocr, xdg-utils,
  tesseract, cuneiform, pdftk, java-commons-lang.


Scanning may be verified by :cmdmenu:`ctrl + g` and refreshing devices, run a
scan and saving it.

Web Services Device (Scanner)
*****************************
Web services may be used to connect the scanner, which is the same method that
Windows uses.

.. code-block:: bash
  :caption: Install airscan (WSD)

  pacman -Syu sane-airscan

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sane.d/airscan.conf``

  'Brother MFC-L2750DW' = http://{IP}/WebServices/Device

`Reference <https://github.com/alexpevzner/sane-airscan>`__
