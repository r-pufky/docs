.. _apps-mutt:

Mutt Maildir Setup
##################
Local terminal texted based email client.

Ubunutu 16.04

Base mutt Setup
***************
This will setup mutt for use with Maildir, as well as subscribe to all folders
in Maildir.

.. code-block:: bash

  sudo apt install mutt

.. literalinclude:: source/.muttrc
  :caption: **0600 user user** ``~/.muttrc``
  :linenos:

.. rubric:: References

#. `Mutt maildir FAQ <http://dev.mutt.org/trac/wiki/MuttFaq/Maildir>`_
#. `Mutt maildir configuration <http://www.elho.net/mutt/maildir>`_
