# Troubleshooting

## UTF-8 codec can't encode characters ... surrogates not allowed
Dropbear host keys are binary files and not standard OpenSSH keypairs. Older
Python/Ansible versions cannot handle these key correctly.

!!! danger ""
    ERROR! 'utf-8' codec can't encode characters in position 23-24: surrogates
           not allowed

Upgrade to Ansible 2.20 and a recent Python version. Ansible 2.19 is considered
a breaking change therefore if you are upgrading one, upgrade the other.

!!! tip "I must use Ansible <2.18 or older Python versions"
    Dropbear keys cannot be stored encrypted in {host,group}_vars directory.
    Ansible will try to [automatically decrypt][a] this file and fail due to
    UTF-8 encoding issues on older versions.

    Storing within ansible but outside of {host,group}_vars to prevent
    decryption until the binary file is copied, wherein the decryption happens
    correctly.

[a]: https://github.com/ansible/ansible/issues/79053
