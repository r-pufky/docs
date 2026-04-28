# [systemd][a]

## Systemd User Environment
User-based systemd units may fail over **SSH** or **sudo** as generally a full
systemd environment is not configured automatically with a non-local login.

``` bash
# Export required user systemd unit environment variables.
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"

# Enable service lingering for user.
loginctl enable-linger {USER}
```

!!! abstract "~/.profile"
    0644 {USER}:{USER}

    ``` bash
    if [ -z "$XDG_RUNTIME_DIR" ]; then
        export XDG_RUNTIME_DIR="/run/user/$(id -u)"
        export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
    fi
    ```

``` bash
# Alternatively use machinectl to spawn a fully isolated (systemd/dbus session)
# interactive shell on a given machine. Use this after SSH/sudo.
sudo machinectl shell {USER}@.host
```

## Cron Replacement
Actively migrate cronjobs to systemd timers. They are much more flexible and
provide consistency on systemd systems. These may also be deployed per-user.

!!! abstract "job.service"
    0644 root:root

    ``` ini
    # Service executes the commands or script from original cronjob.
    [Unit]
    Description=Cronjob service example.
    Requires=cron_example.timer
    After=network.target
    Wants=network.target

    [Service]
    Type=simple
    ExecStart=/bin/bash -c '/usr/bin/tar -cvJf /srv/test.tar.xz" "/opt/test"'
    WorkingDirectory=/opt/test
    User=test_user
    Group=test_user

    [Install]
    WantedBy=multi-user.target
    ```

!!! abstract "job.timer"
    0644 root:root

    ``` ini
    # Timer acts as the scheduler allowing for fine-grained scheduling of job.
    [Unit]
    Description=cron_example.service timer.
    Requires=cron_example.service

    [Timer]
    OnBootSec=1d

    [Install]
    WantedBy=timers.target
    ```

``` bash
systemctl daemon-reload
systemctl enable job.service job.timer
systemctl start job.timer
```

## Analyze Boot Time
Don't rabbit hole. Usually slow boot times are from connected drives and
devices.

``` bash
systemd-analyze plot > plot.svg
```

## Service Security Exposure
Generate exposure threat ratings for current system services.

``` bash
systemd-analyze security
```

## Reference[^1]
[^1]: https://www.freedesktop.org/software/systemd/man/latest/index.html

[a]: https://wiki.archlinux.org/title/Systemd
