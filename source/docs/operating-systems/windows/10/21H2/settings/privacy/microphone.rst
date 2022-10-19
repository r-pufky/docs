.. _w10-21h2-settings-privacy-microphone:

Microphone
##########
:cmdmenu:`⌘ + r --> ms-settings:privacy-microphone`

Leave Microphone enabled. See `1803 update breaks microphone`_.

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow apps to access your microphone
************************************
.. dropdown:: Allow apps to access your microphone
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  GPO policy allow defines desktop and store app access.

  .. gpo::    Enable apps access to your microphone
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              App Privacy -->
              Let Windows access the microphone
    :value0:  ☑, {ENABLED}
    :value1:  Default for all apps, User is in control
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#184-microphone
    :update:  2021-02-19
    :generic:
    :open:

.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
