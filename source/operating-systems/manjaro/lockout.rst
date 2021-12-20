.. _manajaro-kde-lockout:

Increase Failed auth Lockout Attempts
#####################################
Manjaro will lockout a user for 10 minutes on 3 failed password attempts over
15 minutes. Expressed as sudo not working with valid password or unable to
login to the system.

Allow **5** attempts within **5** minutes, lockout for **10** minutes.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/security/faillock.conf``

  deny = 5
  fail_interval = 300
  unlock_time = 600
