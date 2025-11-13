# Secure Boot

!!! example "Migrated to ansible collection"
    Use [r_pufky.deb.secure_boot][a].


## Security Policy Violation
Microsoft changed secure boot shim and disabled previously allowed shims used
in older installers.

!!! danger "Error"
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
5. Update and re-enable secure boot.f


## Reference[^1][^2][^3][^4]

[^1]: https://mjg59.dreamwidth.org/70348.html
[^2]: https://old.reddit.com/r/linuxquestions/comments/1euuha4/please_help_error_message_verifying_shim_sbat/
[^3]: https://en.opensuse.org/openSUSE:UEFI#Reset_SBAT_string_for_booting_to_old_shim_in_old_Leap_image
[^4]: https://forums.linuxmint.com/viewtopic.php?t=427297

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs
