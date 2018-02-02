Troubleshooting PC Issues
-------------------------
I'm asked this all the time, so I put together a list of all the common things
to look for when a PC is flaky and crashing. Even if you _know what you're 
doing_, you should run through these steps. You'd be surprised.

General Maintenance
-------------------
Required typically yearly. If you are using a new build, skip to the next
section.

1. Pull all filters and use canned air / damp rag to clean them. They should be
   obstruction free.
2. Fans
   * Hold fan to prevent rotation. Use canned air on both sides (may require
     removing fan)
   * Use a damp rag (clorox bleach cleanners are good), and wipe out any of the
     hard/compacted dust. Fan should look nearly new.
3. Heatsinks
   * Position canned air in fins and blow through fins to remove dust. Blow both
     ways
4. Blow dust out of remaining components. Special attention to flat/unused
   surfaces. also get under hard-drives. Should look pretty new before you're
   done.
5. Remove RAM, use canned air to clean sticks as well as connectors, reseat. Pay
   attention to order in case you are using dual or quad channel RAM.
5. Power-up computer with case side off. Listen and locate any rapid "ticking"
   or "grinding" noises coming from fans. Replace those. Replace or ensure fans
   that are not spinning are connected properly (fans may not spin if configured
   as such in the BIOS. You'll have to check that). Replace fans that are under
   spinning.
6. Ensure all conections are tight, and you haven't knocked anything out of
   whack.

Random "Crashes"
----------------
In most cases I've seen, this is due to hardware not connect properly, or actual
defective hardware. Most BSOD's I've seen in Windows 10 are actually hardware
related and not due to funky Windows installs.

First, make sure when you run tests, you log everything. When you crash you will
probably not be paying attention to specific values. This also helps you to
verify faulty hardware with manufacturers later on.

Additionally, pay attention to what you are doing when you crash. It can give
you a good jump-off point for quickly debugging the issue. Gaming? Maybe start
with power/connections/airflow. BSOD's? What does the screen infer?

### Memory
Setup [memtest86][5] on a USB drive and set it to run the standard tests. Faulty
memory will be apparent either immediately, or within a few minutes. In most
cases I've seen, running the test for 24 hours works as a good 'burn in' test,
but won't actually detect any additional memory issues.

If you get errors, walk through each of these steps, retesting on each change:
* Save the logs
* Reseat your memory
* Seriously, Reseat your memory
* Ensure your memory is paired properly for dual/quad channel
* Disable XMP timings
* Iterate through the minimum number of sticks to boot; test and add an
  additional memory stick after each test
* Always verify your suspected 'defective' stick independently

### CPU's
Setup [CPUZ][1] and run it. It should display your CPU as well as current
frequency and voltages. Check your voltages to make sure your CPU is getting at
least the minimum required to work.

Setup [prime95][6] to stress test CPU. Launch it, then

```
options > torture test > In-place large FFT's
```

This will allow you to test your CPU under load.

* Ensure your CPU power (4/8 pin power near CPU) is actually connected
* Search for and check voltages for your specific CPU. Watch these numbers as
  you do the task that crashes your machine. Do they dip? Are they low? You may
  need to tweak motherboard BIOS to supply the right amount of power, or replace
  the power supply
* Is the CPU running hot at idle/load? (generally, 85c is the limit on CPU heat)
  If it is, ensure that fans/heatsink are clean and connected. Remove heatsink, 
  clean both CPU and heatsink with isopropel alcohol, and replace heatsink 
  compound. Ensure heatsink is contacting CPU correctly.
* Is your BIOS configured to shutdown automatically when a temperature limit is
  hit? By default this is for extreme cases, but you may be hitting it.

### GPU's
Setup [GPUZ][2] and [Furmark][3]. Use GPUZ to get information on the GPU, and
run a stress test on your video card with Furmark. A stable system should be
able to run this at max settings for your PC without crashing, indefinitely.

* Ensure Windows drivers for the video card are the most recent version. 
  [Clean install][8] your drivers if you crash
* If you just started crashing and you recently updated drivers, 
  [clean install][8] older versions of your drivers
* Re-seat GPU, ensure you are locking the card into the slot
* Ensure that Power cables are connected to the GPU if they have connections for
  it
* If GPU temperatures are hot at idle, clean fan/heatsinks
* Search for and check voltages for your specific GPU. Watch these numbers as
  you do the task that crashes your machine. Do they dip? Are they low? You may
  need to tweak motherboard BIOS to supply the right amount of power, or replace
  the power supply
* Is the GPU running hot at idle/load? (generally, 85c is the limit on GPU heat)
  If it is, ensure that fans/heatsink are clean and connected. Some drivers will
  bluescreen if the GPU temperature remains too hot.
* SLI? Test each card indepently, in each slot. Verify that both cards and slots
  are functioning properly
* Use a different PCIe slot. Your 16x might be borked

### HDD's
Setup [CrystalDiskInfo][7] and run it. It should detect all of your HDD's and
SSD's. It will report a general 'SMART' status (e.g. GOOD) for each disk and the
temperature.

Setup [CrystalDiskMark][7]. After analyzing info results, if you believe your
crashes related to disk, run the CrystalDiskMark bench on your disks -- this
will prematurely wear your SSD's. A crash (BSOD) running this software usually
means the disk in question is bad (test a different disk) or the motherboard
SATA/chipset drivers need to be installed or updated.

Sound isn't necessarily a signal of failure. Some drives (like Western Digitals)
are notorious for being loud on spin-up and seeking. This is normal. You need to
make a determination if the sound you are hearing is normal or not. Check
youtube for videos of your specific drive / manufacturer. Bad sounds generally
entail loud clicking/clacking and are obvious.

* Generally, HDD's should be [pretty tolerant][9] to high temperatures, though
  excessive temperatures for prolonged periods of time (>~55c) could cause
  premature failure. Fix this by re-locating drives or adding some cooling.
* SSD drives (especially M.2 NVME) perform better at higher temperatures and
  have internal throttling mechanisms. It's generally OK to see them operating
  [around ~60c][10].
* Check on the drive in question. In the detailed SMART report, look for
  indicators of failing drives. NOTE: SMART still may report GOOD, but high
  rates of the following failures is an indication your drive is failing. It is
  common to have a few of these in normal usage, that's how drives work; a drive
  with an issue *will* stand out with error rates. You'll know it when you see
  it:
  * Raw Read Error Rate
  * Reallocated Sectors/NAND Count
  * Spin Retry Count
  * Reallocation Event Count
  * Uncorrectable Sector Count
  * Ultra DMA CRC Error Count
  * Write Error Rate
  * Seek Error Rate
  * Erase Fail Count
  * Program Fail Count
* If SATA, replace cables. Throw the old ones out. Check power connections.
* If M.2 / NVME, ensure slot isn't shared or disabled. Move to another slot if
  possible.

### Motherboards
This is very specific to each motherboard you own. however general concepts
remain the same. Get your motherboard model in the BIOS, usually by pressing
*del*.

* Always search for and apply the latest *non-beta* BIOS update. This will
  usually address CPU microcode and board instability issues.
* Only apply *beta* BIOS updates if the specific fix applies directly to your
  situation. No, you are not a special case.
* Ensure you haven't disabled something you are trying to use in your BIOS
* *Always* download the drivers associated with your motherboard and *install*
  *them*. I don't care if windows 'auto-detected' everything. This is a huge
  source of many issues. Particularily, you want to ensure that you have
  installed these (listed in order of importance). Most of the time there will
  be a newer version on the site, and if you don't use the specific device, you
  can disable it in the BIOS or Windows Device Manager:
  * BIOS
  * Chipset
  * SATA
  * Audio
  * VGA (even if descrete card, e.g. GPU, is used)
  * LAN
  * Wireless
  * Bluetooth
* If power supplied to the motherboard (and other components) is consistently
  low, or jumps around a lot, replace your power supply.

Utilities
---------
These are what I consider the bare minimum in diagnosing your PC. Download them
and keep them handy.

1. [CPU-Z][1] (CPU specific info)
2. [GPU-Z][2] (GPU specific info)
3. [Furmark][3] (GPU stress testing)
4. [HWmonitor][4] (CPU/GPU/Motherboard info)
5. [memtest86][5] (Memory stress testing)
6. [prime95][6] (CPU stress testing)
7. [CrystalDiskInfo][7] (Disk specific info)
8. [CrystalDiskMark][7] (Disk stress testing)

[1]: https://www.cpuid.com/softwares/cpu-z.html
[2]: https://www.techpowerup.com/gpuz/
[3]: http://ozone3d.net/benchmarks/fur/
[4]: https://www.cpuid.com/softwares/hwmonitor.html
[5]: https://www.memtest86.com/
[6]: https://www.mersenne.org/download/
[7]: https://crystalmark.info/software/CrystalDiskInfo/index-e.html
[8]: http://www.tomshardware.com/faq/id-2767677/perform-clean-install-video-card-drivers.html
[9]: https://static.googleusercontent.com/media/research.google.com/en//archive/disk_failures.pdf
[10]: https://www.amplicon.com/docs/white-papers/SSD-vs-HDD-white-paper.pdf