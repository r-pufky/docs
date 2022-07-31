.. _manjaro-kde-apps:

Apps
####

.. code-block:: bash
  :caption: Install common Applications

  pacman -Syu signal-desktop git-lfs vim tmux meld discord playonlinux extra/bind

.. code-block:: bash
  :caption: Remove extra packages from standard install

  pacman -Rs firefox firefox-i18n-en-us gwenview manjaro-printer hplip k3b qbittorrent skanlite stoken thunderbird thunderbird-i18n-en-us yakuake openconnect networkmanager-openconnect

.. code-block:: bash
  :caption: Enable git LFS

  git lfs install

#. :ref:`manjaro-kde-apps-chrome`
#. :ref:`manjaro-kde-apps-vscodium`
#. :ref:`manjaro-kde-apps-steam`
#. :ref:`manjaro-kde-apps-sublime`
#. :ref:`manjaro-kde-apps-captive-portal`
#. :ref:`manjaro-kde-apps-nodejs`

.. toctree::
   :hidden:
   :maxdepth: -1

   vscodium
   chrome
   steam
   sublime
   captive-portal
   nodejs
