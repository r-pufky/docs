# Troubleshooting

## Regenerate ACME (letsecnrypt) Certificates
Valid certificates (including test certificates) will only be updated on expiry
or if they are removed.

Remove ACME certs in **data/acme**. Directory must be owned by **mox**. Update
**mox.conf** and restart service.

## Mail Import Fails
Spam and Junk filters will prevent import if no spam message counts are found.

!!! danger ""
    importing...
    import, expected ok, got "open junk filter: looking up ham/spam message count: absent"

!!! abstract "localhost:8080/webmail ➔ login ➔ account"
    * automatic junk flags: ✘
    * junk filter: ✘

Restart import and re-enable when import is done.

## Reverse names do not match hostname
ISP's generally control reverse DNS lookups.

!!! danger ""
    WARNING: reverse name(s) {IP}.bvtn.or.ptr.{DOMAIN} for ip {IP} do not match hostname mail.example.com, which will cause other mail servers to reject incoming messages from this IP.

Mail may still be received but sending mail likely will be rejected. Move mail
server to a hosted solution where reverse DNS lookups are controlled.

## Connecting to gmail-smtp-in.l.google.com dial tcp i/o timeout
Outgoing SMTP connection failed.

!!! tip "This is OK if not sending mail"

!!! danger ""
    ERROR: connecting to gmail-smtp-in.l.google.com.:25: dial tcp {IP}:25: i/o timeout

    WARNING: Could not verify outgoing smtp connections can be made, outgoing
    delivery may not be working. Many providers block outgoing smtp connections
    by default, requiring an explicit request or a cooldown period before 
    allowing outgoing smtp connections. To send through a smarthost, configure
    a "Transport" in mox.conf and use it in "Routes" in domains.conf. See
    "mox config example transport".
