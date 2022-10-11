.. _service-crashplan-network:

Network
#######
All connections are done through SSH X11 forwarding to host.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

PVE Container Configuration
***************************
Only required for **LXC/KVM** hosts. PVE will try to forward to own displays if
``X11UseLocalhost yes`` is enabled for containers (lxc/kvm).

.. code-block:: bash
  :caption: **0664 root root** ``/etc/ssh/sshd_config``

  X11UseLocalhost no

`Reference <https://superuser.com/questions/806637/xauth-not-creating-xauthority-file>`__

Windows X11
***********
Configure :ref:`apps-putty`, :ref:`apps-putty-x-windows` and set these
settings.

.. gui::   Xlaunch (Xserver for Windows)
  :path:   ⌘ --> xlaunch
  :value0: ☑, Multiple windows
  :value1: Diplay number, -1
  :value2: ☑, Start no client
  :value3: ☑, Clipboard
  :value4: › ☑, primary selection
  :value5: ☑, Native opengl
  :update: 2022-10-08

.. gui::   Putty
  :path:   ⌘ --> putty --> connection --> ssh --> x11
  :value0: ☑, Enable x11 forwarding
  :value1: X display location, localhost:0.0
  :value2: ☑, MIT-Magic-Cookie-1
  :update: 2022-10-08

.. code-block:: bash
  :caption: Connect to host and launch crashplan.

  /usr/local/crashplan/bin/desktop.sh

.. warning::
  Read :ref:`service-crashplan-basic-configuration-backup-set` to adopt
  existing backup sets without losing data.

Linux
*****
No configuration required. Just xserver running.

.. code-block:: bash
  :caption:  to host and launch crashplan.

  ssh -X {USER}@{HOST}
  /usr/local/crashplan/bin/desktop.sh

.. warning::
  Read :ref:`service-crashplan-basic-configuration-backup-set` to adopt
  existing backup sets without losing data.