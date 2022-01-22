.. _realtek-nahimic:

Realtek A-Volute (Nahimic)
##########################
Realtek has added A-Volute(Nahimic) services to the install package. These
generally automatically take over speaker and microphone settings to improve
'quality'. They are also added automatically via Microsoft auto updates based
on hardware detection, as well as through Dolby Atmos installation.

Disabling does **not** affect either realtek or dolby installs.

Nahimic behaves very much like a virus, automatically reinstalling itself and
running two processes to ensure it is always loaded; providing no value to the
end user.

Disabling
*********
If the realtek device is not being used, **disable it** in the BIOS. This will
prevent Microsoft from re-installing the software everytime windows update
runs.

.. dropdown:: Disable Nahimic Virtual Devices
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gui::   Disable A-Volute Nh3 Audio Effects Component
    :label:  Service
    :nav:    ⌘ + x --> Device Manager
    :path:   Software components --> A-Volute Nh3 Audio Effects Component
    :value0: RMB, Disable Device
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

  .. gui::   Disable Nahimic Mirroring Device
    :label:  Service
    :nav:    ⌘ + x --> Device Manager
    :path:   Sound, video and game controllers --> Nahimic Mirroring Device
    :value0: RMB, Disable Device
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

  .. gui::   Disable Sonic Studio Virtual Mixer
    :label:  Service
    :nav:    ⌘ + x --> Device Manager
    :path:   Sound, video and game controllers --> Sonic Studio Virtual Mixer
    :value0: RMB, Disable Device
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

.. dropdown:: Disable Nahimic Services
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gui::   Disable Nahimic Service
    :label:  Service
    :nav:    ⌘ --> services.msc
    :path:   Nahimic service --> General
    :value0:   Service name, NahimicService
    :value1:   Startup type, {DISABLED}
    :value2: Service status, {STOPPED}
    :ref: https://old.reddit.com/r/Amd/comments/koh9ca/turning_offdisabling_my_rgb_g_skill_trident_z_neo/
    :update: 2022-01-22

.. dropdown:: Prevent Nahimic Executables from Starting
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Prevent Nahimic Executables from Starting
    :path:    User Configuration -->
              Administrative Templates -->
              System -->
              Don't run specified Windows applications
    :value0:  ☑, {ENABLED}
    :value1:  List of disallowed applications, C:\Windows\System32\NahimicService.exe
    :value2:                                ›, C:\Windows\System32\NahimicSvc64.exe
    :value3:                                ›, C:\Windows\SysWOW64\NahimicSvc32.exe
    :value4:                                ›, C:\Windows\System32\NhNotifSys.exe
    :value5:                                ›, C:\Users\{USER}\AppData\Local\NhNotifSys\NhNotifSys.exe
    :value6:                                ›, C:\Users\{USER}\AppData\Local\NhNotifSys\sonicstudio\NhNotifSys.exe
    :ref:     https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
              https://appuals.com/how-to-remove-windows-defender-icon-on-windows-10/
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Nahimic Scheduled Tasks
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Scheduled tasks may not all exist.

  .. gui::   Disable NahimicSvc32Run
    :label:  Task Scheduler
    :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:   NahimicSvc32Run
    :value0: Task, {DISABLED}
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

  .. gui::   Disable NahimicSvc64Run
    :label:  Task Scheduler
    :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:   NahimicSvc64Run
    :value0: Task, {DISABLED}
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

  .. gui::   Disable NahimicTask32
    :label:  Task Scheduler
    :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:   NahimicTask32
    :value0: Task, {DISABLED}
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

  .. gui::   Disable NahimicTask64
    :label:  Task Scheduler
    :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:   NahimicTask64
    :value0: Task, {DISABLED}
    :ref:    https://old.reddit.com/r/MSI_Gaming/comments/ilys2o/nahimic_is_literal_malware_no_matter_how_you/
    :update: 2022-01-22

:ref:`wbase-remove-startup-items` related to this.

Delete files that have been placed in ``C:\Users\{USER}\AppData\Local\NhNotifSys*``.