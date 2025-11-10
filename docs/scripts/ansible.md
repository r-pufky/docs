# Ansible
Development documentation located at
https://r-pufky.github.io/ansible_collection_docs.

Roles are self-documented:
[https://github.com/r-pufky/ansible_*](https://github.com/r-pufky).

## Vault
Vault is the built in encryption store for Ansible. GPG (and security key based
GPG keys) can be used to encrypt ansible data, enabling ansible deployments with
security key touches.

### Generate a random vault password to use
``` bash
pwgen -n 71 -C | head -n1 | gpg --armor --recipient {GPGID} -e -o ansible.gpg

# Re-key existing vault data with new key if needed.
grep -rl '^$ANSIBLE_VAULT.*' . | xargs -t ansible-vault rekey
```

### Create script to decrypt the password for use
**vault-gpg** (1)
{ .annotate }

1. 0755 {USER}:{USER}

``` bash
#!/bin/sh
#
# See: https://disjoint.ca/til/2016/12/14/encrypting-the-ansible-vault-passphrase-using-gpg/
#      https://www.cloudsavvyit.com/3902/how-to-use-ansible-vault-to-store-secret-keys/
#
# pwgen -n 71 -C | head -n1 | gpg --armor --recipient {GPG ID} -e -o ansible.gpg
#
gpg --batch --use-agent --decrypt ../cfg/ansible/ansible.gpg
```

**ansible.cfg** (1)
{ .annotate }

1. 0644 {USER}:{USER}

``` bash
# If set, configures the path to the Vault password file as an alternative to
# specifying --vault-password-file on the command line. This can also be
# an executable script that returns the vault password to stdout.
#
vault_password_file = vault-gpg
```

## Reference

* https://www.cloudsavvyit.com/3902/how-to-use-ansible-vault-to-store-secret-keys
* https://disjoint.ca/til/2016/12/14/encrypting-the-ansible-vault-passphrase-using-gpg
