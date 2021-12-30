.. _apps-chrome:

Chrome Configuration
####################
See :ref:`service-nginx-chrome-client-certificate` to setup auto selection of
client certificate for matched sites.

Block location tracking
***********************

.. code-block::
  :caption: ``chrome://settings/content/location``

  Ask before accessing (Recommended) = Disabled

.. code-block::
  :caption: ``chrome://settings/content/notifications``

  Ask before sending (Recommended) = Disabled

Disable Software Reporting
**************************

.. regedit:: Disable Chrome running software reporting tool.
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
  :value0:   ChromeCleanupEnabled, {DWORD}, 0
  :ref:      https://www.ghacks.net/2018/01/20/how-to-block-the-chrome-software-reporter-tool-software_reporter_tool-exe/
  :update:   2021-02-12
  :open:

.. regedit:: Disable reporting results to Google.
  :path:      HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
  :value0:    ChromeCleanupReportingEnabled, {DWORD}, 0
  :ref:      https://www.ghacks.net/2018/01/20/how-to-block-the-chrome-software-reporter-tool-software_reporter_tool-exe/
  :update:    2021-02-12
  :open:
