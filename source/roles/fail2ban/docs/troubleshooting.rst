.. _service-fail2ban-troubleshooting:

fail2ban Troubleshooting
########################

Bans Not Triggering
*******************
This is due to either invalid regex filters, timezone differences in logs and
``fail2ban`` container, or database wonkiness.

.. code-block:: bash
  :caption: Ensure regex filter is actually catching known bannable attempts.

  fail2ban-regex /path/to/log.log /etc/fail2ban/filter.d/my-filter.conf

.. note::
  If there are known lines that should be caught, these should appear in the
  output as ``matched``.

.. code-block:: bash
  :caption: Ensure regex filter is loaded properly.

  fail2ban-client --dp

.. note::
  This will show the loaded filters and jails. They should match your config.

  Restart the service to reload if different.

.. code-block:: bash
  :caption: Reset fail2ban state.

  fail2ban-client unban --all
  rm /var/lib/fail2ban/fail2ban.sqlite3

.. note::
  Sometimes the DB gets in a weird state where actions are not triggered. This
  will reset fail2ban to a default state (including the database) and actions
  should be triggered again.