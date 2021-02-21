.. _w10-pro-base:

Windows 10 Pro Base
###################
Standard Windows setup used for gaming. Removes known tracking & bloatware.

Working assumptions:

* Windows 10 pro (64 bit).
* Execution Policy: **Unrestricted** (see: :ref:`setting-execution-policy`).
* Assumes Admin Rights.

Use base setup instructions, then apply based on current Windows version.

Related Material:

* :ref:`w10-pro-install` for base installation.
* :ref:`w10-1903` for ``1903`` specific configuration.
* :ref:`w10-execution-policy` to run powershell commands.
* :ref:`w10-force-upgrade` to next major Windows version.
* :ref:`w10-reinstall-checklist` for common items to backup before reinstalling.
* :ref:`troubleshooting-pc-issues` for diagnosing problems.
* :ref:`w10-pro-advanced` Windows configuration.

See :ref:`w10-advanced-references` for advanced command references.

.. only:: comment

  Documentation updates

  #. Cut existing to new directory
  #. ``find . -type f -name "*.rst" -exec sed -i -e 's/w10-{OLD}/w10-{NEW}/g' {} \;``
  #. Prune and re-parse as needed to fit new windows release
  #. Check windows refs in docs and see if update (e.g. w10-1903, etc)

.. toctree::
   :hidden:
   :maxdepth: -1

   install-config
   execution-policy
   force-upgrade
   reinstall-checklist
   troubleshooting-pc-issues
   advanced/index
