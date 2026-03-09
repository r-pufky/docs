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
