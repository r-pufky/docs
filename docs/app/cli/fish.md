# [FISH][a]
Friendly Interactive SHell.

## Enable direnv
=== "CachyOS"

    ``` bash
    pacman -S direnv
    ```

=== "Debian"

    ``` bash
    apt install direnv
    ```

!!! abstract "~/.config/fish/config.fish"
    0644 {USER}:{USER}

    ``` fish
    direnv hook fish | source
    ```

``` bash
# Enable processing of ansible.env
echo 'dotenv ansible.env' > .envrc

# Enable direnv for directory.
direnv allow
```

## Disable Greeting
!!! abstract "~/.config/fish/config.fish"
    0644 {USER}:{USER}

    ``` fish
    function fish_greeting
      # noop
    end
    ```

## Default Editor
!!! abstract "~/.config/fish/config.fish"
    0644 {USER}:{USER}

    ``` fish
    set -gx EDITOR vim
    ```

[a]: https://fishshell.com

## Vagrant shell completion
!!! abstract "~/.config/fish/completion/vagrant.fish"
    0644 {USER}:{USER}

    ``` fish
    function __fish_vagrant_ids
      # ID's are hex.
      vagrant global-status | awk '/^[0-9a-f]{7}/ {print $1}'
    end

    # Complete for commands that take an ID (e.g., up, halt, ssh, destroy)
    complete -c vagrant -n "__fish_seen_subcommand_from up halt ssh scp destroy" -a "(__fish_vagrant_ids)"
    ```
