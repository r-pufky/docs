.. _w10-20h2:

Windows 10 20H2
###############
See :ref:`wbase-pro-install` for initial Windows setup.

* `Notable changes <https://en.wikipedia.org/wiki/Windows_10_version_history#Version_20H2_(October_2020_Update)>`__
* `Release information <https://docs.microsoft.com/en-us/windows/release-information/status-windows-10-20H2>`__
* `Technical notes <https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-20H2>`__
* `Shortcut keys <https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec>`__

.. important::
  :term:`GPO` should be thought of a template framework that applies specific
  Registry changes based on specific conditions at the user, computer and domain
  level. :term:`Registry` changes are extremely specific and apply to the user
  or computer.

  Always prefer :term:`GPO` over :term:`Registry` edits where multiple options
  are provided; but apply both as recent updates with Windows have been pushing
  more and more GPO policies to only work in ``Education`` and ``Enterprise``
  versions.

  A reboot is required once these changes are made.

.. note::
  Any unlisted section/change assumes default settingss.

.. toctree::
   :maxdepth: -1

   standalone/index
   settings/index
   security/index
