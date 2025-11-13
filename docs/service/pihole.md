# Pi-Hole
Pi-Hole DNS Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.pihole][a].


## Setup
Clients will send DNS requests to Pi-Hole. Pi-Hole will either block, resolve
or forward those requests to the router. The router will be able to resolve
local DNS names and forward remaining unknown queries to upstream DNS servers.

Optionally, if the router supports **destination NAT**, all DNS traffic will be
routed directly to *Pi-Hole*. This catches hard-coded DNS servers that many
phone apps, IoT devices, and applications use.

1. Router upstream DNS servers set to **1.1.1.1**, **8.8.8.8**.
2. Router DHCP Assigns **Pi-Hole** as primary DNS server for clients.
3. Router uses [Destination NAT - DNAT][b] to force all DNS requests to
   **Pi-Hole** (optional).
4. Pi-Hole upstream DNS server set to **router**.

### Set Admin Password
``` bash
pihole -a -p
```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: ../networking/edge_os/README.md#add-a-destination-nat-rule
