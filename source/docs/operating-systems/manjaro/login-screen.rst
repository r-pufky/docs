.. _manajaro-kde-login-screen:

Login Screen (sddm)
###################
SDDM login screen may be a bit finicky during configuration. Applying changes
tend to overwrite custom background setup. Login screen should be configured
after all UI settings have been set.

Multiple Monitors
*****************
SDDM requires setup for multiple monitors to reflect the same configuration
when on the desktop.

.. code-block:: bash
  :caption: Get current desktop monitor configuration.

  xrandr | grep ' connected'

.. note::
  Output display format is {SCREEN WIDTH}x{SCREEN HEIGHT}x{X POS}x{Y POS}.

Set the display configuration for SDDM and ensure ``Xsetup`` is run on launch.

.. code-block:: bash
  :caption: **0755 root root** ``/usr/share/sddm/scripts/Xsetup``

  #!/bin/bash

  # 3:DP-0 connected 2560x1440+5120+0 (normal left inverted right x axis y axis) 597mm x 336mm
  # 17:DP-2 connected primary 2560x1440+2560+0 (normal left inverted right x axis y axis) 598mm x 336mm
  # 23:DP-4 connected 2560x1440+0+0 (normal left inverted right x axis y axis) 597mm x 336mm

  xrandr --output DP-4 --mode 2560x1440 --pos 0x0 --rotate normal \
         --output DP-2 --mode 2560x1440 --pos 2560x0 --rotate normal \
         --output DP-0 --mode 2560x1440 --pos 5120x0 --rotate normal

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sddm.conf``

  DisplayCommand=/usr/share/sddm/scripts/Xsetup

`Reference <https://blog.victormendonca.com/2018/06/29/how-to-fix-sddm-on-multiple-screens/>`__

SDDM configuration
******************
.. gui:: Login Screen
  :nav:    ⌘ --> system settings --> startup and shutdown
  :path:   login screen (sddm)
  :value0:            ☑, Breath
  :value1: › background, ``/usr/share/wallpapers/SafeLanding/contents/images/*.jpg``
  :update: 2021-01-07
  :open:

.. note::
  **apply plasma settings** after setting background and any other theme UI
  settings. This will apply the current UI settings (arc dark) to the Breeze
  login screen; this should match the **lockscreen**.
