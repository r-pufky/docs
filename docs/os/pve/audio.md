# Audio Passthrough
All PVE nodes must be configured for LXC/VM migration support.

## Host (PVE)
Enable audio controllers if required.

### Determine Audio Devices

``` bash
# Radeon(Rembrandt/Strix), NVIDIA devices are GPU-based audio processors. These
# should be shared with GPU passthrough if used.
$ lspci | grep -i audio
> 01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Radeon High Definition Audio Controller [Rembrandt/Strix]
> 01:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h/1ah HD Audio Controller

# Map device names to devices.
$ ls -la /dev/snd/by-path
# Radeon is C0, Onboard audio is C1.
> lrwxrwxrwx 1 root root  12 Apr 23 20:55 pci-0000:01:00.1 -> ../controlC0
> lrwxrwxrwx 1 root root  12 Apr 23 20:55 pci-0000:01:00.6 -> ../controlC1

# Show all device nodes.
$ ls -la /dev/snd
# Audio control interface.
> crw-rw----  1 root audio 116,  7 Apr 23 20:55 controlC0
# Raw HW device. Most applications do not require it.
> crw-rw----  1 root audio 116,  6 Apr 23 20:55 hwC0D0
# (P)layback devices (output).
> crw-rw----  1 root audio 116,  2 Apr 23 20:55 pcmC0D3p
> crw-rw----  1 root audio 116,  3 Apr 23 20:55 pcmC0D7p
> crw-rw----  1 root audio 116,  4 Apr 23 20:55 pcmC0D8p
> crw-rw----  1 root audio 116,  5 Apr 23 20:55 pcmC0D9p

# Audio control interface.
> crw-rw----  1 root audio 116, 11 Apr 23 20:55 controlC1
# Raw HW device. Most applications do not require it.
> crw-rw----  1 root audio 116, 10 Apr 23 20:55 hwC1D0
# (C)apture device (mic).
> crw-rw----  1 root audio 116,  9 Apr 23 20:55 pcmC1D0c
# (P)layback device (output).
> crw-rw----  1 root audio 116,  8 Apr 23 20:55 pcmC1D0p

# Global MIDI support. Most applications do not require it.
> w-rw----  1 root audio 116,  1 Apr 23 20:55 seq

# Global hardware audio stream timer. Shared across ALL passthrough instances.
> w-rw----  1 root audio 116, 33 Apr 23 20:55 timer
```

### Container configuration
``` bash
# Determine audio group.
grep audio /etc/group
> audio:x:29:

# Add any user to audio group to enable access.
usermod -aG audio {USER}
```

### Map Audio device to PVE
On PVE Host

``` bash
# Passthrough audio device to LXC container 100. Control and Timer are required
# as well as any playback or capture devices. Automatically map these to the
# CONTAINER GID found above.
pct set 100 -dev0 /dev/snd/controlC0,gid=29,uid=0
pct set 100 -dev1 /dev/snd/pcmC0D0p,gid=29,uid=0
pct set 100 -dev2 /dev/snd/timer,gid=29,uid=0
```

``` bash
# Restart LXC container and verify device appears with audio groups.
ls -l /dev/snd
```

## Reference[^1]
[^1]: https://medium.com/@jakeasmith/running-a-vllm-lxc-on-proxmox-9-f7fbb8a7db2f
