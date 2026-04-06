# [Code Server][a]
VSCodium via WebUI over forwarded SSH connection.

=== "CachyOS"
    ``` bash
    paru -S code-server
    paru -S code-server-marketplace  # Auto patch MS Marketplace.
    ```

## Copy VSCodium Profiles
A majority of extensions will work with code-server. It is not recommended to
link VSCodium profiles to code-server profiles.

``` bash
# Start the service to auto-generate locations and default config.
# Recommend always manually starting and stopping the service.
systemctl --user start code-server
systemctl --user stop code-server

# Copy existing user settings and keybindings. Not all settings will carry over
# and may require explicitly setting on code-server.
cp ~"/.config/Code - OSS/User/settings.json" ~/.local/share/code-server/User/
cp ~"/.config/Code - OSS/User/keybindings.json" ~/.local/share/code-server/User/

# Export extensions and install them on code-server.
code --list-extensions | xargs -L 1 code-server --install-extension
```

### [Configure Service][b]
Changes require service restart.

!!! abstract "~/.config/code-server/config.yml"
    0644 {USER}:{USER}

    ``` yaml
    # Only serve on localhost requiring access via SSH port forwarding.
    # ssh -L 2222:localhost:2222 {IP} -p {PORT}
    bind-addr: 127.0.0.1:2222
    auth: none
    ```

``` bash
systemctl --user start code-server
```

## Locations

  Option                | Location
 ----------------------:|----------
          User Settings | **~/.local/share/code-server/User/**
                 Config | **~/.config/code-server/config.yml**

[a]: https://github.com/coder/code-server
[b]: https://github.com/coder/code-server/blob/main/docs/guide.md