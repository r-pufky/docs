.. _salt-gpg:

GPG Encrypt Pillar Data
#######################
### [Setup GPG][10]
[Alternative Reference][11]. [CLI Reference][19]

`/etc/salt/gpgkeys` is a required hard-coded directory. Ensure only the
salt-master user has access to this.

Note: salt-master requires no password for GPG decryption to work. Secure your
certs. You may want to enforce expiration on certs as well.

If entropy generation is slow (typical on VM's), install [`haveged`][18] to
speed up entropy collection.

.. code-block:: bash
  :caption: Generate GPG keys for salt-master encryption/decryption.

  mkdir -p /etc/salt/gpgkeys
  chmod 0700 /etc/salt/gpgkeys
  gpg --gen-key --homedir /etc/salt/gpgkeys

.. important::
   * use NO password for salt-master. secure your keys.
   * default option (RSA/RSA)
   * 4096 bit key
   * 0 (cert does not expire)
   * salty (salt@example.com)
   * no password.

.. code-block:: bash
  :caption: Export public key for signing data.

  gpg --homedir /etc/salt/gpgkeys --armor --export > public_key.gpg

``public_key.gpg`` is used by anyone on any system to created encrypted data
that only the server can read.

.. code-block:: bash
  :caption: Import the public key for signing (stored in ``~/.gnupg``).

  gpg --import public_key.gpg

.. _encrypting-data:

Encrypting Data
***************

.. note::
  The entire PGP block should be added to pillar, and the *blank vertical space*
  can be removed. ``salty`` is the name of the recipient of the data.

.. code-block:: bash
  :caption: Text.

  echo -n "super_secret_server_stuff" | gpg --armor --batch --trust-model always --encrypt --recipient salty

.. code-block:: bash
  :caption: Files.

  gpg --armor --batch --trust-model always --encrypt --recipient salty {FILE}

.. note::
  The contents of this file should be what is placed in pillar. It will be
  written as ``{FILE}.asc``.
* `salty` is the name of the recipient of the data (see GPG key creation).

.. _encrypt-shadow-passwords:

Encrypt Shadow Passwords
************************
The [salt user state documentation][20] recommends using `openssl passwd -1` to
generate a bash passwd hash. This **only hashes MD5**, modern distributuions of
linux hash **sha512**. Use the [python script][21] below to generate a _salted, sha512
hash_ in the correct format for consumption in `/etc/shadow`. Then just run that
through the GPG encryption to store in pillar.

_storing password hashes in pillar that are not additionally GPG encrypted is
probably a **BAD** idea._

.. code-block:: bash
  :caption: Using utility.

  apt install whois
  mkpasswd -m sha-512

.. code-block:: bash
  :caption: Python3 version.

  python3 -c "import crypt, getpass; print(crypt.crypt(getpass.getpass('password to hash: '), crypt.mksalt(crypt.METHOD_SHA512)))"

.. _add-to-pillar:

Add to Pillar
*************

Prefix any Pillar file using GPG encryped data with:
```yaml
#!yaml|gpg
```

Insert the GPG message block as the value for the key. Use a pipe (|) to denote
GPG message. Indentation matters.

```yaml
secret-stuff: |
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v2.0.22 (GNU/Linux)
  hQEMA4Pr9QJhL3umAQgAnZtS7lTyDR3kjr+VjCIADutmxyjrxbyaNnPEs3eJRi9G
  N6LtiFlUt24Jgdgupu/CG2IS815V0Vx3EbBknpNNwq0Yrs2joMnm92ZRv4AI6ZTo
  yQqGICetmBOS+vGk4jS8mj9qRjLamvPDOBPyNpKiRCFqu1TPKYw0a8xssO/j/pzW
  TJ39WsHXjtOWLkfYOaf7SKffYL9EsdU5tqXASe5UvjR1Gbj7wdjPl+vMZxRhzfOn
  YQ3fq3wNrGkuz2PpE7n77mmvYGVlXemw4o6tITZMa3MIFZqGTPbCCnh4OubqWGqd
  MtMNgPD2EeZ6wfEWkf1LGrrFy9POmdpssiU92J5dsNJQAdTAZVP4gtoyjWRtHJQB
  3FNarZY210P1o16s1n05ZbkVnz2FeZW/ClB6FqiewDe2EoXcVbXT5WgSZTHFi3mJ
  dFXQZGtReJL4vt8Iq8jSwRI=
  =wJ+K
  -----END PGP MESSAGE-----
some-other-key: data
```
* Blank lines between the begin/version and body can be removed.

#### Refresh Pillar and Push Data
Pillar will automatically refresh and push, however this allows you to
immediately regenerate pillar data and push new values to minions.

```bash
salt '*' saltutil.refresh_pillar
salt pillar.items
```
 * You should see the decrypted original text in the items list.

### Pillar Environment Data
By default data is merged and applied based on where the minion is defined in
top files. You can specify a specific environment (and are required to when
using `pillar_source_merging_strategy: none`) to get pillar values for that
environment:

```bash
pillarenv=dev
```

```bash
pillarenv=prod
```
