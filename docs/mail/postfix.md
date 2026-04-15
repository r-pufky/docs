# Postfix
Email testing for classic postfix stack.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.mox][a].

    The classic postfix stack has been archived:
    https://github.com/r-pufky/ansible_mail


## Verify Services Locked Down
``` bash
# Test SASL service.
telnet localhost 25
ehlo localhost

# Should see '250 auth plain login' after issuing command. This means that SASL
# dovecot is setup correctly.

# Press 'ctrl + ]' to quit.
```

### Verify non-encrypted connections fail
``` bash
telnet localhost 143  # IMAP
telnet localhost 110  # POP
telnet localhost 995  # POP

# All unencrypted connections should fail with: Unable to connect to remote
# host: Connection refused.

# Verify IMAPS connections succeed.
``` bash
openssl s_client -connect localhost:993

# Should get '* OK [{CAPABILITY LIST}] Dovecot ready'. Verify the certificate
# listed is the correct Let's Encrypt certificate for the domain used.

# 'C logout {ENTER}' to quit.
```

### Verify encrypted SMTP connections succeed
``` bash
openssl s_client -starttls smtp -crlf -connect localhost:587

# Verify the certificate listed is the correct Let's Encrypt certificate for
# domain used.

# 'crtl + c' to quit.
```


## Test Email Delivery
Ensure that users can receive mail. Test for users and alias cases.

!!! tip
    **{USER}** and **{PASS}** should be base64 encoded.

### Telnet SMTP and send test emails
``` bash
telnet localhost 25
ehlo localhost
auth login  # Should recieve 220.
VXNlcm5hbWU6
{USER}
UGFzc3dvcmQ6
{PASS}
mail from: root@localhost
rcpt to: {USER}@{DOMAIN}
data
Subject: postfix text
testing mail from postfix
.
quit
```

### [Verify SSL/TLS SMTP can send][b]
``` bash
openssl s_client -starttls smtp -crlf -connect mail.{DOMAIN}:587
ehlo mail.{DOMAIN}
auth login  # Should recieve 220.
VXNlcm5hbWU6
{USER}
UGFzc3dvcmQ6
{PASS}
mail from: root@localhost
rcpt to: {USER}@{DOMAIN}
data
Subject: postfix text
testing mail from SSL/TLS SMTP
.
quit
```


## Verify Proper Mail Configuration
Tests must be green or the mail server will be blacklisted by major email
services.

Use https://mxtoolbox.com to validate settings and ensure ports (25,587) are
exposed for testing.

1. Test **{DOMAIN}** and **`mail.{DOMAIN}** MX records.
    * All results **must** be green.
    * The correct IP must be shown.

* **SMTP Test** after looking up the MX record.
    * All results **must** be green, except **PTR** lookup.

!!! note
    The **PTR** record maps an IP address to a DNS name. This is used by
    **other** mail servers to verify mail received from your server is a valid
    email.

    This **must** be green if there is **any** intent to send mail to other
    services. Your [ISP generally controls this][c], which implies that you
    have your ISP set this up for you or setup a hosted solution where you
    control the IP space.

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: https://support.sugarcrm.com/Knowledge_Base/Email/Testing_Outbound_Email_Using_Command_Line
[c]: https://community.spiceworks.com/topic/405534-dns-ptr-record-issues
