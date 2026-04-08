# [Code Server][a]
VSCodium via WebUI over forwarded SSH connection.

!!! tip "Use Chrome"
    Chrome correct interprets complex key combinations. When navigating to
    code-server, install the offered PWA (progessive web app). This will open
    the code-serve page in a separate window and allow native-like app usage.

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

### Configure SSH Host
Create a pre-defined host to automatically configure forwarded ports.

!!! abstract "~/.ssh/confg"
    0644 {USER}:{USER}

    ``` bash
    Host remote_dev
      HostName {IP}
      # code-server, mkdocs
      LocalForward 2222 localhost:2222
      LocalForward 8000 localhost:8000
      # GPG Agent forwarding (local yubikey taps for remote).
      #RemoteForward /run/user/1000/gnupg/S.gpg-agent /run/user/1000/gnupg/S.gpg-agent
      #RemoteForward /run/user/1000/gnupg/S.gpg-agent.ssh /run/user/1000/gnupg/S.gpg-agent.ssh
      ForwardAgent yes
      Port 51821
      LogLevel error
    ```

``` bash
ssh remote_dev
```

## Locations

  Option                | Location
 ----------------------:|----------
          User Settings | **~/.local/share/code-server/User/**
                 Config | **~/.config/code-server/config.yml**

[a]: https://github.com/coder/code-server
[b]: https://github.com/coder/code-server/blob/main/docs/guide.md