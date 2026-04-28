# Troubleshooting


## Failed to connect to user scope bus via local transport
User environment variables required for systemd user configuration are not
present. This typically happens with **SSH** and **sudo** commands.

!!! danger ""
    ``` log
    Failed to connect to user scope bus via local transport:
    $DBUS_SESSION_BUS_ADDRESS and $XDG_RUNTIME_DIR not defined (consider using
    --machine=<user>@.host --user to connect to bus of other user)
    ```

``` bash
# Export required user systemd unit environment variables.
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"

# Enable service lingering for user.
loginctl enable-linger {USER}
```

Setup [Systemd User Environment](README.md#systemd-user-environment) to prevent
errors in the future.

Re-run command.
