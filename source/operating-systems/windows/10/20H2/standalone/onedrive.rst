.. _w10-20h2-standalone-onedrive:

OneDrive
########
OneDrive is Microsoft Cloud storage built into Windows 10 and automatically
enabled by default. It is the default location for all files; disabled this.

.. danger::
  After every major windows update, verify these settings.

.. gui::   Unlink OneDrive before disabling
  :path:   taskbar --> RMB OneDrive --> More --> Settings --> Account
  :value0: Unlink this PC, {LMB}
  :value1: Unlink account, {LMB}
  :ref:    https://support.microsoft.com/en-us/office/turn-off-disable-or-uninstall-onedrive-f32a17ce-3336-40fe-9c38-6efb09f944b0?ui=en-us&rs=en-us&ad=us,
           https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive
  :update: 2021-02-19

  If you have signed into OneDrive on this machine, OneDrive **should** be
  unlinked before proceeding. Data will still be on https://onedrive.live.com.

.. regedit:: Remove OneDrive from Windows Explorer
  :path:     HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}
  :value0:   System.IsPinnedToNameSpaceTree, {DWORD}, 0
  :ref:      https://www.techjunkie.com/remove-onedrive-file-explorer-sidebar-windows-10/,
             https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive
  :update:   2021-02-19

  OneDrive is integrated with Windows Explorer by default.

.. dropdown:: Disable OneDrive from storing files
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Windows updates may re-enable this task.

  .. gpo::    Disable OneDrive from storing files
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              OneDrive -->
              Prevent the usage of OneDrive for file storage
    :value0:  ☑, {ENABLED}
    :ref:     https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.OneDrive::PreventOnedriveFileSync,
              https://docs.microsoft.com/en-us/onedrive/use-group-policy#computer-configuration-policies,
              https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-onedrive
    :update:  2021-02-19
    :generic:
    :open:

  .. gui::    Disable OneDrive schedule update task
    :label:   Task Scheduler
    :nav:     ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:    OneDrive Standalone Update Task v2
    :value0:  Task, {DISABLED}
    :generic:
    :open:

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

  +-----------------------------+----------------------------------------------+
  | Service                     | Endpoint                                     |
  +=============================+==============================================+
  | OneDrive app for Windows 10 | https://vortex.data.microsoft.com/collect/v1 |
  +-----------------------------+----------------------------------------------+
  | ›                           | vortex.data.microsoft.com/collect/v1         |
  +-----------------------------+----------------------------------------------+

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
