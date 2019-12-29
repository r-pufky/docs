.. _windows-10-disable-restore:

Disable Restore Points
######################
All system changes trigger a backup of affect files before changes are applied;
this creeate a drastic performance hit

.. ggui:: Disable restore points for each drive
  :key_title: ⌘ + r -->
              systempropertiesprotection -->
              Protection Settings -->
              {DRIVE} -->
              Configure
  :option:    ☑,
              Max Usage,
              Delete all restore points for this drive
  :setting:   Disable system protection,
              0,
              Delete
  :no_section:
  :no_launch:

    .. note::
      Be sure to set this for each drive explicitly.