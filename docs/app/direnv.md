# [direnv][a]
Load and unload environments based on current directory.

## Setup

=== "Arch"

    ``` bash
    pacman -S direnv
    ```

=== "Debian"

    ``` bash
    apt install direnv
    ```

!!! abstract ".bashrc"

    ``` bash
    eval "$(direnv hook bash)"
    ```
!!! abstract "~/.config/fish/config.fish"

    ``` bash
    direnv hook fish | source
    ```

!!! warning "Bash is used to parse .envrc files"
    environment files (**.envrc**) are processed using bash and exported to
    whatever shell the user is currently running.

## Auto configure virtual environments
Use with UV to automatically create, activate, and manage virtual environments.

``` bash
# Create venv with required packages.
uv init --bare  # Only create pyproject.toml file for venv.
uv add ansible argcomplete ansible-lint molecule
```

!!! abstract "pyproject.toml"
    0644 {USER}:{USER}

    ``` toml
    name = "dir-uv"
    version = "0.1.0"
    requires-python = ">=3.14"
    dependencies = [
        "ansible>=13.4.0",
        "ansible-lint>=26.3.0",
        "argcomplete>=3.6.3",
        "molecule>=26.3.0",
    ]
    ```

!!! abstract ".envrc"
    0644 {USER}:{USER}

    ``` bash
    # direnv executes .envrc in bash and exports back to current shell.

    # Create venv if needed and activate.
    # Activate using bash as these are exported to current user shell.
    uv sync --all-extras && source .venv/bin/activate

    source ansible.env  # Optionally source addition environments.
    ```

``` bash
# Enable auto parsing of environment on entering directory.
direnv allow
```

**uv.lock**, **.envrc**, **pyproject.toml** must be added to git repositories
to enable one-step environment configuration.

[a]: https://direnv.net
