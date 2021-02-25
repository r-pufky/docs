.. _w10-20h2-standalone-resource-exhaustion:

Resource Exhaustion
###################
Automatic Resource Exhaustion Resolution will force close applications in use
when memory starts to fill up. Prevent Windows from closing your active Windows.

.. dropdown:: Disable automatic resource exhaustion Service
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. wservice:: Disable Diagnostic Service
    :key_title: Diagnostic Policy Service --> General
    :option:    Service name,
                Startup type,
                Service status
    :setting:   DPS,
                Disabled,
                Stopped
    :no_section:
    :no_caption:

.. gpo::   Disable automatic resource exhaustion
  :path:   Computer Configuration -->
           Administrative Templates -->
           System -->
           Troubleshooting and Diagnostics -->
           Windows Resource Exhaustion Detection and Resolution -->
           Configure Scenario Execution Level
  :value0: ☑, {DISABLED}
  :ref:    https://www.windows-security.org/f4aece067cb4976eb7a4f3add2fda30c/configure-scenario-execution-level
  :update: 2021-02-19

  This :term:`GPO` is not defined correctly using the GPO API. It must be set
  manually via the GUI or disabling the diagnostic service.
