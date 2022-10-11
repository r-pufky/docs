.. _wbase:

Windows Base
############
Base Windows configuration that may be applied to all versions of windows.

Generally these are tweaks and fixes that should **not** be applied unless
specifically needed.

See :ref:`w10-latest` for the latest Windows 10 install instructions.

Related Material:

* :ref:`wbase-execution-policy` to run powershell commands.
* :ref:`wbase-force-upgrade` to next major Windows version.
* :ref:`wbase-reinstall-checklist` for common items to backup before reinstalling.
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
