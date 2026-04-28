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
# Export required environment for remainder of session and re-run commands.
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"

# Enable service lingering for user.
loginctl enable-linger {USER}
```

!!! abstract "~./bashrc"
    0644 {USER}:{USER}

    ``` bash
    # Add at end of .bashrc to always setup environment even if SSH'ed.
    if [ -z "$XDG_RUNTIME_DIR" ]; then
        export XDG_RUNTIME_DIR="/run/user/$(id -u)"
        export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
    fi
    ```

!!! tip "Alternatively use machinectl"
    machinectl spawns a fully isolated (systemd/dbus session) interactive shell
    inside a given machine.

    ``` bash
    sudo machinectl shell {USER}@.host
    ```

Re-run command.
