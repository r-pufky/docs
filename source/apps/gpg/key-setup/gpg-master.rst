.. _gpg-master:

GPG Master Key
##############
The GPG Master Key is your digital identity and should be kept **offline** and
**encrypted** per :ref:`gpg-prerequisites`. Subkeys are used for everyday use.

GPG 2.1 and higher will automatically create a revocation certificate in
``$GNUPGHOME/openpgp-revocs.d``. Using the revocation certificate is better
mechanism than an expiry date for `protecting the master key`_.

.. danger::
  Ensure machine is **air-gapped** (no transmission devices on) during this
  setup.

Basic Setup
***********
Setup GPG to store configuration on encrypted storage and setup secure
cross-platform preferences.

#. Run through :ref:`gpg-prerequisites`.
#. Run through :ref:`gpg-prep-yubikey`.

.. code-block:: bash
  :caption: Environment Variables & Base Directory Structure (on encrypted
            container).

  mkdir /media/user/KINGSTON/gnupghome
  mkdir -p /media/user/KINGSTON/backup/public /media/user/KINGSTON/backup/private
  export GNUPGHOME=/media/user/KINGSTON/gnupghome
  export GPGBACKUP=/media/user/KINGSTON/backup

* ``GNUPGHOME`` directs gpg where to find key material.
* ``GPGBACKUP`` location of backups of key material.
* ``public`` and ``private`` will be used to store respective key and cert
  material.

.. literalinclude:: source/gpg.conf
  :caption: **0600 user user** ``/media/user/KINGSTON/gnupghome/gpg.conf``
  :linenos:

.. note::
  This configures GPG with the following settings:

   * Require cipher AES 256, 192, 128.
   * Require digest SHA 512, 384, 256.
   * Public preferences for cipher/digest, compression.
   * Force our digest creation to SHA512.
   * Force our cipher to AES256.
   * Enable UTF-8 support (for cross platform usage).
   * Fixed list - use unixtimestamps for all timestamps and do not merge id/key.
   * Do not include comments in signature.
   * Do not include version in signature.
   * Require long hexidecimal keys.
   * Show UID validity for listing and verification options.
   * List fingerprints with keys.
   * Ensure cross certification on subkey is present and valid (prevents attack).
   * Enable smartcard use.

Generate Strong Password
************************
Generate a strongly-random password for use with the GPG master key. Doing
actions on the system will slowly increase the entropy pool.

.. code-block:: bash
  :caption: Ensure entropy pool is larger than 3000.

  cat /proc/sys/kernel/random/entropy_avail

.. code-block:: bash
  :caption: Generate a random 64 bit ACSII safe sequence for GPG password.

  gpg --gen-random --armor 0 64

.. note::
  Use this password when generating the Master GPG Key below. Store it in a
  physically separate location from where the offline Master Key is stored. This
  **protects your digital identity**.

