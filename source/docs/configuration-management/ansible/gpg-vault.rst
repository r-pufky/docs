.. _ansible-gpg-vault:

Vault
#####
Vault is the built in encryption store for Ansible. GPG (and security key based
GPG keys) can be used to encrypt ansible data, enabling ansible deployments with
security key touches.

See :ref:`gpg-with-yubikey`.

.. code-block:: bash
  :caption: Generate a random vault password to use.

  pwgen -n 71 -C | head -n1 | gpg --armor --recipient {GPGID} -e -o ansible.gpg

.. _ansible-vault-rekey:

.. code-block:: bash
  :caption: Re-key existing vault data with new key if needed.

  grep -rl '^$ANSIBLE_VAULT.*' . | xargs -t ansible-vault rekey

.. literalinclude:: source/vault-gpg
  :caption: Create script to decrypt the password for use.

Set ansible configuration to use the script for password prompts.

.. code-block:: bash
  :caption: ``ansible.cfg``

  # If set, configures the path to the Vault password file as an alternative to
  # specifying --vault-password-file on the command line. This can also be
  # an executable script that returns the vault password to stdout.
  #
  vault_password_file = vault-gpg

`Reference <https://www.cloudsavvyit.com/3902/how-to-use-ansible-vault-to-store-secret-keys/>`__

`Reference <https://disjoint.ca/til/2016/12/14/encrypting-the-ansible-vault-passphrase-using-gpg/>`__
