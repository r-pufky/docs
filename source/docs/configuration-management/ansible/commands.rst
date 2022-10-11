.. _ansible-commands:

Common Commands
###############

Grab Remote Facts from Host
***************************
No ansible setup is required. ``-K`` will force prompts for become if ineeded.

.. code-block:: bash

  ansible {HOST} -m ansible.builtin.setup -K -u {SSH USER}
