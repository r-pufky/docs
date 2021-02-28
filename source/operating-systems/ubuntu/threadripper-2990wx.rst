.. _ubuntu-2990wx-linux-patches:

2990WX Linux Patches
####################
Until Kernel 4.18.6 is released with the k10temp patch, Threadripper thermals
will be mis-reported by 27c. Building a custom Kernel module will fix the issue
temporarily.

This specifically patches thermal detection for the `Gigabyte X399 Aorus
Extreme`_ for Ubuntu, but most likely will easily translate to other distros and
motherboards.

Install Build Tools
*******************
Add ``deb-src`` lines for distribution sources in ``/etc/apt`` (just duplicate
the ``deb`` line and add ``deb-src``).

.. code-block:: bash
  :caption: Add deb-src to apt and install build tools, Kernel dependencies.

  apt update && apt upgrade
  apt install build-essential bison flex linux-headers lm-sensors
  apt build-dep linux

Clone patched IT87 Kernel Driver
********************************
The original Kernel IT87 driver was removed by the original author when he
couldn't keep up with requests anymore. Pull from a `clone of that repository`_
with the AMD patches built in. This will build and install the module for your
current Kernel.

.. code-block:: bash

  git clone https://github.com/rpavlik/it87
  cd it87
  make clean
  make
  make install

.. note::
  https://github.com/Road-Drum/it87 contains a unmodified fork of original it87.

Force Detection of Module
*************************
Both the `IT8792E and IT8795E`_ have the same ID, so we need to force module
installation and ignore conflicts.

.. code-block:: bash
  :caption: Install it87 module and show sensor data.

  modprobe it87 ignore_resource_conflict=1
  sensors-detect
  sensors | grep -i amd

* ``sensors-detect`` can be run with all default values.
* See :ref:`reading-sensors` for a breakdown of sensors for the X399 Aorus
  board.
* If a line is returned, then you are correctly reading Threadripper thermal
  temperatures.

Load Module on Boot
*******************
Add the module load line for ramfs and update it.

.. code-block::
  :caption: **0644 root root** ``/etc/initramfs/modules``
  :lineno-start: 12
  :emphasize-lines: 2

  ...
  it87 ignore_resource_conflict=1

.. code-block:: bash

  sudo update-initramfs -u

.. important::
  Any new Kernel installed will require a new build of this module.

.. _reading-sensors:

Reading Sensors
***************
Be sure to read the correct chipset to find the right sensor values. Labels are
according to the board layout diagram in the `manual`_.

.. code-block:: bash

  sensors

.. code-block:: bash
  :caption: it8792-isa-0a60.

  in0:          +1.19 V  (min =  +0.00 V, max =  +2.78 V)
  in1:          +1.50 V  (min =  +0.00 V, max =  +2.78 V)
  in2:          +1.05 V  (min =  +0.00 V, max =  +2.78 V)
  in3:          +2.02 V  (min =  +0.00 V, max =  +2.78 V)
  in4:          +1.80 V  (min =  +0.00 V, max =  +2.78 V)
  in5:          +1.50 V  (min =  +0.00 V, max =  +2.78 V)
  in6:          +2.78 V  (min =  +0.00 V, max =  +2.78 V)
  3VSB:         +3.33 V  (min =  +0.00 V, max =  +5.56 V)
  Vbat:         +3.21 V
  fan1:           0 RPM  (min =    0 RPM)
  fan2:           0 RPM  (min =    0 RPM)
  fan3:           0 RPM  (min =    0 RPM)
  temp1:        +43.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp2:        -55.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp3:        +41.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor

it8792 Fan Mapping

+-------------+---------------+
| Layout Name | Sensor Name   |
+=============+===============+
| fan1        | SYS_FAN5_PUMP |
+-------------+---------------+
| fan2        | SYS_FAN6_PUMP |
+-------------+---------------+
| fan3        | SYS_FAN4      |
+-------------+---------------+

