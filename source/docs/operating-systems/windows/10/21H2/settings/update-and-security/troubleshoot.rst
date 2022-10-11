.. _w10-21h2-settings-update-and-security-troubleshoot:

Troubleshoot
############
.. regedit:: Don't run any troubleshooters
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsMitigation
  :value0:   UserPreference, {DWORD}, 1
  :ref:      https://www.tenforums.com/tutorials/113553-turn-off-automatic-recommended-troubleshooting-windows-10-a.html
  :update:   2021-02-19
  :open:

  Requires diagnostic data to be uploaded to Microsoft.
