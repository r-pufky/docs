TCP BBR Kernel Patches
----------------------
[TCP BBR][1] is a new congestion controlling algorithm that is designed to
respond to actual congestion instead of packet loss. This results in a dramatic
increase in transfer speeds.

This applies to _any_ Linux distrubtion running Kernel **4.9+** with BBR
patches.

### Verify BBR is supported
Ensure `CONFIG_TCP_CONG_BBR` and `CONFIG_NET_SCH_FQ` are supported in the Kernel
and that the kernel version is **4.9+**.

```bash
uname -r
egrep 'CONFIG_TCP_CONG_BBR|CONFIG_NET_SCH_FQ' /boot/config-$(uname -r)
```
* Both lines should be returned.
* Uname should return a kernel version **4.9** or higher.

### Enable BBR Support

/etc/sysctl.d/10-custom-kernel-bbr.conf `root:root 0640`
```sysctl
net.core.default_qdisc=fq
net.ipv4.tcp_congestion_control=bbr
```

Reboot the system to apply changes.

### Testing Performance
Before/after performance may tested using iperf.

On BBR Server
```bash
iperf -s
```

On Client
```bash
iperf -c {SERVER} -i 2 -t 30
```

[1]: https://cloud.google.com/blog/products/gcp/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster
