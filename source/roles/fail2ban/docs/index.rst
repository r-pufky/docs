.. _service-fail2ban:

Fail2Ban
########
Automatically ban repeated failed authentication attempts.

.. toctree::
   :hidden:
   :maxdepth: -1

   custom-filters
   common-commands
   troubleshooting

.. role:: fail2ban
  :service_doc: https://github.com/fail2ban/fail2ban
  :ref:         https://www.digitalocean.com/community/tutorials/how-to-protect-an-nginx-server-with-fail2ban-on-ubuntu-14-04
  :update:      2022-10-10
  :private:
  :open:

  Role handles all steps that are provided in this documentation.

  * All base action, filter, and jail provided by the Debian are included for
    use in the role by default.
  * Custom definitions may be provided with ``fail2ban_filterd_path``,
    ``fail2ban_actiond_path``, and ``fail2ban_jaild_path``.

Defaults
********
.. literalinclude:: ../defaults/main.yml
