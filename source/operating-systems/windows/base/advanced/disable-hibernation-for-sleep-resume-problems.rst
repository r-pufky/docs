.. _wbase-specific-windows-fixes-disable-hibernation-for-sleep-resume-problems:

Disable Hibernation for Sleep Resume Problems
#############################################
If your system doesn't seem to be resuming from sleep properly (e.g. power is
on, but keyboard/mouse won't resume it), disable hibernation. This does affect
power consumption and probably shouldn't be used on laptops.

.. code-block:: powershell
  :caption: Disable hibernation (powershell as admin).

  powercfg /h off

`Reference <https://www.tenforums.com/general-support/5265-turn-off-wake-up-problems.html>`__
