require "fileinto";
require "vacation";

# Automatically move flagged spam to spam folder
if header :contains "X-Spam-Flag" "YES" {
  fileinto "spam";
  stop;
}

# Allow specific addresses to domain to be delivered.
if address :is "to" "user@exmaple.com" {
  keep;
  stop;
}

# Autorespond for all other domain mails, and drop into special delivery folder.
# In this example, we are notifying people of new email address.
if address :is :domain "to" "example.com" {
  fileinto "example-domain-filter";
  vacation
    :days 1
    :addresses "alt-email@example.com"
    :subject "[Action Required]: Your contact information is out of date."
    text:
You've recently sent an email to example.com, which is no longer used.

Please request updated contact information by mailing:

  alt-email@example.com

and you'll receive new contact information. Please delete any current
example.com email addresses you have, as these are now invalid.

.

;
}
