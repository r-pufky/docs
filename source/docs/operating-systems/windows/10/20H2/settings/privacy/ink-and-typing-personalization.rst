.. _w10-20h2-settings-privacy-ink-and-typing-personalization:

Ink & Typing Personalization
############################
:cmdmenu:`⌘ + r --> ms-settings:privacy-speechtyping`

Getting to know you
*******************
.. dropdown:: Disable When this is switched off your personal typing and inking
              dictionary will be cleared, but the standard dictionary will
              continue to provide typing suggestions and handwriting
              recognition.
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  .. gpo::    Disable Getting to know you inking and typing recognition
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Text Input -->
              Improve inking and typing recognition
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable Getting to know you automatic learning
    :path:    User Configuration -->
              Administrative Templates -->
              Control Panel -->
              Regional and Language Options -->
              Handwriting personalization -->
              Turn off automatic learning
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Getting to know you
    :path:     HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization
    :value0:   RestrictImplicitTextCollection, {DWORD}, 1
    :value1:    RestrictImplicitInkCollection, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing
    :update:   2021-02-19
    :generic:
    :open:
