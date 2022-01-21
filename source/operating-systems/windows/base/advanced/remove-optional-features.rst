.. _wbase-remove-optional-features:

Remove Optional Features
########################
Some optional components are installed by default and make no sense being
installed. Remove them.

Manually
********
:cmdmenu:`⌘ + r --> ms-settings: --> Apps  --> Manage optional features`

   * English (united states) retail demo content.
   * Neutral retail demo content (cortana demo).
   * News hub.
   * Microsoft Quick Assist.
   * Contact Support.

Powershell
**********
May be used to automate removal of known optional features.

.. code-block:: powershell
  :caption: List optional features (powershell as admin)

  Get-WindowsOptionalFeature -Online

.. code-block:: powershell
  :caption: Add optional feature (powershell as admin)

  Enable-WindowsOptionalFeature -FeatureName {NAME} -All -Online

.. code-block:: powershell
  :caption: Remove optional feature (powershell as admin)

  Disable-WindowsOptionalFeature FeatureName {NAME} -Online

Reboot may be required.

`Reference <https://www.tenforums.com/tutorials/7565-manage-optional-features-windows-10-a.html>`__
