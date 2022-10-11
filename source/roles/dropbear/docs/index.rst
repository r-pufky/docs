.. _service-dropbear:

Dropbear
########
Remote unlock encrypted root filesystems over SSH on boot.

Note that most systems do not encrypt ``/boot`` and therefore dropbear keys
should be considered compromised/untrusted; use separate keys when using
dropbear!

See :ref:`service-wireguard-initramfs` to enable wireguard service on boot for
fully encrypted remote boot root FS unlock.

.. role:: dropbear
  :galaxy:      https://galaxy.ansible.com/r_pufky/dropbear
  :source:      https://github.com/r-pufky/ansible_dropbear
  :service_doc: https://linuxconfig.org/how-to-install-and-configure-dropbear-on-linux
  :update:      2022-10-08
  :open:

  * Dropbear host identification keys are a special format, not a standard SSH
    keypair. See: :ref:`service-dropbear-defaults`.
  * Dropbear host keys are binary files and cannot be stored encrypted in the
    {host,group}_vars directory. Ansible will try to automtically decrypt this
    file and fail due to UTF-8 encoding issues. Storing within ansible but
    outside of {host,group}_vars to prevent decryption until the binary file is
    copied, wherein the decryption happens correctly.
  * Remote Unlock using the dropbear key
    ``ssh -i ~/.ssh/dropbear root@remote_host``.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

.. _service-dropbear-defaults:

Defaults
********
.. literalinclude:: ../defaults/main.yml
