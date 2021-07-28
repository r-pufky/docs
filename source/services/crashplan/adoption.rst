.. _service-crashplan-adoption:

Backup Set Adoption
###################
Previous backup sets from other machines may be adopted in place instead of
re-uploading all backup data. This applies for all crashplan installs.

* Start container.
* Sign in to your account.
* Click the Replace Existing button to start the wizard.
* **SKIP** File Transfer.
* Once done with the wizard, go to your device's details and click Manage
  Files. You will probably see missing items in the file selection. This
  is normal, since path to your files may be different in the container.
* Update the file selection by re-adding your files. Do not unselect
  missing items yet.
* Perform a backup. Because of deduplication, files will not be uploaded
  again.
* Once the backup is terminated, you can remove missing items if you
  don't care about file versions. Else, keep missing items.

`Reference <https://support.code42.com/CrashPlan/6/Configuring/Replace_your_device>`__
