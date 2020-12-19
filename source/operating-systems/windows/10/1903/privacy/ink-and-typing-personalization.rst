.. _w10-1903-reasonable-privacy-ink-and-typing-personalization:

Ink & Typing Personalization
############################
:cmdmenu:`⌘ + r --> ms-settings:privacy-speechtyping`

.. dropdown:: Getting to know you
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable typing history
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization
      :names:     RestrictImplicitTextCollection,
                  RestrictImplicitInkCollection
      :types:     DWORD,
                  DWORD
      :data:      1,
                  1
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `General Inking & Typing Personalization Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing>`_
