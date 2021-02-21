.. _w10-20h2-standalone-onedrive:

OneDrive
########
OneDrive is Microsoft Cloud storage built into Windows 10 and automatically
enabled by default. It is the default location for all files; disabled this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Unlink OneDrive before disabling
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  If you have signed into OneDrive on this machine, OneDrive **should** be
  unlinked before proceeding. Data will still be on https://onedrive.live.com.

  .. ggui:: Unlink OneDrive
    :key_title: taskbar --> RMB OneDrive --> More --> Settings --> Account
    :option:  Unlink this PC,
              Unlink account
    :setting: LMB,
              LMB
    :no_section:
    :no_caption:
    :no_launch:

  `Reference <https://support.microsoft.com/en-us/office/turn-off-disable-or-uninstall-onedrive-f32a17ce-3336-40fe-9c38-6efb09f944b0?ui=en-us&rs=en-us&ad=us>`__
  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive>`__

.. dropdown:: Remove OneDrive from Windows Explorer
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  OneDrive is integrated with Windows Explorer by default.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Remove OneDrive from Windows Explorer
      :key_title: HKEY_CLASSES_ROOT\\CLSID\\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
      :names:     System.IsPinnedToNameSpaceTree
      :types:     DWORD
      :data:      0
      :admin:
      :no_section:
      :no_caption:

  `Reference <https://www.techjunkie.com/remove-onedrive-file-explorer-sidebar-windows-10/>`__
  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive>`__

.. dropdown:: Disable OneDrive from storing files
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows updates may re-enable this task.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable OneDrive from storing files
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  OneDrive -->
                  Prevent the usage of OneDrive for file storage
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: Scheduled Tasks
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wtschedule:: Disable OneDrive schedule update task
      :key_title:   OneDrive Standalone Update Task v2
      :option:      Task
      :setting:     Disabled
      :no_section:
      :no_caption:

  `Reference <https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.OneDrive::PreventOnedriveFileSync>`__
  `Reference <https://docs.microsoft.com/en-us/onedrive/use-group-policy#computer-configuration-policies>`__
  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive>`__

.. dropdown:: Remove OneDrive
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  OneDrive may be removed manually via the GUI once disabled.

  .. code-block:: powershell
    :caption: Remove OneDrive (powershell as admin).

    taskkill /F /IM OneDrive.exe
    %SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall

  Reboot.

  `Reference <https://support.office.com/en-us/article/turn-off-disable-or-uninstall-onedrive-f32a17ce-3336-40fe-9c38-6efb09f944b0?ui=en-US&rs=en-US&ad=US>`__
  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive>`__

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Diagnostic data services endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  .. gtable:: Diagnostic data services
    :header: Service,
             Endpoint
    :c0:     OneDrive app for Windows 10,
             ›
    :c1:     https://vortex.data.microsoft.com/collect/v1,
             vortex.data.microsoft.com/collect/v1
    :no_key_title:
    :no_section:
    :no_caption:
    :no_launch:

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
