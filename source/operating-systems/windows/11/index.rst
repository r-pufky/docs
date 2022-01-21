.. _w11-21h2:

.. _w11-latest:

Windows 11 21H2
###############
Download `full windows 11 ISO image with <https://www.microsoft.com/software-download/windows11>`__

.. warning::
  Currently a work in progress and not complete. Many Windows 10 settings have
  changed locations and options.

  There are many non-trivial performance hits due to increase attack mitigation
  and requires a TPM and a recent processor. With a noted increase in password
  lockout during updates.

  **Highly** recommend letting 11 bake for another year before seriously
  attempting to use it. Windows 10 is supported to `2025-10-14 <https://docs.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro>`__.

* `System requirements <https://www.microsoft.com/en-us/windows/windows-11-specifications?r=1>`__
* `Notable changes <https://en.wikipedia.org/wiki/Windows_11_version_history#Version_21H2>`__
* `Release information <https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2>`__
* `Technical notes <https://docs.microsoft.com/en-us/windows/whats-new/windows-11-whats-new>`__
* `Shortcut keys <https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec>`__

.. important::
  :term:`GPO` should be thought of a template framework that applies specific
  Registry changes based on specific conditions at the user, computer and domain
  level. :term:`Registry` changes are extremely specific and apply to the user
  or computer. Recent updates with Windows have been pushing more and more GPO
  policies to only work in ``Education`` and ``Enterprise`` versions.

  :term:`Registry` settings are only used when there are no specific GPO
  polices that can be applied. Only settings that have been changed or are
  deemed important are listed. Apply based on your personal preferences.
  Registry settings may be found in reference material if provided.

  A reboot is required once these changes are made.

.. note::
  Any unlisted section/change assumes default settingss.

Install
*******
Rough install instructions from USB.

#. Name your device: Computer can no longer be the **same** as first user name.
#. Setup for personal use.
#. Let's connect you to a network

   If the offline option is not present in creating a user account, kill the
   networking manager to disable netowrk connections during setup:

   :cmdmenu:`shift + F10`

   .. code-block:: powershell
     :caption: Disable network connections temporarily.

     taskkill /F /IM oobenetworkconnectionflow.exe

   `Reference <https://hothardware.com/news/windows-11-setup-internet-connection-bypass>`__

#. :cmdmenu:`Lets add your microsoft account --> Sign in options --> Offline account --> skip for now (microsoft account)`

   There is no way to manage security questions in Windows 11. Recommend
   installing with no password then setting a password which skips security
   questions.

#. Privacy for device: all {OFF}

.. gpo::    Disable local account security questions
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Credential User Interface -->
            Prevent the use of security questions for local accounts
  :value0:  ☑, {DISABLED}
  :ref:     https://www.tenforums.com/tutorials/117755-enable-disable-security-questions-local-accounts-windows-10-a.html
            https://www.cyclonis.com/windows-10-security-questions-not-secure/
  :update:  2022-01-20
  :generic:
  :open:
