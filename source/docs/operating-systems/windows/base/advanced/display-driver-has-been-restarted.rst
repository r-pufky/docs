.. _wbase-specific-windows-fixes-display-driver-has-been-restarted:

Display Driver Has Been Restarted
#################################
Windows Vista+ has a feature called Timeout Detection and Recovery, which
detects if the GPU becomes unresponsive and restarts the driver. The GPU
running at 100% load can inadvertantly trip this reset the driver, causing
applications to crash. This can saftely be increased from the default *2
seconds* to a larger value with the only negative impact being that an actual
crashing driver will take that much longer to be reset. A bump to *8 to 10*
seconds is generally ok; it is **not** recommended to disable TDR entirely.

.. regedit:: Increase TDR delay to 8 seconds
  :path:     HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
  :value0:   TdrDelay, {DWORD}, 8
  :ref:      https://www.pugetsystems.com/labs/hpc/Working-around-TDR-in-Windows-for-a-better-GPU-computing-experience-777/
  :update:   2021-02-19
