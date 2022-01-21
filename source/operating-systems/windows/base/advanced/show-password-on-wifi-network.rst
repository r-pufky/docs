.. _wbase-specific-windows-fixes-show-password-on-wifi-network:

Show Password on Wifi Network
#############################
.. code-block:: powershell
  :caption: Dump wifi configuration including password (powershell as admin).

  netsh wlan show profile WiFi-name key=clear
