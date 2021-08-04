.. _service-firefly-lxc:

Firefly LXC/KVM/Baremetal Install
#################################
Self-hosted financial manager.

+-------------+-------------+
| Requirement | Recommended |
+=============+=============+
| Memory      | 512MB       |
+-------------+-------------+

Ports
*****
.. ports:: Firefly Ports
  :value0:   80, {TCP},  {PUBLIC}, Firefly web UI
  :value1:  443, {TCP}, {PRIVATE}, Firefly web UI (https)
  :open:

Files
*****
.. files:: Firefly Files
  :value0: /var/www/firefly-iii/storage/export, Exported data location
  :value1: /var/www/firefly-iii/storage/upload, Uploaded docs location
  :open:

Install
*******
Assumes :ref:`ubuntu` installed with a local user account, with backup data
mounted on ``/data/storage``.

Dependencies
============
.. code-block:: bash
  :caption: Install firefly denpendencies

  apt install nginx curl php7.4 php7.4-cli php7.4-zip php7.4-gd php7.4-fpm php7.4-json php7.4-common php7.4-pgsql php7.4-zip php7.4-mbstring php7.4-curl php7.4-xml php7.4-bcmath php7.4-imap php7.4-ldap php7.4-intl 

Set 512MB php limit.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/php/7.4/fpm/php.ini``

  memory_limit = 512MB

.. code-block:: bash
  :caption: Install php composer for php dependency management.

  wget https://getcomposer.org/installer
  chmod +x installer
  ./installer -- --install-dir=/usr/local/bin --filename=composer

.. code-block:: bash
  :caption: Remove default NGINX files.

  rm /var/www/html/index.nginx-debian.html
  rm /etc/nginx/sites-enabled/default

.. _service-firefly-lxc-install-versioned:

Install Versioned
=================
Installing to a versioned directory enables easy migration to new versions.

https://api.github.com/repos/firefly-iii/firefly-iii/releases/latest

.. code-block:: bash
  :caption: Install latest version.

  cd /var/www/html/
  tar xvf firefly-iii.tar.gz

.. note::
   Latest version: https://api.github.com/repos/firefly-iii/firefly-iii/releases/latest

   This should extract to firefly-iii-{VERSION}

.. code-block:: bash
  :caption: Install php dependencies, set ownership, and link to latest version.

  composer create-project grumpydictator/firefly-iii --no-dev --prefer-dist firefly-iii --no-interaction {VERSION}
  sudo chown -R www-data:www-data firefly-iii
  sudo chmod -R 775 firefly-iii/storage
  ln -sf /var/www/html/firefly-iii-{VERSION} /var/www/html/firefly-iii

.. code-block:: bash
  :caption: Link to storage.

  rm /var/www/html/firefly-iii-{VERSION}/storage/{export,upload}
  ln -sf /var/www/html/firefly-iii-{VERSION}/storage/export /var/www/html/firefly-iii/storage/export
  ln -sf /var/www/html/firefly-iii-{VERSION}/storage/upload /var/www/html/firefly-iii/storage/upload
  chown -R www-data:www-data /var/www/html/firefly-iii-{VERSION}/storage/{export,upload}
  chmod -R 0775 /var/www/html/firefly-iii-{VERSION}/storage

Set logrotation.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/logrotate.d/firefly-iii``

  /opt/firefly-iii/storage/logs/*.log
  {
    weekly
    missingok
    rotate 2
    compress
    notifempty
    sharedscripts
    maxage 60
  }

Set the NGINX configuration to server firefly.

.. literalinclude:: source/firefly.conf
  :caption: **0640 root root** ``/etc/nginx/sites-enabled/firefly.conf``

.. code-block:: bash
  :caption: **0640 www-data www-data** ``/var/www/html/firefly-iii/.env``

  APP_KEY={KEY}

  TRUSTED_PROXIES=**

  DB_CONNECTION=pgsql
  DB_HOST=192.168.1.10
  DB_PORT=5432
  DB_DATABASE=firefly
  DB_USERNAME=firefly
  DB_PASSWORD={PASS}
  
  APP_URL=http://localhost

.. note::
  ``APP_KEY`` is alphanumeric string of 32 characters. Use
  ``php artisan key:generate`` to create it.

  Set ``TRUSTED_PROXIES=**`` to enable proxy usage.

  ``APP_URL`` this should remain localhost it does not effect proxied or
  non-proxied connections. Existing documentation on the web is wrong.

Proceed to :ref:`service-firefly-lxc-databse-config`.

.. _service-firefly-lxc-databse-config:

Database Config
***************
Majority of cases should use the DB migration instead of initalization; only use
initalization if new DB or wiping existing DB contents are ok.

.. _service-firefly-lxc-migration:

.. code-block:: bash
  :caption: Migrate the database.
  
  rm -rf /var/www/html/firefly-iii-{VERSION}/bootstrap/cache/*
  php artisan cache:clear
  php artisan migrate --seed
  php artisan firefly-iii:upgrade-database
  php artisan passport:install
  php artisan cache:clear

.. code-block:: bash
  :caption: Initialize the database.

  php artisan migrate:refresh --seed
  php artisan firefly-iii:upgrade-database
  php artisan passport:install

.. code-block:: bash
  :caption: Restart NGINX/php.

  systemctl restart nginx php7.4-fpm

Updating Firefly
****************
Install new version using the :ref:`service-firefly-lxc-install-versioned` steps
and :ref:`service-firefly-lxc-migration`. Previous versions can be deleted.

`Reference <https://docs.firefly-iii.org/firefly-iii/installation/upgrade/>`_

`Reference <https://computingforgeeks.com/setup-firefly-personal-finance-manager-on-ubuntu/>`__

`Reference <https://docs.firefly-iii.org/firefly-iii/installation/self_hosted/>`__
