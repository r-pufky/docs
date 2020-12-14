.. _w10-1903-disable-error-reporting:

Disable Error Reporting
#######################
Errors encountered on your systems are automatically sent to Microsoft,
including related metadata. Disable this.

.. danger::
  After every major windows update, verify these settings.

:term:`Registry` Machine
************************
.. wregedit:: Disable error reporting policy via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting
  :names:     Disabled
  :types:     DWORD
  :data:      1
  :no_section:

.. wregedit:: Disable error reporting via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting
  :names:     Disabled
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`GPO` Computer
********************
.. wgpolicy:: Disable Windows Error Reporting via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Error Reporting -->
              Disable Windows Error Reporting
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. rubric:: References

#. `Error Reporting Group Policy <https://auditsquare.com/advisory/windows/error-reporting>`_
#. `Error Reporting Registry <https://github.com/adolfintel/Windows10-Privacy#turn-off-windows-error-reporting>`_
