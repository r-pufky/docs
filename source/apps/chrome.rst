.. _apps-chrome:

Chrome Configuration
####################

Block location tracking
***********************

.. code-block::
  :caption: ``chrome://settings/content/location``

  Ask before accessing (Recommended) = Disabled

.. code-block::
  :caption: ``chrome://settings/content/notifications``

  Ask before sending (Recommended) = Disabled

`Disable Software Reporting`_
*****************************

.. wregedit:: Disable Chrome running software reporting tool.
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
  :names:     ChromeCleanupEnabled
  :types:     DWORD
  :data:      0
  :no_section:

.. wregedit:: Disable reporting results to Google.
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
  :names:     ChromeCleanupReportingEnabled
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

.. _Disable Software Reporting: https://www.ghacks.net/2018/01/20/how-to-block-the-chrome-software-reporter-tool-software_reporter_tool-exe/
