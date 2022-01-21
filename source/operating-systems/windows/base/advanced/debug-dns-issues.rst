.. _wbase-specific-windows-fixes-debug-dns-issues:

Debug DNS Issues
################
Windows 10 aggressively caches DNS with a DNS caching service and can sometimes
lead to invalid results. First flush resolver caches and test.

.. code-block:: powershell
  :caption: powershell

  ipconfig /flushdns
  Clear-DnsClientCache

If that does not work, disabling the DNS caching service can be used. **Cannot**
be disabled via ``services.msc``.

.. regedit:: Disable DNS caching service
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache
  :value0:   Start, {DWORD}, 4
  :update:   2021-02-19

After resolving, re-enable the caching service and **Reboot**.

.. regedit:: Enable DNS caching service
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Dnscache
  :value0:   Start, {DWORD}, 2
  :update:   2021-02-19

`Reference <https://wintechlab.com/enable-disable-dns-client-service/>`__
