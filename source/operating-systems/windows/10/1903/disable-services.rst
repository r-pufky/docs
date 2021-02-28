.. _w10-1903-disable-services:

Disable Services
################
These services either do user data tracking, or are unnecessary.

.. gui::   Disable razer game scanner Service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   Razer Game Scanner --> General
  :value0:   Service name, GameScannerService
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :update: 2021-02-19
  :open:
