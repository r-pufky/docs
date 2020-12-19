.. _w10-1903-disable-error-reporting:

Disable Error Reporting
#######################
Errors encountered on your systems are automatically sent to Microsoft,
including related metadata. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable error reporting
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable error reporting policy
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting
      :names:     Disabled
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

    .. wregedit:: Disable error reporting
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting
      :names:     Disabled
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Windows Error Reporting
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Windows Error Reporting -->
                  Disable Windows Error Reporting
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. rubric:: References

#. `Error Reporting Group Policy <https://auditsquare.com/advisory/windows/error-reporting>`_
#. `Error Reporting Registry <https://github.com/adolfintel/Windows10-Privacy#turn-off-windows-error-reporting>`_
