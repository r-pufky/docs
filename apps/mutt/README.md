Mutt Maildir Setup
------------------
Local terminal texted based email client.

Ubunutu 16.04


Base mutt Setup
---------------
This will setup mutt for use with Maildir, as well as subscribe to all folders
in Maildir.

```bash
sudo apt install mutt
```

#### ~/.muttrc
```config
set mbox_type=Maildir
set spoolfile="~/Maildir/"
set folder="~/Maildir/"
set mask=".*"
set record="+.Sent"
set postponed="+.Drafts"

# Generate mailboxes for each maildir subdir
mailboxes ! + `\
for file in ~/Maildir/.*; do \
  box=$(basename "$file"); \
  if [ ! "$box" = '.' -a ! "$box" = '..' -a ! "$box" = '.customflags' \
      -a ! "$box" = '.subscriptions' ]; then \
   echo -n "\"+$box\" "; \
  fi; \
done`

# Marcos to display folder list when changing maildir folders
macro index c "<change-folder>?<toggle-mailboxes>" "open a different folder"
macro pager c "<change-folder>?<toggle-mailboxes>" "open a different folder"

# Macros to display folder list when copying/moving messages
macro index C "<copy-message>?<toggle-mailboxes>" "copy a message to a mailbox"
macro index M "<save-message>?<toggle-mailboxes>" "move a message to a mailbox"
```

[1]: http://dev.mutt.org/trac/wiki/MuttFaq/Maildir
[2]: http://www.elho.net/mutt/maildir
