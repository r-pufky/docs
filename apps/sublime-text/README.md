Sublime Text Configuration

1. Installation
2. File Locations
2. Configuration

Installation
------------
* Download [latest binary here][1]
* No special install instructions

Important File Locations
------------------------
Configuration file can be modified directly in sublime via

```
preferences > settings
```

Generally, you should never have to modify file directly; you can copy and paste
directly with the menu settings.

Windows
| File                                                                | Purpose                             |
|---------------------------------------------------------------------|-------------------------------------|
| %appdata%\Sublime Text 3                                            | configuration and package locations |
| %appdata%\Sublime Text 3\Packages\User\Preferences.sublime-settings | User preferences                    |

Linux
| File                                                                | Purpose                             |
|---------------------------------------------------------------------|-------------------------------------|
| ~/.config/sublime-text-3                                            | configuration and package locations |
| ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings | user preferences                    |

OSX
| File                                                                | Purpose                                                 |
|---------------------------------------------------------------------|---------------------------------------------------------|
| ~/Library/Application Support/Sublime Text 3                                            | configuration and package locations |
| ~/Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings | user preferences                    |


Configuration
-------------
Copy and paste the custom config below into user preferences

[Custom user configuration][4]
```
preferences > settings
```


References
----------
[Download Sublime Text 3][1]
[Settings Files][2]
[Customizing Settings Files][3]

[1]: https://www.sublimetext.com/3
[2]: https://www.sublimetext.com/docs/3/settings.html
[3]: http://docs.sublimetext.info/en/latest/customization/settings.html
[4]: Preferences.sublime-settings