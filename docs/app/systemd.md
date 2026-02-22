# [systemd][a]

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

[a]: https://wiki.archlinux.org/title/Systemd

## Reference[^1]

[^1]: https://www.freedesktop.org/software/systemd/man/latest/index.html