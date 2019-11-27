.. _gpg-cleanup:

GPG Cleanup
###########
Manually verify this information to ensure you do not accidently lose data or
access/control to your GPG identity.

Verify the Following
********************
#. Encrypted Media has the following:

   * ``$GPGBACKUP/private/$KEYID.master.asc``
   * ``$GPGBACKUP/private/$KEYID.subkeys.asc``
   * ``$GPGBACKUP/private/$KEYID.rev``
   * ``$GPGBACKUP/public/$KEYID.asc``
   * ``$GPGBACKUP/public/$KEYID.ssh.pub``

#. A backup of GPG Master Key (with all keys locally present):

   * ``$GPGBACKUP/gnupghome``

#. Your Master Key password is stored **away** from your encrypted media, in a
   controlled space.
#. Your Encrypted Media password is stored **away** from your encrypted media,
   in a controlled space.
#. **The encrypted media is stored offline, in a controlled space.**
#. The public keys are stored or published, and are readily accessible.

   * ``$GPGBACKUP/public/*``

#. It is generally a good idea to print a copy of the revocation certificate and
   give it to a trusted third-party.

Secure Delete Secret Material
*****************************
Securely remove any secret GPG material.

If you are using a Live OS, just reboot. If you're paranoid, wipe the live OS
drive.

If not using a live OS, wipe private key material **after** you confirm it is
backed up.

.. code-block:: bash

  sudo srm -r $GNUPGHOME || sudo rm -rf $GNUPGHOME
  sudo srm -r $GPGBACKUP || sudo rm -rf $GPGBACKUP
  gpg --delete-secret-key $KEYID