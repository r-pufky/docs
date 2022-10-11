.. _pve-gpu-passthru:

GPU Passthru
############
GPU's can be passed to containers or virtual machines; standard GPU's can be
passed to one instance, while professional/datacenter cards can be passed to
multiple devices at the same time. AMD cards will follow the same general
steps.

This requires the same driver version to be installed on the cluster node as
well as the LXC container.

PVE Cluster Node
****************
.. note::
  For Proxmox < ``7``; enable ``buster-backports main contrib non-free`` and
  use ``cgroup`` for lxc setup.

Install PVE headers and ensure nvidia hardware is detected. Determine the
available driver version and note this for LXC container usage. Install
drivers.

.. code-block:: bash
  :caption: Instal PVE headers and ensure nvidia hardware is detected.

  apt install pve-headers
  lspci | grep -i nvidia
  apt search nvidia-driver
  apt install nvidia-driver={VERSION} nvidia-smi={VERSION}

Enable nvidia modules on boot.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/modules-load.d/nvidia.conf``

  nvidia-drm
  nvidia
  nvidia_uvm

Populate ``/dev`` on boot with nvidia devices.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/udev/rules.d/70-nvidia.rules``

  # Create nvidia devices for passthru

  # Create /nvidia0, /dev/nvidia1 … and /nvidiactl when nvidia module is loaded
  KERNEL=="nvidia", RUN+="/bin/bash -c '/usr/bin/nvidia-smi -L && /bin/chmod 666 /dev/nvidia*'"

  # Create the CUDA node when nvidia_uvm CUDA module is loaded
  KERNEL=="nvidia_uvm", RUN+="/bin/bash -c '/usr/bin/nvidia-modprobe -c0 -u && /bin/chmod 0666 /dev/nvidia-uvm*'"

.. code-block:: bash
  :caption: Reboot and confirm nvidia hardware is properly assigned.

  reboot
  nvidia-smi

    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: N/A      |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  Quadro RTX 4000     On   | 00000000:42:00.0 Off |                  N/A |
    | 30%   42C    P8     9W / 125W |      1MiB /  7982MiB |      0%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+

    +-----------------------------------------------------------------------------+
    | Processes:                                                                  |
    |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
    |        ID   ID                                                   Usage      |
    |=============================================================================|
    |  No running processes found                                                 |
    +-----------------------------------------------------------------------------+

Determine the devices ID's in ``/dev`` to pass to the appropriate container. All
ID's and devices should be recorded.

.. code-block:: bash
  :caption: Determine device/character ID's via script.

  find /dev/dri/ /dev/nvidia* -type c | xargs ls -lA | awk '{ print $5 }' | sed '/^$/d' | sed 's/,*$//g' | sort | uniq | awk '{ print "lxc.cgroup2.devices.allow: c "$1":* rwm" }'

    lxc.cgroup2.devices.allow: c 195:* rwm
    lxc.cgroup2.devices.allow: c 226:* rwm
    lxc.cgroup2.devices.allow: c 236:* rwm
    lxc.cgroup2.devices.allow: c 508:* rwm

  find /dev/nvidia* -type c ! -name nvidia-cap* | awk '{ print "lxc.mount.entry: "$1" "$1" none bind,optional,create=file" }'

    lxc.mount.entry: /dev/nvidia0 /dev/nvidia0 none bind,optional,create=file
    lxc.mount.entry: /dev/nvidiactl /dev/nvidiactl none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-modeset /dev/nvidia-modeset none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm /dev/nvidia-uvm none bind,optional,create=file
    lxc.mount.entry: /dev/nvidia-uvm-tools /dev/nvidia-uvm-tools none bind,optional,create=file

.. code-block:: bash
  :caption: Determine device ID's via column 5 on ``ls`` output.

  ls -la /dev/nvidia*
  ls -la /dev/dri/*

Shutdown the LXC container and manually edit the LXC configuration to map device
ID's.

.. code-block:: bash
  :caption: **0640 root root** ``/etc/pve/lxc/{VMID}.conf``

  # Nvidia GPU passthru
  lxc.cgroup2.devices.allow: c 195:* rwm
  lxc.cgroup2.devices.allow: c 226:* rwm
  lxc.cgroup2.devices.allow: c 236:* rwm
  lxc.cgroup2.devices.allow: c 508:* rwm
  lxc.mount.entry: /dev/nvidia0 dev/nvidia0 none bind,optional,create=file
  lxc.mount.entry: /dev/nvidiactl dev/nvidiactl none bind,optional,create=file
  lxc.mount.entry: /dev/nvidia-uvm dev/nvidia-uvm none bind,optional,create=file
  lxc.mount.entry: /dev/nvidia-modeset dev/nvidia-modeset none bind,optional,create=file
  lxc.mount.entry: /dev/nvidia-uvm-tools dev/nvidia-uvm-tools none bind,optional,create=file
  lxc.mount.entry: /dev/dri dev/dri none bind,optional,create=dir
  lxc.mount.entry: /dev/nvidia-caps /dev/nvidia-caps none bind,optional,create=dir

.. note::
  Use all ID's to map to ``cgroup2``. Map all nvidia devices to mount; including
  ``/dev/dri`` and ``/dev/nvidia-caps``.

LXC Container
*************
For the LXC container installation of the driver is done manually based on the
driver version on the PVE host.

.. code-block:: bash
  :caption: Manually download the correct driver version.

  wget http://us.download.nvidia.com/XFree86/Linux-x86_64/{VERSION}/NVIDIA-Linux-x86_64-{VERSION}.run
  NVIDIA-Linux-x86_64-{VERSION}.run --no-kernel-module --silent

.. code-block:: bash
  :caption: Verify hardware is detected and reporting properly in the container.

  nvidia-smi

    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: N/A      |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  Quadro RTX 4000     On   | 00000000:42:00.0 Off |                  N/A |
    | 30%   42C    P8     9W / 125W |      1MiB /  7982MiB |      0%      Default |
    |                               |                      |                  N/A |
    +-------------------------------+----------------------+----------------------+

    +-----------------------------------------------------------------------------+
    | Processes:                                                                  |
    |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
    |        ID   ID                                                   Usage      |
    |=============================================================================|
    |  No running processes found                                                 |
    +-----------------------------------------------------------------------------+

`Reference <https://passbe.com/2020/02/19/gpu-nvidia-passthrough-on-proxmox-lxc-container/>`__

`Reference <https://old.reddit.com/r/homelab/comments/b5xpua/the_ultimate_beginners_guide_to_gpu_passthrough/>`__

`Reference <https://www.youtube.com/watch?v=-HCzLhnNf-A&t=618s>`__

`Reference <https://www.youtube.com/watch?v=fgx3NMk6F54>`__
