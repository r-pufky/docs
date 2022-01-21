.. _w10-21h2:

.. _w10-latest:

Windows 10 21H2
###############
See :ref:`wbase-pro-install` for initial Windows setup.

* `Notable changes <https://en.wikipedia.org/wiki/Windows_10_version_history#Version_21H2_(November_2021_Update)>`__
* `Release information <https://docs.microsoft.com/en-us/windows/release-health/status-windows-10-21h2>`__
* `Technical notes <https://docs.microsoft.com/en-us/windows/whats-new/whats-new-windows-10-version-21H2>`__
* `Shortcut keys <https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec>`__

.. important::
  :term:`GPO` should be thought of a template framework that applies specific
  Registry changes based on specific conditions at the user, computer and domain
  level. :term:`Registry` changes are extremely specific and apply to the user
  or computer. Recent updates with Windows have been pushing more and more GPO
  policies to only work in ``Education`` and ``Enterprise`` versions.

  :term:`Registry` policies are only used when there are no specific GPO
  polices that can be applied. Only settings that have been changed or are
  deemed important are listed. Apply based on your personal preferences.
  Registry settings may be found in reference material if provided.

  A reboot is required once these changes are made.

.. note::
  Any unlisted section/change assumes default settingss.

.. toctree::
   :maxdepth: -1

   standalone/index
   settings/index
   security/index
