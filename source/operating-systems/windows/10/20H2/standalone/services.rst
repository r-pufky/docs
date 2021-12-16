.. _w10-20h2-standalone-services:

Services
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

.. gui::   Disable ASUS Armoury Crate
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   Armoury Crate --> General
  :value0:   Service name, ARMOURYCRATEService
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
  :update: 2021-04-08

.. gui::   Disable ASUS Com Service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   ASUS Com Service --> General
  :value0:   Service name, asComSvc
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
  :update: 2021-04-08

.. gui::   Disable Asus Service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   asus --> General
  :value0:   Service name, asus
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
  :update: 2021-04-08

.. gui::   Disable AsusUpdateCheck Service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   AsusUpdateCheck --> General
  :value0:   Service name, AsusUpdateCheck
  :value1:   Startup type, {DISABLED}
  :value2: Service status, {STOPPED}
  :ref: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
  :update: 2021-04-08
