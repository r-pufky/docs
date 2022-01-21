.. _w10-21h2-standalone-microsoft-defender:

Microsoft Defender
##################
.. dropdown:: Disable microsoft defender notification icon
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable microsoft defender notification icon
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Security -->
              Systray
    :value0:  Hide Windows Security Systray, {ENABLED}
    :ref:     https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

  .. gui::    Disable microsoft defender notification icon manager
    :label:   Task Manager
    :nav:     ⌘ --> Task Manager
    :path:    More Details --> Startup
    :value0:  Microsoft Defender notification icon, {DISABLED}
    :ref:     https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

Firewall
********
`Endpoints for telemetry`_ may change. Peridiocally verify these have not
changed. See references for additional documentation.

.. warning::
  These endpoints should be blocked or routed to a blackhole. See
  :ref:`service-pihole` and :ref:`networking-dnat-for-captive-dns`.

.. dropdown:: Connected User Experiences and Telemetry endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  Microsoft Defender Advanced Threat Protection is country specific and the
  prefix changes by country, e.g.: **de**.vortex-win.data.microsoft.com

  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | Release                                | Diagnostic Endpoint                | Functional Endpoint               | Settings Endpoint               |
  +========================================+====================================+===================================+=================================+
  | 1703 with 2018-09 cumulative update    | v10c.vortex-win.data.microsoft.com | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | 1803 without 2018-09 cumulative update | v10.events.data.microsoft.com      | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+
  | 1709 or earlier                        | v10.vortex-win.data.microsoft.com  | v20.vortex-win.data.microsoft.com | settings-win.data.microsoft.com |
  +----------------------------------------+------------------------------------+-----------------------------------+---------------------------------+

.. dropdown:: Diagnostic data services endpoints
  :container: + shadow
  :title: bg-info text-white font-weight-bold
  :animate: fade-in

  +-----------------------------------------------+-------------------------------+
  | Service                                       | Endpoint                      |
  +===============================================+===============================+
  | Microsoft Defender Advanced Threat Protection | https://wdcp.microsoft.com    |
  +-----------------------------------------------+-------------------------------+
  | ›                                             | https://wdcpalt.microsoft.com |
  +-----------------------------------------------+-------------------------------+

.. rubric:: References

#. `Configure Windows Diagnostic Data <https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization>`_
#. `Manage connections from Windows 10 to Microsoft Services <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services>`_
#. `Remove Microsoft Defender Telemetry <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-defender>`_

.. _Endpoints for telemetry: https://docs.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization#how-microsoft-handles-diagnostic-data
