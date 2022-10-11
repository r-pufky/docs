.. _service-fail2ban-common-commands:

Common Commands
###############

Show Overall Ban Status
***********************
.. code-block:: bash

  fail2ban-client status

Show Specific Jail Bans
***********************
.. code-block:: bash

  fail2ban-client status {F2B JAIL NAME}

Unban an IP
***********
.. code-block:: bash

  fail2ban-client set {F2B JAIL NAME} unbanip {IP}

Unban all IPs
*************
.. code-block:: bash

  fail2ban-client unban --all

Show Current Config Value
*************************
.. code-block:: bash

  fail2ban-client get {F2B JAIL NAME} {CONFIG SETTING}

Show iptables Rules
*******************
.. code-block:: bash

  iptables -S