.. code-block:: bash
  :caption: it8686-isa-0a40.

  in0:          +0.77 V  (min =  +0.00 V, max =  +3.06 V)
  in1:          +2.00 V  (min =  +0.00 V, max =  +3.06 V)
  in2:          +2.03 V  (min =  +0.00 V, max =  +3.06 V)
  in3:          +2.00 V  (min =  +0.00 V, max =  +3.06 V)
  in4:          +1.19 V  (min =  +0.00 V, max =  +3.06 V)
  in5:          +0.88 V  (min =  +0.00 V, max =  +3.06 V)
  in6:          +1.20 V  (min =  +0.00 V, max =  +3.06 V)
  3VSB:         +3.24 V  (min =  +0.00 V, max =  +6.12 V)
  Vbat:         +3.12 V
  fan1:         432 RPM  (min =   10 RPM)
  fan2:           0 RPM  (min =    0 RPM)
  fan3:        1506 RPM  (min =    0 RPM)
  fan4:         703 RPM  (min =    0 RPM)
  fan5:           0 RPM  (min =    0 RPM)
  temp1:        +40.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp2:        +53.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp3:        +36.0°C  (low  =  +0.0°C, high = +90.0°C)  sensor = AMD AMDSI
  temp4:        +44.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp5:        +49.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor
  temp6:        -55.0°C  (low  = +127.0°C, high = +127.0°C)  sensor = thermistor

it8686 Fan Mapping

+-------------+------------------------------------+
| Layout Name | Sensor Name                        |
+=============+====================================+
| fan1        | CPU_FAN                            |
+-------------+------------------------------------+
| fan2        | SYS_FAN1                           |
+-------------+------------------------------------+
| fan3        | SYS_FAN2 (Built in VRM fans).      |
+-------------+------------------------------------+
| fan4        | SYS_FAN3                           |
+-------------+------------------------------------+
| fan5        | CPU_OPT                            |
+-------------+------------------------------------+
| temp3       | Threadripper CPU temp (AMD AMDSI). |
+-------------+------------------------------------+

.. note::
  ``SYS_FAN2`` is unlisited in `manual`_.

Building Kernel 4.18.6+
***********************
If you would rather install a later Kernel, be aware that this will not be auto
upgraded, and you'll need to install additional packages for Kernel support such
as ZFS (e.g. zfs-dkms spl-dkms). These are essentially Vanilla Kernels for
Ubuntu with core patches. You will need *at least* Kernel **4.18.6**.

Determine your platform and grab `Kernel 4.18.6`_ source with ubuntu pataches.
Any recent 64bit CPU will be **amd64**. You *only* need the generic Kernel.

.. code-block:: bash
  :caption: Download ubuntu Kernel 4.18.6 package and install.

  wget http://Kernel.ubuntu.com/~Kernel-ppa/mainline/v4.18.6/linux-headers-4.18.6-041806_4.18.6-041806.201809050847_all.deb
  wget http://Kernel.ubuntu.com/~Kernel-ppa/mainline/v4.18.6/linux-headers-4.18.6-041806-generic_4.18.6-041806.201809050847_amd64.deb
  wget http://Kernel.ubuntu.com/~Kernel-ppa/mainline/v4.18.6/linux-image-unsigned-4.18.6-041806-generic_4.18.6-041806.201809050847_amd64.deb
  wget http://Kernel.ubuntu.com/~Kernel-ppa/mainline/v4.18.6/linux-modules-4.18.6-041806-generic_4.18.6-041806.201809050847_amd64.deb
  dpkg -i linux-headers*all.deb
  dpkg -i linux-headers*amd64.deb
  dpkg -i linux-modules*amd64.deb
  dpkg -i linux-image*amd64.deb

Load the updated Kernel module and Add to ``ramfs``:

.. code-block:: bash

  modprobe k10temp

.. code-block::
  :caption: **0644 root root** ``/etc/initramfs/modules``
  :lineno-start: 12
  :emphasize-lines: 2

  ...
  k10temp

.. code-block:: bash

  sudo update-initramfs -u

.. rubric:: References

#. `Monitor Ryzen temperatures in latest Kernels <https://linuxconfig.org/monitor-amd-ryzen-temperatures-in-linux-with-latest-Kernel-modules>`_
#. `Get the CPU temperature in Ubuntu <https://askubuntu.com/questions/15832/how-do-i-get-the-cpu-temperature>`_
#. `Ubuntu Kernel mainline build repository <https://wiki.ubuntu.com/Kernel/MainlineBuilds>`_

.. _Gigabyte X399 Aorus Extreme: https://www.gigabyte.com/Motherboard/X399-AORUS-XTREME-rev-10
.. _clone of that repository: https://github.com/rpavlik/it87
.. _IT8792E and IT8795E: https://forum.level1techs.com/t/threadripper-lm-sensors-halp/119487/6
.. _manual: http://download.gigabyte.us/FileList/Manual/mb_manual_x399-aorus-xtreme_1001_e.pdf
.. _`Kernel 4.18.6`: https://kernel.ubuntu.com/~kernel-ppa/mainline/
