.. _w10-20h2-settings-apps-apps-and-features:

Apps & features
###############
.. dropdown:: Choose where to get apps
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Allow install from anywhere.
    
  .. gpo::    Choose where to get apps
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Windows Defender SmartScreen -->
              Explorer -->
              Configure App Install Control
    :value0:  ☑, {ENABLED}
    :value1:  ›, Turn off app recommendations
    :ref:     https://www.tenforums.com/tutorials/78213-choose-where-apps-can-installed-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Choose where to get apps
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
               Explorer
    :value0:   AicEnabled, {SZ}, Anywhere
    :ref:      https://www.tenforums.com/tutorials/78213-choose-where-apps-can-installed-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
