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
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Getting to know you inking and typing recognition
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Text Input -->
                  Improve inking and typing recognition
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Disable Getting to know you automatic learning
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Control Panel -->
                  Regional and Language Options -->
                  Handwriting personalization -->
                  Turn off automatic learning
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Getting to know you
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization
      :names:     RestrictImplicitTextCollection,
                  RestrictImplicitInkCollection
      :types:     DWORD,
                  DWORD
      :data:      1,
                  1
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing>`__
