# Troubleshooting


## Could not insert 'zfs': Key was rejected by service
Secure boot enabled systems require the MOK (Machine Owner's Key) for signed
DKMS modules to be loaded into the kernel, otherwise errors like the following
will occur:

!!! danger ""
    /sbin/modprobe zfs
    > modprobe: ERROR: could not insert 'zfs': Key was rejected by service

Certificates must be added to secure boot certificate store before enabling
secure boot; intentionally **requires** physical presence (or pre-existing keys
to be installed during bare-metal turn-up via firmware/BIOS).

**mokutil** manages this process and generates changes for MOK Manager (loaded
by the secure boot shim) to process on next reboot.


## Security Policy Violation
Microsoft changed secure boot shim and disabled previously allowed shims used
in older installers.

!!! danger ""
    Verifying shim SBAT data failed: Security Policy Violation
    Something has gone seriously wrong: SBAT self-check failed: Security Policy Violation

Disable secure boot, disable SBAT policy, and install updated shims.

1. Disable secure boot.
2. Boot live cd.
3. install **mokutil** and delete SBAT policy.

    ``` bash
    mokutil --set-sbat-policy delete
    ```

4. Reboot.
5. Update and re-enable secure boot.


## Reference[^1][^2][^3][^4]

[^1]: https://mjg59.dreamwidth.org/70348.html
[^2]: https://old.reddit.com/r/linuxquestions/comments/1euuha4/please_help_error_message_verifying_shim_sbat/
[^3]: https://en.opensuse.org/openSUSE:UEFI#Reset_SBAT_string_for_booting_to_old_shim_in_old_Leap_image
[^4]: https://forums.linuxmint.com/viewtopic.php?t=427297

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs
