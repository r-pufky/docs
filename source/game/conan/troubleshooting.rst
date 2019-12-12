.. _game-conan-troubleshooting:

Troubleshooting
###############

.. _game-conan-troubleshooting-space:

Failed to determine free disk space for ... error 75
****************************************************
This happens when the underlying data store cannot be queried for remaing qouta.

Explicitly set a quota for store or ignore. See `quota error`_.

.. _game-conan-troubleshooting-disk:

``0x0`` or disk write errors
****************************
The docker container does not have permissions to write updates to the data
mount.

.. code-block:: bash
  :caption: Explicitly set permissions for Conan Exiles files.

  chown -R conan:conan /data/server/ConanSandbox

.. _game-conan-troubleshooting-wine:

Wine Taking Long Time for First Start
*************************************
``winehq`` may potentially take ~5 minutes on first boot to launch, due to
blocking on boot events:

.. pull-quote::
  *0014:err:ole:get_local_server_stream Failed: 80004002*

.. pull-quote::
  *__wine_kernel_init boot event wait timed out*

This is a suspected issue with the GCC build toolchain, but has not been
resolved yet. See `GCC breaks 64bit wine`_ and `wait timeout`_.

Steam container should pre mitigate this, however, system updates could change
that. Letting the container run will resolve itself. See `manual update`_ for
container specific resolution.

.. _GCC breaks 64bit wine: https://bugs.winehq.org/show_bug.cgi?id=38653
.. _wait timeout: https://ubuntuforums.org/archive/index.php/t-1499348.html
.. _quota error: https://github.com/r-pufky/steam#failed-to-determine-free-disk-space-for--error-75
.. _manual update: https://github.com/r-pufky/steam#windows-wine-takes-5-minutes-to-launch-on-first-boot