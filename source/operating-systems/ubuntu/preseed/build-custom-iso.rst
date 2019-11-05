.. _preseed-build-custom-iso:

Build Custom ISO
################

.. code-block:: bash
  :caption: Copy preseed configuration and any post-install scripts to ISO
            image.

  cp ubuntu-preseed.seed custom-iso/preseed/ubuntu-preseed.seed
  cp -av post-install custom-iso/

.. note::
  Ensure that the modified boot menus have been copied to the ISO image if not
  modified directly.

Take the existing multi-boot (EFI/non-EFI) image from the iso and reuse it to
create the new ISO image:

.. code-block:: bash
  :caption: Extract existing isohdpfx.bin for multi-boot (EFI/non-EFI) ISO
            image.

  sudo dd if=<ubuntu>.iso bs=512 count=1 of=custom-iso/isolinux/isohdpfx.bin

.. code-block:: bash
  :caption: Rehash MD5 sums for file integrity checks.

  cd custom-iso
  md5sum $(find -type f) > md5sum.txt

.. code-block:: bash
  :caption: Make new ISO image and checksum it.

  cd custom-iso
  sudo xorriso -as mkisofs -isohybrid-mbr isolinux/isohdpfx.bin -c isolinux/boot.cat -b isolinux/isolinux.bin -no-emul-boot -boot-load-size 4 -boot-info-table -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -o ../custom-ubuntu.iso .
  cd ..
  sha512sum custom-ubuntu.iso > custom-ubuntu.sha512sum
  sha512sum -c custom-ubuntu.sha512sum

.. code-block:: bash
  :caption: Ensure both non-EFI and EFI partitions show.
  :emphasize-lines: 4,5

  fdisk -l custom-ubuntu.iso

  Device             Boot Start     End Sectors  Size Id Type
  custom-ubuntu.iso1 *        0 1763327 1763328  861M  0 Empty
  custom-ubuntu.iso2       4028    8763    4736  2.3M ef EFI (FAT-12/16/32)

.. note::
  ``iso1`` and ``iso2`` presence will confirm there is an EFI and non-EFI ISO in
  the image.