Create Master Key
*****************
.. code-block:: bash
  :caption: Generate a 4096bit RSA with authenticate (certify) abilities only.
  :emphasize-lines: 1,14,24,26,34,36,39-41,45,48-49,62

  $ gpg --expert --full-generate-key

  Please select what kind of key you want:
     (1) RSA and RSA (default)
     (2) DSA and Elgamal
     (3) DSA (sign only)
     (4) RSA (sign only)
     (7) DSA (set your own capabilities)
     (8) RSA (set your own capabilities)
     (9) ECC and ECC
    (10) ECC (sign only)
    (11) ECC (set your own capabilities)
    (13) Existing key
  Your selection? 8

  Possible actions for a RSA key: Sign Certify Encrypt Authenticate
  Current allowed actions: Sign Certify Encrypt

     (S) Toggle the sign capability
     (E) Toggle the encrypt capability
     (A) Toggle the authenticate capability
     (Q) Finished

  Your selection? =c
  RSA keys may be between 1024 and 4096 bits long.
  What keysize do you want? (2048) 4096
  Requested keysize is 4096 bits
  Please specify how long the key should be valid.
           0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
  Key is valid for? (0) 0
  Key does not expire at all
  Is this correct? (y/N) y
  GnuPG needs to construct a user ID to identify your key.

  Real name: {USER FIRST NAME} {USER LAST NAME}
  Email address: {GPG USER EMAIL ADDRESS}
  Comment: {PRESS ENTER}
  You selected this USER-ID:
      "FIRST LAST <EMAIL>"

  Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
  You need a Passphrase to protect your secret key.

  Enter passphrase: {GPG PASSWORD}
  Repeat passphrase: {GPG PASSWORD}

  We need to generate a lot of random bytes. It is a good idea to perform
  some other action (type on the keyboard, move the mouse, utilize the
  disks) during the prime generation; this gives the random number
  generator a better chance to gain enough entropy.

  gpg: /media/user/KINGSTON/gnupghome/trustdb.gpg: trustdb created
  gpg: key ################ marked as ultimately trusted
  gpg: directory '/media/user/KINGSTON/gnupghome/openpgp-revocs.d' created
  gpg: revocation certificate stored as '/media/user/KINGSTON/gnupghome/openpgp-revocs.d/########################################.rev'
  public and secret key created and signed.

  pub   rsa4096/################ 2019-01-01 [C]
        Key fingerprint = #### #### #### #### ####  #### #### #### #### ####
  uid                              FIRST LAST <EMAIL>

.. note::
  * ``=c`` forces certify only and moves to next prompt.
  * `Comments are considered harmful`_ and explicitly left blank.
  * Revocation certificate will be listed in output.
  * Master Key ID will be listed under ``pub  rsa4096/################``.
  * See :ref:`gpg-troubleshooting` if an error occurs.

.. code-block:: bash
  :caption: Export master key ID to bash environment for easy reference later.

  export KEYID=################

Add Photo to Master Key (Optional)
**********************************
A photo to help confirm your identity (typically a headshot); this is added to
your GPG key for additional verification in person.

Create a **240x288 JPEG** photo (max **6144 bytes**) with metadata information
removed, `instructions here`_.

.. code-block:: bash
  :emphasize-lines: 1,3,10-11,13

  gpg --edit-key $KEYID

  gpg> addphoto

  Pick an image to use for your photo ID. The image must be a JPEG file.
  Remember that the image is stored within your public key. If you use a very
  large picture, your key will become very large as well! Keeping the image
  close to 240x288 is a good size to use.

  Enter JPEG filename for photo ID: photo.jpg
  Is this correct? (y/N) y

  gpg> save

Add Additional Identities (Optional)
************************************
Associate additional metadata to GPG key, useful if you have multiple emails,
etc.

.. code-block:: bash
  :emphasize-lines: 1,3,5-7,11,13-15

  $ gpg --edit-key $KEYID

  gpg> adduid

  Real name: {USER FIRST NAME} {USER LAST NAME}
  Email address: {GPG USER EMAIL ADDRESS}
  Comment: {PRESS ENTER}
  You selected this USER-ID:
      "FIRST LAST <EMAIL>"

  Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

  gpg> uid 1
  gpg> primary
  gpg> save

.. note::
  The ``primary`` ID is the main identity used for the GPG key. This can be any
  identity that has been configured, in this case **1**.

  * `Comments are considered harmful`_ and explicitly left blank.

Sign New Key with Existing Key (Optional)
*****************************************
This will extend the chain of trust and prove that the new key is controlled by
your original key (you). Useful for when the master key is compromised or
expired.

The new key is exported and signed by the old key, then published.

.. code-block:: bash
  :caption: Export new key and sign with old key.

  gpg --export-secret-keys --armor --output /tmp/new-gpg-key.asc
  gpg --default-key $OLDKEY --sign-key $KEYID

.. _Comments are considered harmful: https://debian-administration.org/users/dkg/weblog/97
.. _instructions here: https://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key/
.. _protecting the master key: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386
