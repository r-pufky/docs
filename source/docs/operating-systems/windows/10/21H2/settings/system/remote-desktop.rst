.. _w10-21h2-settings-system-remote-desktop:

Remote Desktop
##############
.. dropdown:: Disable Remote Desktop
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  Remote desktop is easily exploited and should never be enabled.

  .. gpo::    Disable Remote Desktop
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Remote Desktop Services -->
              Remote Desktop Session Host -->
              Connections -->
              Allow users to connect remotely by using Remote Desktop Services
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/92433-enable-disable-remote-desktop-connections-windows-10-pc.html
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Require network authentication
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Remote Desktop Services -->
              Remote Desktop Session Host -->
              Security -->
              Require user authentication for remote connections by using network level authentication
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/92433-enable-disable-remote-desktop-connections-windows-10-pc.html
    :update:  2021-02-19
    :generic:
    :open:
