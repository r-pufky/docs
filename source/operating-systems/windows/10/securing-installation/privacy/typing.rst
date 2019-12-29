.. _windows-10-reasonable-privacy-typing:

Ink & Typing Personalization
############################
:cmdmenu:`⌘ + r --> ms-settings:privacy-speechtyping`

.. rubric:: Getting to know you

.. wregedit:: Disable typing history via Registry
  :key_title: HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization
  :names:     RestrictImplicitTextCollection,
              RestrictImplicitInkCollection
  :types:     DWORD,
              DWORD
  :data:      1,
              1
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.

.. rubric:: Rreferences

#. `General Inking & Typing Personalization Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing>`_