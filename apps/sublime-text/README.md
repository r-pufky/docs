Sublime Text Configuration

1. Installation
2. File Locations
2. Configuration

Installation
------------
* Any Platform Manual Download [latest binary here][1]

### Ubuntu Apt Repository

Add the sublime repository and key
```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt update
```

Install sublime-text
```bash
sudo apt install libgtk2.0-0 sublime-text
```

Important File Locations
------------------------
Configuration file can be modified directly in sublime via

```
preferences > settings
```

Generally, you should never have to modify file directly; you can copy and paste
directly with the menu settings.

Windows

| File                                                                        | Purpose                             |
|-----------------------------------------------------------------------------|-------------------------------------|
| %appdata%\Sublime Text 3                                                    | configuration and package locations |
| %appdata%\Sublime Text 3\Packages\User\Preferences.sublime-settings         | user preferences                    |
| %appdata%\Sublime Text 3\Packages\User\Package Control.sublime-settings     | user installed packages             |
| %appdata%\Sublime Text 3\Installed Packages\Package Control.sublime-package | package control                     |


Linux

| File                                                                        | Purpose                             |
|-----------------------------------------------------------------------------|-------------------------------------|
| ~/.config/sublime-text-3                                                    | configuration and package locations |
| ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings         | user preferences                    |
| ~/.config/sublime-text-3/Packages/User/Package Control.sublime-settings     | user installed packages             |
| ~/.config/sublime-text-3/Installed Packages/Package Control.sublime-package | package control binary              |

OSX

| File                                                                                            | Purpose                                                 |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| ~/Library/Application Support/Sublime Text 3                                                    | configuration and package locations |
| ~/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings         | user preferences                    |
| ~/Library/Application Support/Sublime Text 3/Packages/User/Package Control.sublime-settings     | user installed packages             |
| ~/Library/Application Support/Sublime Text 3/Installed Packages/Package Control.sublime-package | package control binary              |


Configuration
-------------
Copy and paste the custom config below into user preferences

[Custom user configuration][4]
```
preferences > settings
```

Or directly copy the preferences file
```bash
cp Preferences.sublime-settings <sublime config>/Packages/User
```

[Automatically Installing Packages][6]
--------------------------------------
Sublime will automatically keep packages up to date if they are listed as Installed. You can use this to automatically installed Package Control, as well as packages on a fresh installation. Some [recommended packages are here][7].

Directly download the package control binary
```bash
wget https://packagecontrol.io/Package%20Control.sublime-package <sublime config>/Installed\ Packages/
```

Add installed packages
```bash
cp Package\ Control.sublime-settings <sublime config>/Packages/User
```

Upon startup of sublime, it will automatically install the missing packages now listed in your installed packages.


References
----------
[Download Sublime Text 3][1]

[Settings Files][2]

[Customizing Settings Files][3]

[Package Control Binary][8]

[1]: https://www.sublimetext.com/3
[2]: https://www.sublimetext.com/docs/3/settings.html
[3]: http://docs.sublimetext.info/en/latest/customization/settings.html
[4]: Preferences.sublime-settings
[5]: Package%20Control.sublime-settings
[6]: https://github.com/mrmartineau/SublimeTextSetupWiki/issues/3
[7]: http://txfx.net/2014/11/08/my-sublime-text-3-packages/
[8]: https://packagecontrol.io/Package%20Control.sublime-package
[9]: https://medium.com/@pck/how-to-use-sublime-text-3-from-command-line-with-ubuntu-bash-terminal-in-windows-10-subsystems-for-aa2ad59d088c
