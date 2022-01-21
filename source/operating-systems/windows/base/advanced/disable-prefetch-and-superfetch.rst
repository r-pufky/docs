.. _wbase-specific-windows-fixes-disable-prefetch-and-superfetch:

Disable Prefetch and Superfetch
###############################
This addresses 100% disk usage during idle in windows 10, even if you've already
disabled the superfetching service.

.. regedit:: Disable prefetch and superfetch regedit
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Session Manager\Memory Management\PrefetchParameters
  :value0:   EnablePrefetcher,   {DWORD}, 0
  :value1:   EnableSuperfetcher, {DWORD}, 0
  :ref:      https://www.thewindowsclub.com/disable-superfetch-prefetch-ssd
  :update:   2021-02-19
