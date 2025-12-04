# Troubleshooting


## Deleted DHCP Host Still Resolves in DNS
When deleting a DHCP host, the DNS reservation should be [removed as well][a].
However [there is a bug][b] in which these hosts are never deleted.

Delete hosts in **/etc/hosts** which are no longer used and reboot the router.


## DNS Hostnames not Resolving
DHCP server on the edgerouter needs to update the hosts file when new IP's are
issued.

Enable Dynamic DNS Updates
!!! example "Config Tree ➔ Service ➔ dhcp-server ➔ dynamic-dns-update"
    * Enable: ✔

[a]: https://community.ui.com/questions/DNS-resolution-of-local-hosts/3b0a70d6-aefb-44a2-872e-e3703e757cd2
[b]: https://community.ui.com/questions/12901fe9-f520-49cc-99f7-12cbbc8d6aed
