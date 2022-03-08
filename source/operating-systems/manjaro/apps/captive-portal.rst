.. _manjaro-kde-apps-captive-portal:

Captive Portal
##############
Laptop devices using public wifi need to install a specific captive-portal
application to access public wifis requiring login or acceptance of terms.

Optional. Only needed for laptops.

.. code-block:: bash

  sudo pacman -Syu capnet-assist

Run captive portal login to present the advertised login page.

.. code-block:: bash

  io.elementary.capnet-assist

