.. _service-steam-troubleshooting:

Troubleshooting
###############

.. _service-steam-troubleshooting-space:

Failed to determine free disk space for ... error 75
****************************************************
This happens when steamcmd cannot query the underlying data store remaining
qouta. Common with ZFS backed data stores. Either set an explicit qouta or
ignore it.

.. code-block::

  sudo zfs set quota=2T zpool1/games

.. _service-steam-troubleshooting-disk:

``0x0`` or disk write errors
****************************
No permissions to write updates to the data mount.

.. code-block:: bash
  :caption: Explicitly set permissions for Conan Exiles files.

  chown -R conan:conan /data/server/ConanSandbox

.. _service-steam-troubleshooting-wine:

Wine Taking Long Time for First Start
*************************************
``winehq`` may potentially take ~5 minutes on first boot to launch, due to
blocking on boot events:

.. pull-quote::
  *0014:err:ole:get_local_server_stream Failed: 80004002*

.. pull-quote::
  *__wine_kernel_init boot event wait timed out*

This is a suspected issue with the GCC build toolchain, but has not been
resolved yet. See `GCC breaks 64bit wine <https://bugs.winehq.org/show_bug.cgi?id=38653>`_
and `wait timeout <https://ubuntuforums.org/archive/index.php/t-1499348.html>`_.

Steam role should pre mitigate this, however, system updates could change that.
Letting it run will resolve itself.

.. code-block:: bash

  wineboot --update
  xvfb-run --autoservernum wineboot --update
