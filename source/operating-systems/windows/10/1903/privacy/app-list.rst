.. _w10-1903-privacy-app-list:

Determining App List
####################
A specific list of apps can be denied/allowed as well as allowing user to choose
apps.

If the apps have been properly identified and denied, you will not be able to
re-enable them from the GUI.

.. code-block:: powershell
  :caption: Get App package family names (powershell)

  Get-AppPackage | Select Name,PackageFamilyName

.. note::
  Searching with the GUI name and ``AppPackage name`` usually returns the
  related package name. Use this `AppPackage Names list`_ can be use to find the
  general package (then determine the ``PackageFamilyName``).

  An example PackageFamilyName is ``Microsoft.MicrosoftEdge_8wekyb3d8bbwe``.

.. rubric:: Setting App List for GPO

Read the description for the :term:`GPO` in question for all options.

The identified package family names are added in the ``Force deny`` section.

.. rubric:: Setting App List for Registry

``HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore``

.. wregedit:: Example app privacy restriction using ConsentStore via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\microphone\
              {PACKAGE FAMILY NAME}
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:

    .. note::
      A key needs to be made for each app to block. Valid values are ``Allow``
      and ``Deny``.

      :term:`GPO` policy settings can be found in the registry at
      ``HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy`` but
      are not modifiable.

.. rubric:: References

#. `Registry App List Blocking Example <https://www.kapilarya.com/allow-prevent-apps-access-to-microphone-in-windows-10>`_

.. _AppPackage Names list: https://com-puterworks.com/remove_apps.html