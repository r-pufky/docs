.. _gpg-subkeys:

Generate Subkeys
################
Subkeys are issued from the master key and are used for specific actions *on
behalf of* the master identity. These subkeys are loaded onto Yubikeys for
everyday use. As they are subkeys, these can be revoked as needed or the master
key can be revoked/changed to invalidate all subkeys at once.

If the subkeys will not be stored on a self-destructing device when attacked
(e.g. a Yubikey), then **set an expiry date**.

Create :term:`Signing Key`
**************************
.. code-block:: bash
  :emphasize-lines: 1,3,15,17,25,27-28,37-38,41

  $ gpg --expert --edit-key $KEYID

  gpg> addkey
  Please select what kind of key you want:
     (3) DSA (sign only)
     (4) RSA (sign only)
     (5) Elgamal (encrypt only)
     (6) RSA (encrypt only)
     (7) DSA (set your own capabilities)
     (8) RSA (set your own capabilities)
    (10) ECC (sign only)
    (11) ECC (set your own capabilities)
    (12) ECC (encrypt only)
    (13) Existing key
  Your selection? 4
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
  Really create? (y/N) y
  We need to generate a lot of random bytes. It is a good idea to perform
  some other action (type on the keyboard, move the mouse, utilize the
  disks) during the prime generation; this gives the random number
  generator a better chance to gain enough entropy.

  sec  rsa4096/################
      created: 2019-01-01  expires: never       usage: C
      trust: ultimate      validity: ultimate
  ssb  rsa4096/################
      created: 2019-01-01  expires: never       usage: S
  [ultimate] (1). FIRST LAST <EMAIL>

  gpg> save

Create :term:`Encryption Key`
*****************************
.. code-block:: bash
  :emphasize-lines: 1,3,9,11,19,21-22,33-34,37

  $ gpg --expert --edit-key $KEYID

  gpg> addkey
  Please select what kind of key you want:
     (3) DSA (sign only)
     (4) RSA (sign only)
     (5) Elgamal (encrypt only)
     (6) RSA (encrypt only)
  Your selection? 6
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
  Really create? (y/N) y
  We need to generate a lot of random bytes. It is a good idea to perform
  some other action (type on the keyboard, move the mouse, utilize the
  disks) during the prime generation; this gives the random number
  generator a better chance to gain enough entropy.

  sec  rsa4096/################
      created: 2019-01-01  expires: never       usage: C
      trust: ultimate      validity: ultimate
  ssb  rsa4096/################
      created: 2019-01-01  expires: never       usage: S
  ssb  rsa4096/################
      created: 2019-01-01  expires: never       usage: E
  [ultimate] (1). FIRST LAST <EMAIL>

  gpg> save

Create :term:`Authentication Key`
*********************************
.. code-block:: bash
  :emphasize-lines: 1,3,15,25,27,35,37-38,51-52,55

  $ gpg --expert --edit-key $KEYID

  gpg> addkey
  Please select what kind of key you want:
     (3) DSA (sign only)
     (4) RSA (sign only)
     (5) Elgamal (encrypt only)
     (6) RSA (encrypt only)
     (7) DSA (set your own capabilities)
     (8) RSA (set your own capabilities)
    (10) ECC (sign only)
    (11) ECC (set your own capabilities)
    (12) ECC (encrypt only)
    (13) Existing key
  Your selection? 8

  Possible actions for a RSA key: Sign Encrypt Authenticate
  Current allowed actions: Sign Encrypt

     (S) Toggle the sign capability
     (E) Toggle the encrypt capability
     (A) Toggle the authenticate capability
     (Q) Finished

  Your selection? =a
  RSA keys may be between 1024 and 4096 bits long.
  What keysize do you want? (3072) 4096
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
  Really create? (y/N) y
  We need to generate a lot of random bytes. It is a good idea to perform
  some other action (type on the keyboard, move the mouse, utilize the
  disks) during the prime generation; this gives the random number
  generator a better chance to gain enough entropy.

  sec  rsa4096/################
       created: 2019-01-01  expires: never       usage: C
       trust: ultimate      validity: ultimate
  ssb  rsa4096/################
       created: 2019-01-01  expires: never       usage: S
  ssb  rsa4096/################
       created: 2019-01-01  expires: never       usage: E
  ssb  rsa4096/################
       created: 2019-01-01  expires: never       usage: A
  [ultimate] (1). FIRST LAST <EMAIL>

  gpg> save

Verify Keys Are Secure
**********************
Highlight any potential concern areas with generated keys. These should appear
green with exceptions for the authentication subkey.

.. code-block:: bash

  gpg --export $KEYID | hokey lint

.. note::
  **Red** text indicates potential problems. Non-expiring keys will be marked as
  red; setting expiry is based on your security decisions.

  **Orange** text indicates warnings. This is typically seen as a missing
  embedded cross-certificate for the **authentication** subkey. The GPG
  authentication subkey does not sign and does not need to be cross-certified.

Verify GPG Password
*******************
There is no built in method to confirm a GPG password is correct. Verification
of passsword happens by checking the exit code and printing 'Correct' if the
command succeeded.

.. code-block:: bash
  :caption: Verify GPG password works.

  echo '1234' | gpg --batch --passphrase-fd 1 -o /dev/null --local-user $KEYID -as - && echo 'Correct.'

.. _Comments are considered harmful: https://debian-administration.org/users/dkg/weblog/97
.. _instructions here: http://blog.josefsson.org/2014/06/19/creating-a-small-jpeg-photo-for-your-openpgp-key/
.. _protecting the master key: https://security.stackexchange.com/questions/14718/does-openpgp-key-expiration-add-to-security/79386