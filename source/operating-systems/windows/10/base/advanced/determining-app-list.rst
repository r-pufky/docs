.. _w10-determining-app-list:

Determining App List
####################
A specific list of apps can be denied/allowed as well as allowing user to choose
apps.

If the apps have been properly identified and denied, you will not be able to
re-enable them from the GUI.

.. dropdown:: Get App package family names
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Searching with the GUI name and ``AppPackage name`` usually returns the
  related package name. Use this `AppPackage Names list`_ can be use to find the
  general package (then determine the ``PackageFamilyName``).

  An example PackageFamilyName is ``Microsoft.MicrosoftEdge_8wekyb3d8bbwe``.

  .. code-block:: powershell
    :caption: Get App package family names (powershell)

    Get-AppPackage | Select Name,PackageFamilyName


.. dropdown:: Setting App List
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    
    Read the description for the :term:`GPO` in question for all options.

    The identified package family names are added in the ``Force deny`` section.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    
    A key needs to be made for each app to block. Valid values are ``Allow``
    and ``Deny``.

    :term:`GPO` policy settings can be found in the registry at
    ``HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy`` but
    are not modifiable.

    Base Registry location ``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore``.

    .. dropdown:: Example app privacy restriction
      :title: font-weight-bold
      :animate: fade-in

      .. wregedit:: Example app privacy restriction using ConsentStore
        :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                    CapabilityAccessManager\ConsentStore\microphone\
                    {PACKAGE FAMILY NAME}
        :names:     Value
        :types:     SZ
        :data:      Deny
        :no_section:
        :no_caption:

.. rubric:: References

#. `Registry App List Blocking Example <https://www.kapilarya.com/allow-prevent-apps-access-to-microphone-in-windows-10>`_

.. _AppPackage Names list: https://com-puterworks.com/remove_apps.html
