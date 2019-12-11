.. _troubleshooting-pc-hardware:

Troubleshooting PC Issues
#########################
I'm asked this all the time, so I put together a list of all the common things
to look for when a PC is flaky and crashing. Even if you *know what you're
doing*, you should run through these steps. You'd be surprised.

General Maintenance
*******************
Required typically yearly. If you are using a new build, skip to
:ref:`random-crashes`.

#. Pull all filters and use canned air / damp rag to clean them. They should be
   obstruction free.
#. Fans

    * Hold fan to prevent rotation. Use canned air on both sides (may require
      removing fan).
    * Use a damp rag (clorox bleach cleanners are good), and wipe out any of the
      hard/compacted dust. Fan should look nearly new.
#. Heatsinks

    * Position canned air in fins and blow through fins to remove dust. Blow
      both ways.
#. Blow dust out of remaining components

    * Pay special attention to flat/unused surfaces.
    * Get under hard-drives.
    * Should look pretty new when done.
#. RAM

    * Remove RAM.
    * Use canned air to clean sticks as well as connectors, reseat.
    * Pay attention to order in case you are using dual or quad channel RAM.
#. Power-up computer with case side off

    * Listen and locate any rapid 'ticking' or 'grinding' noises coming from
      fans and replace those.
    * Replace or ensure fans that are not spinning are connected properly (fans
      may not spin if configured as such in the BIOS/UEFI. You'll have to check
      that).
    * Replace fans that are under spinning.
#. Ensure all conections are tight, and you haven't knocked anything out of
   whack.

.. _random-crashes:

Random 'Crashes'
****************
In most cases I've seen, this is due to hardware not connected properly, or
actual defective hardware. Most BSOD's I've seen in Windows 10 are actually
hardware related and not due to funky Windows installs.

First, make sure when you run tests, you **log everything**. When you crash you
will probably not be paying attention to specific values. This also helps you to
verify faulty hardware with manufacturers later on.

Additionally, pay attention to what you are doing when you crash. It can give
you a good jump-off point for quickly debugging the issue. Gaming? Maybe start
with power/connections/airflow. BSOD's? What does the screen infer?

Basic utilities to monitor system include `HWinfo`_ and `HWmonitor`_. Both of
these provide monitoring and logging for many computer components.

Memory
======
Setup `memtest86`_ on a USB drive and set it to run the standard tests. Faulty
memory will be apparent either immediately, or within a few minutes. In most
cases I've seen, running the test for 24 hours works as a good 'burn in' test,
but won't actually detect any additional memory issues.

If you get errors, walk through each of these steps, retesting on each change:

#. Save the logs.
#. Reseat your memory.
#. Seriously, Reseat your memory.
#. Ensure your memory is paired properly for dual/quad channel.
#. Disable XMP timings.
#. Iterate through the minimum number of sticks to boot; test and add an
   additional memory stick after each test.
#. Always verify your suspected 'defective' stick independently.

CPU's
=====
Setup `CPUZ`_ and run it. It should display your CPU as well as current
frequency and voltages. Check your voltages to make sure your CPU is getting at
least the minimum required to work.

Setup `prime95`_ to stress test CPU. Launch it, then::

  options > torture test > In-place large FFT's

This will allow you to test your CPU under load.

#. Ensure your CPU power (4/8 pin power near CPU) is actually connected.
#. Search for and check voltages for your specific CPU:

    * Watch these numbers as you do the task that crashes your machine.
    * Do they dip? Are they low? You may need to tweak motherboard BIOS to
      supply the right amount of power, or replace the power supply.

#. Is the CPU running hot at idle/load?

    * Generally, *85c* is the limit on CPU heat -- if it is, ensure that
      fans/heatsink are clean and connected.
    * Remove heatsink, clean both CPU and heatsink with isopropel alcohol, and
      replace heatsink compound.
    * Ensure heatsink is contacting CPU correctly.

#. Is your BIOS configured to shutdown automatically when a temperature limit is
   hit? By default this is for extreme cases, but you may be hitting it.

GPU's
=====
Setup `GPUZ`_ and `Furmark`_. Use `GPUZ`_ to get information on the GPU, and
run a stress test on your video card with Furmark. A stable system should be
able to run this at max settings for your PC without crashing, indefinitely.

#. Ensure Windows drivers for the video card are the most recent version.
   `Clean install`_ your drivers if you crash.
#. If you just started crashing and you recently updated drivers,
   `Clean install`_ older versions of your drivers.
#. Re-seat GPU, ensure you are locking the card into the slot.
#. Ensure that Power cables are connected to the GPU if they have connections
   for it.
#. If GPU temperatures are hot at idle, clean fan/heatsinks.
#. Search for and check voltages for your specific GPU.

    * Watch these numbers as you do the task that crashes your machine.
    * Do they dip? Are they low? You may need to tweak motherboard BIOS/EFI to
      supply the right amount of power, or replace the power supply.

#. Is the GPU running hot at idle/load?

    * Generally, *85c* is the limit on GPU heat -- if it is, ensure that
      fans/heatsink are clean and connected.
    * Some drivers will bluescreen if the GPU temperature remains too hot.

#. Use a different PCIe slot. Your 16x might be borked.
#. SLI Configurations

    * Test each card independently, in each slot.
    * Verify that both cards and slots are functioning properly.

