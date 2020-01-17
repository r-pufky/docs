require "fileinto";
require "vacation";

# Automatically move flagged spam to spam folder
if header :contains "X-Spam-Flag" "YES" {
  fileinto "spam";
  stop;
}

# Allow email-update@{DOMAIN} to be delivered.
if address :is "to" "email-update@{DOMAIN}" {
  keep;
  stop;
}

# Autorespond with CM deprecation, send to special mailbox.
if address :is :domain "to" "{DOMAIN}" {
  fileinto "email-update";
  vacation
    :days 1
    :addresses "email-update@{DOMAIN}"
    :subject "[Action Required]: Your contact information is out of date."
    text:
You've recently sent an email to {DOMAIN}, which is no longer used.

Please request updated contact information by mailing:

  email-update@{DOMAIN}

and you'll receive new contact information. Please delete any current
{DOMAIN} email addresses you have, as these are now invalid.

.

;
}
