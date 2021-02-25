.. _w10-20h2-standalone-error-reporting:

Error Reporting
###############
Errors encountered on your systems are automatically sent to Microsoft,
including related metadata. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable error reporting
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. gpo::    Disable Windows Error Reporting
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Error Reporting -->
              Disable Windows Error Reporting
    :value0:  ☑, {ENABLED}
    :ref:     https://auditsquare.com/advisory/windows/error-reporting
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable error reporting policy
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               Windows Error Reporting
    :value0:   Disabled, {DWORD}, 1
    :ref:      https://github.com/adolfintel/Windows10-Privacy#turn-off-windows-error-reporting
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable error reporting
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\
               Windows Error Reporting
    :value0:   Disabled, {DWORD}, 1
    :ref:      https://github.com/adolfintel/Windows10-Privacy#turn-off-windows-error-reporting
    :update:   2021-02-19
    :generic:
    :open:
