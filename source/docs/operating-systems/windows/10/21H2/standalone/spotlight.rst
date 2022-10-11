.. _w10-21h2-standalone-spotlight:

Spotlight
#########
Downloads pictures and advertisments to show while computer is locked. Disable
this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable all spotlight features
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable all spotlight features
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off all Windows spotlight features
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable third-party content in spotlight
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable third-party content in spotlight
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Do not suggest third-party content in Windows spotlight
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable all spotlight features on lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable all spotlight features on lock screen
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Configure Windows spotlight on lock screen
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable spotlight action center notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable spotlight action center notifications
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Action Center
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable spotlight settings notifications
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable spotlight notifications for settings via user GPO
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Cloud Content -->
              Turn off Windows Spotlight on Settings
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/configuration/windows-spotlight
    :update:  2021-02-19
    :generic:
    :open:
