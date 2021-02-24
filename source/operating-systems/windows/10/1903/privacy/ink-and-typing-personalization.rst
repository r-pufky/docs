.. _w10-1903-reasonable-privacy-ink-and-typing-personalization:

Ink & Typing Personalization
############################
:cmdmenu:`⌘ + r --> ms-settings:privacy-speechtyping`

.. regedit:: Disable typing history
  :path:     HKEY_CURRENT_USER\Software\Microsoft\InputPersonalization
  :value0:   RestrictImplicitTextCollection, {DWORD}, 1
  :value1:   RestrictImplicitInkCollection,  {DWORD}, 1
  :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1821-inking--typing
  :update:   2021-02-19
