.. _w10-20h2-settings-phone-phone:

Phone
#####

.. dropdown:: Disable Add a phone
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Phones are easy vectors that can bring in outside threats. Do not pair.

  .. gpo::    Disable Add a phone
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Group Policy -->
              Phone-PC linking this device
    :value0:  ☑, {DISABLED}
    :ref:     https://www.windowscentral.com/how-disable-phone-pc-linking-feature-windows-10
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Add a phone
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
    :value0:   EnableMmx, {DWORD}, 0
    :ref:      https://www.windowscentral.com/how-disable-phone-pc-linking-feature-windows-10
    :update:   2021-02-19
    :generic:
    :open:

    ``EnableMMX`` is an unfortunate name, but correct.
