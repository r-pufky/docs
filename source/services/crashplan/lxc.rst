.. _service-crashplan-lxc:

Crashplan LXC/KVM/Baremetal Install
###################################
Crashplan Pro (For Small Business) is now the only consumer level option for
crashplan.

+-------------+---------------+------------------+
| Requirement | Recommended   | Reality          |
+=============+===============+==================+
| Memory      | 2GB           | 5GB              |
+-------------+---------------+------------------+
| CPU         | 1c@2Ghz 64bit | 2c/4t@3Ghz 64bit |
+-------------+---------------+------------------+
| Disk        | 2GB           | 6GB              |
+-------------+---------------+------------------+

Ports
*****
.. ports:: Crashplan Pro Ports
  :value0: 443,  {TCP}, {PUBLIC},    Code42 Console
  :value1: 4244, {TCP}, {LOCALHOST}, GUI to Service
  :value2: 4285, {TCP}, {PUBLIC},    Crashplan service (console)
  :value3: 4287, {TCP}, {PUBLIC},    Crashplan service (online)
  :ref:    https://support.code42.com/Small_Business/Get_Started/CrashPlan_for_Small_Business_requirements
  :update: 2021-07-27
  :open:

Files
*****
.. files:: Crashplan Pro Files
  :value0: /usr/local/crashplan/bin/desktop.sh, Crashplan GUI
  :value1: /usr/local/crashplan/bin/service.sh, Crashplan service init script
  :update: 2021-07-27
  :open:

Install
*******
Assumes :ref:`ubuntu` installed with a local user account, with backup data
mounted on ``/data``.

.. note::
  Crashplan should run as **root** to read all backup files. If using LXC
  containers, you must run as privileged (``unprivileged: 0``) or use ``idmap``
  to map all permissions to the container; otherwise mounted data will appear
  empty.

  Backup locations should be mounted ``read only`` if possible.

Dependencies
============
.. code-block:: bash
  :caption: Install crashplan service/GUI dependencies.

  apt install libgconf-2-4 libnss3 libasound2 xfce4

Increase inotify limits, see: :ref:`service-crashplan-troublshooting-inotify`.

SSHD Config
===========
Only required for LXC/KVM. By default PVE will try to forward X11 to own
displays if ``X11UserLocalhost yes`` is set.

`Reference <https://superuser.com/questions/806637/xauth-not-creating-xauthority-file>`__

.. code-block:: bash
  :caption: **0644 root root** ``/etc/ssh/sshd_config``

  X11UserLocalhost no

Install Service/GUI
===================
.. code-block:: bash
  :caption: Install crashplan service and reboot.

  wget https://download.code42.com/installs/agent/cloud/8.6.1/3/install/CrashPlanSmb_8.6.1_1525200006861_3_Linux.tgz
  tar xvf CrashPlanSmb_8.6.1_1525200006861_3_Linux.tgz
  cd code42-install
  ./install.sh -q
  reboot

.. note::
  Latest installer/URL: https://www.crashplanpro.com/app/#/console/app-downloads

  In practice, machines required a reboot before the service would properly
  function. ``-q`` installs accepting the defaults, which work in almost all
  cases.

Connect to GUI
**************
Done through SSH forwarding. See :ref:`apps-putty` for initial Putty, VcXsrv
install.

No specific Linux setup is required other than running an xserver.

Windows
=======
.. gui::   Xlaunch (Xserver for Windows)
  :path:   ⌘ --> xlaunch
  :value0: ☑, Multiple windows
  :value1: Diplay number, -1
  :value2: ☑, Start no client
  :value3: ☑, Clipboard
  :value4: › ☑, primary selection
  :value5: ☑, Native opengl
  :update: 2021-07-27

.. gui::   Putty
  :path:   ⌘ --> putty --> connection --> ssh --> x11
  :value0: ☑, Enable x11 forwarding
  :value1: X display location, localhost:0.0
  :value2: ☑, MIT-Magic-Cookie-1
  :update: 2021-07-27

.. code-block:: bash
  :caption: Open GUI client through ssh.

  ssh -X {USER}@{HOST}
  /usr/local/crashplan/bin/desktop.sh

Import existing backup configuration with :ref:`service-crashplan-adoption`.

`Reference <https://www.nicksherlock.com/2016/10/creating-a-crashplan-container-on-proxmox-to-back-up-your-files/>`__
