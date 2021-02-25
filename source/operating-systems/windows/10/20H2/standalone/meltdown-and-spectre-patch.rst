.. _w10-20h2-meltdown-spectre:

Meltdown and Spectre Patch
##########################
Windows 10 will not automatically patch for meltdown and spectre due to
anti-virus software causing BSOD's. If you are running anti-virus software
ensure you are not affected by checking the `anti-virus compatibility list`_.

`InSpectre`_ can be used to validate patches are applied.

.. regedit:: Enable Meltdown and Spectre patching
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             QualityCompat
  :value0:   cadca5fe-87d3-4b96-b7fb-a231484277cc, {DWORD}, 0
  :ref:      https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
  :update:   2021-02-19
  :open:

  :download:`regedit script <source/enable-meltdown-spectre-update.reg>`.

  Reboot.

.. _anti-virus compatibility list: https://docs.google.com/spreadsheets/d/184wcDt9I9TUNFFbsAVLpzAtckQxYiuirADzf3cL42FQ/htmlview?usp=sharing&sle=true
.. _InSpectre: https://www.grc.com/inspectre.htm
