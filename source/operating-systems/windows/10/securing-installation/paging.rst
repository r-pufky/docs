.. _windows-10-disable-paging:

Disable Paging
##############
Systems with more than **8GB** memory should disable paging. This may need to be
re-enabled if certain programs rely on the paging file existing.

.. ggui:: Give priority to foreground applications
  :key_title: ⌘ + r -->
              systempropertiesadvanced -->
              Performance -->
              Settings -->
              Advanced -->
              Processor scheduling
  :option:    ☑
  :setting:   Programs
  :no_section:
  :no_launch:

.. ggui:: Disable paging files for all drives
  :key_title: ⌘ + r -->
              systempropertiesadvanced -->
              Performance -->
              Settings -->
              Advanced -->
              Virtual memory -->
              Change...
  :option:    ☑
  :setting:   No paging file
  :no_section:
  :no_launch:

    .. note::
      Be sure to set this for each drive explicitly.