HDD's
=====
Setup `CrystalDiskInfo`_ and run it. It should detect all of your HDD's and
SSD's. It will report a general 'SMART' status (e.g. *GOOD*) for each disk and
the temperature.

Setup `CrystalDiskMark`_. After analyzing `CrystalDiskInfo`_ results, if you
believe your crashes related to disk, run the `CrystalDiskMark`_ bench on your
disks -- this will prematurely wear your SSD's. A crash (BSOD) running this
software usually means the disk in question is bad (test a different disk) or
the motherboard SATA/chipset drivers need to be installed or updated.

Sound isn't necessarily a signal of failure. Some drives (like Western Digitals)
are notorious for being loud on spin-up and seeking. This is normal. You need to
make a determination if the sound you are hearing is normal or not. Check
youtube for videos of your specific drive / manufacturer. Bad sounds generally
entail loud 'clicking' or 'clacking' and are obvious.

#. Generally, HDD's should be `pretty tolerant`_ to high temperatures, though
   excessive temperatures for prolonged periods of time *(>~55c)* could cause
   premature failure. Fix this by re-locating drives or adding some cooling.
#. SSD drives (especially M.2 NVME) perform better at higher temperatures and
   have internal throttling mechanisms. It's generally OK to see them operating
   `around ~60c`_.
#. Check on the drive in question. In the detailed SMART report, look for
   indicators of failing drives.

    * Raw Read Error Rate.
    * Reallocated Sectors/NAND Count.
    * Spin Retry Count.
    * Reallocation Event Count.
    * Uncorrectable Sector Count.
    * Ultra DMA CRC Error Count.
    * Write Error Rate.
    * Seek Error Rate.
    * Erase Fail Count.
    * Program Fail Count.

   .. NOTE::
      SMART still may report GOOD, but high rates of the preceeding failures is
      an indication your drive is failing. It is common to have a few of these
      in normal usage, that's how drives work; a drive with an issue *will*
      stand out with error rates. You'll know it when you see it.

#. If SATA: replace cables. Throw the old ones out. Check power connections.
#. If M.2 NVME: ensure slot isn't shared or disabled. Move to another slot if
   possible.

Motherboards
============
This is very specific to each motherboard you own. however general concepts
remain the same. Get your motherboard model in the BIOS, usually by pressing
*del*.

#. Always search for and apply the latest *non-beta* BIOS update. This will
   usually address CPU microcode and board instability issues.
#. Only apply *beta* BIOS updates if the specific fix applies directly to your
   situation. No, you are not a special case.
#. Ensure you haven't disabled something you are trying to use in your BIOS
#. *Always* download the drivers associated with your motherboard and *install*
   *them*. I don't care if windows 'auto-detected' everything. This is a huge
   source of many issues. Particularily, you want to ensure that you have
   installed these (listed in order of importance). Most of the time there will
   be a newer version on the site, and if you don't use the specific device, you
   can disable it in the BIOS or Windows Device Manager:

    * BIOS/UEFI.
    * Chipset.
    * SATA.
    * Audio.
    * VGA (even if descrete card, e.g. GPU, is used).
    * LAN.
    * Wireless.
    * Bluetooth.

#. If power supplied to the motherboard (and other components) is consistently
   low, or jumps around a lot, replace your power supply.
#. Verify your RAM and SSD's (*especially NVME*) are listed as compatible with
   your specific motherboard. These are listed usually as *hardware
   qualification lists*. In recent years, I've noticed that motherboards are
   *much more sensitive* to RAM and SSD's used, even though they are based on a
   standard.

Utilities
*********
These are what I consider the bare minimum in diagnosing your PC. Download them
and keep them handy.

#. `CPUZ`_ (CPU specific info)
#. `GPUZ`_ (GPU specific info)
#. `Furmark`_ (GPU stress testing)
#. `HWmonitor`_ (CPU/GPU/Motherboard info)
#. `HWinfo`_ (CPU/GPU/Motherboard info)
#. `memtest86`_ (Memory stress testing)
#. `prime95`_ (CPU stress testing)
#. `CrystalDiskInfo`_ (Disk specific info)
#. `CrystalDiskMark`_ (Disk stress testing)

.. _HWinfo: https://www.hwinfo.com/download/
.. _HWmonitor: https://www.cpuid.com/softwares/hwmonitor.html
.. _memtest86: https://www.memtest86.com
.. _CPUZ: https://www.cpuid.com/softwares/cpu-z.html
.. _prime95: https://www.mersenne.org/download
.. _GPUZ: https://www.techpowerup.com/gpuz
.. _Furmark: https://geeks3d.com/furmark/
.. _Clean install: https://forums.tomshardware.com/faq/how-to-perform-a-clean-install-of-your-video-card-drivers.2402269/
.. _CrystalDiskInfo: https://crystalmark.info/en/software/crystaldiskinfo/
.. _CrystalDiskMark: https://crystalmark.info/en/software/crystaldiskmark
.. _pretty tolerant: https://static.googleusercontent.com/media/research.google.com/en//archive/disk_failures.pdf
.. _around ~60c: https://forums.guru3d.com/threads/what-should-normal-safe-operating-temperature-be-for-a-m-2-nvme-drive.418369/