.. _service-crashplan-troubleshooting:

Crashplan Troubleshooting
#########################

.. _service-crashplan-troublshooting-inotify:

Inotify Limits
**************
You may receive inotify warnings if the limit is low. Increase inotify max watch
limits on host so crashplan can watch all monitored files. 

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sysctl.conf``

  fs.inotify.max_user_watches=1048576

.. code-block:: bash
  :caption: Reload sysctl and reboot/restart crashplan:

  sysctl -p /etc/sysctl.conf
  reboot

`Reference <https://support.code42.com/CrashPlan/4/Troubleshooting/Linux_real-time_file_watching_errors>`__
