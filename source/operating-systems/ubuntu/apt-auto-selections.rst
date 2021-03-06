.. _apt-auto-selection:

Apt Auto Selection
##################
Automatically select user-required options during package install.

This is used for configuration management and preseeding for automatic installs
that require user input. See :ref:`ubuntu-preseed-installation` and
:ref:`salt-saltstack`.

`Reference <https://serverfault.com/questions/407317/passing-default-answers-to-apt-get-package-install-questions>`__

Install with Options
********************
Determine the `debconf` options used by installing the package with the options
set.

.. code-block:: bash

  apt install debconf-utils
  apt install {PACKAGE}
  debconf-get-selections | grep {PACKAGE}

Set Options
***********
On target machines, set options before installing the package. This will remove
the prompts from apt.

.. code-block:: bash

  echo "{PACKAGE}-{VERSION} package/option {NAME} {VALUE}" | debconf-set-selections
  apt install {PACKAGE}

.. tip::
  debconf will list with tabs for easy reading. When setting selections separate
  with a **space**, otherwise the extra whitespace will be included with the
  option.

Example
*******
Complete example with MySql

.. code-block:: bash

  $ apt install mysql-server debconf-utils
  $ debconf-get-selections | grep mysql-server

  mysql-server-5.5        mysql-server/root_password_again        password
  mysql-server-5.5        mysql-server/root_password      password
  mysql-server-5.5        mysql-server/error_setting_password     error
  mysql-server-5.5        mysql-server-5.5/postrm_remove_databases        boolean false
  mysql-server-5.5        mysql-server-5.5/start_on_boot  boolean true
  mysql-server-5.5        mysql-server-5.5/nis_warning    note
  mysql-server-5.5        mysql-server-5.5/really_downgrade       boolean false
  mysql-server-5.5        mysql-server/password_mismatch  error
  mysql-server-5.5        mysql-server/no_upgrade_when_using_ndb  error

  $ echo "mysql-server-5.5        mysql-server-5.5/start_on_boot  boolean true"  | debconf-set-selections
  $ apt install mysql-server-5.5
