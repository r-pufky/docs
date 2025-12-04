# Troubleshooting

## Reverse names do not match hostname
ISP's generally control reverse DNS lookups.

!!! danger ""
    WARNING: reverse name(s) {IP}.bvtn.or.ptr.{DOMAIN} for ip {IP} do not match hostname mail.example.com, which will cause other mail servers to reject incoming messages from this IP.

Mail may still be received but sending mail likely will be rejected. Move mail
server to a hosted solution where reverse DNS lookups are controlled.

## Connecting to gmail-smtp-in.l.google.com dial tcp i/o timeout
Outgoing SMTP connection failed.

!!! danger ""
    ERROR: connecting to gmail-smtp-in.l.google.com.:25: dial tcp {IP}:25: i/o timeout


WARNING: Could not verify outgoing smtp connections can be made, outgoing
delivery may not be working. Many providers block outgoing smtp connections by
default, requiring an explicit request or a cooldown period before allowing
outgoing smtp connections. To send through a smarthost, configure a "Transport"
in mox.conf and use it in "Routes" in domains.conf. See
"mox config example transport".


``` bash
NOTE: Quickstart used the IPs of the host name of the mail server, but only
found private IPs on the machine. This indicates this machine is behind a NAT,
so the host IPs were configured in the NATIPs field of the public listeners. If
you are behind a NAT that does not preserve the remote IPs of connections, you
will likely experience problems accepting email due to IP-based policies. For
example, SPF is a mechanism that checks if an IP address is allowed to send
email for a domain, and mox uses IP-based (non)junk classification, and IP-based
rate-limiting both for accepting email and blocking bad actors (such as with too
many authentication failures).
```