.. _windows-10-meltdown-spectre:

`Meltdown and Spectre Patch`_
#############################
Windows 10 will not automatically patch for meltdown and spectre due to
anti-virus software causing BSOD's. If you are running anti-virus software
ensure you are not affected by checking the `anti-virus compatibility list`_.

`InSpectre`_ can be used to validate patches are applied.

:term:`Registry`
****************
.. wregedit:: Meltdown and sepctre patch via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              QualityCompat
  :names:     cadca5fe-87d3-4b96-b7fb-a231484277cc
  :types:     DWORD
  :data:      0
  :admin:
  :no_section:

:download:`regedit script <source/enable-meltdown-spectre-update.reg>`.

Reboot.

.. _Meltdown and Spectre Patch: https://support.microsoft.com/en-us/help/4056892/windows-10-update-kb4056892
.. _anti-virus compatibility list: https://docs.google.com/spreadsheets/d/184wcDt9I9TUNFFbsAVLpzAtckQxYiuirADzf3cL42FQ/htmlview?usp=sharing&sle=true
.. _InSpectre: https://www.grc.com/inspectre.htm