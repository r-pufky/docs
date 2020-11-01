.. _apps-sublime-text:

Sublime Text Configuration
##########################

Installation
************
Download `latest binary`_ for any platform here.

Ubuntu Apt Repository
=====================

.. code-block:: bash
  :caption: Add the sublime repository and install.

  wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
  apt install apt-transport-https
  echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
  apt update
  apt install libgtk2.0-0 sublime-text

Important File Locations
************************
Configuration files can be modified directly in sublime via
:cmdmenu:`preferences --> settings`.

Generally, you should never have to modify file directly; you can copy and paste
directly with the menu settings.

.. gflocation:: Windows
  :file:    %appdata%\Sublime Text 3,
            %appdata%\Sublime Text 3\Packages\User\Preferences.sublime-settings,
            %appdata%\Sublime Text 3\Packages\User\Package Control.sublime-settings,
            %appdata%\Sublime Text 3\Installed Packages\Package Control.sublime-package
  :purpose: Configuration and package locations.,
            User preferences.,
            User installed packages.,
            Package control.
  :no_key_title:
  :no_section:
  :no_launch:

.. gflocation:: Linux
  :file:    ~/.config/sublime-text-3,
            ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings,
            ~/.config/sublime-text-3/Packages/User/Package Control.sublime-settings,
            ~/.config/sublime-text-3/Installed Packages/Package Control.sublime-package
  :purpose: Configuration and package locations.,
            User preferences.,
            User installed packages.,
            Package control.
  :no_key_title:
  :no_section:
  :no_launch:

.. gflocation:: OSX
  :file:    ~/Library/Application Support/Sublime Text 3,
            ~/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings,
            ~/Library/Application Support/Sublime Text 3/Packages/User/Package Control.sublime-settings,
            ~/Library/Application Support/Sublime Text 3/Installed Packages/Package Control.sublime-package
  :purpose: Configuration and package locations.,
            User preferences.,
            User installed packages.,
            Package control.
  :no_key_title:
  :no_section:
  :no_launch:

Configuration
*************
.. literalinclude:: source/Preferences.sublime-settings
  :caption: Copy and paste into user preferences
            :cmdmenu:`preferences --> settings`.
  :linenos:

:download:`Download settings here <source/Preferences.sublime-settings>`.

.. note::
  Preferences can also be set by replacing the file directly:
  ``cp Preferences.sublime-settings <sublime config>/Packages/User``

`Automatically Installing Packages`_
************************************
Sublime will automatically keep packages up to date if they are listed as
Installed. You can use this to automatically installed Package Control, as well
as packages on a fresh installation. Some `recommended packages`_ are here.

.. code-block:: bash
  :caption: Download the package control binary and add installed packages.

  wget https://packagecontrol.io/Package%20Control.sublime-package <sublime config>/Installed\ Packages/
  cp Package\ Control.sublime-settings <sublime config>/Packages/User

:download:`Download package control settings file <source/Package
Control.sublime-settings>`.

Upon startup of sublime, it will automatically install the missing packages now
listed in your installed packages.

`Force Unix Line Endings on Save`_
**********************************
This will save all files with unix lines endings regardless of platform or
setting.

.. literalinclude::**0600 user user** ``source/set_unix_line_endings.py``
  :linenos:

:download:`Downfile file here <source/set_unix_line_endings.py>`

Copy file to ``<sublime config>/Packages/User``. Remove to disable.

Markdown Editing
****************
Install ``MarkdownEditing`` and ``MonokaiC`` packages.

:cmdmenu:`preferences --> package settings --> markdown editing --> markdown GFM Settings -- user --> Markdown.sublime-settings`

.. literalinclude:: source/Markdown.sublime-settings
  :caption: **0600 user user** ``<sublime config>/Preferences/User/Markdown.sublime-settings``
  :linenos:

.. rubric:: References

#. `Settings Files <https://www.sublimetext.com/docs/3/settings.html>`_
#. `Customizing Settings Files <https://sublime-text.readthedocs.io/en/stable/customization/settings.html>`_
#. `Package Control Binary <https://packagecontrol.io/Package%20Control.sublime-package>`_
#. `Using Sublime text from the command line <https://medium.com/@pck/how-to-use-sublime-text-3-from-command-line-with-ubuntu-bash-terminal-in-windows-10-subsystems-for-aa2ad59d088c>`_

.. _latest binary: https://www.sublimetext.com/3
.. _custom user preferences: Preferences.sublime-settings
.. _Automatically Installing Packages: https://github.com/mrmartineau/SublimeTextSetupWiki/issues/3
.. _recommended packages: https://txfx.net/2014/11/08/my-sublime-text-3-packages/
.. _Force Unix Line Endings on Save: https://stackoverflow.com/questions/39680585/how-do-configure-sublime-to-always-convert-to-unix-line-endings-on-save
