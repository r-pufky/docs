Tomahawk Configuration

1. [Installation](#installation)
1. [Important File Locations](#important-file-locations)
1. [Configuration](#configuration)

Installation
------------
* Any Platform Manual Download [latest binary here][1]

Important File Locations
------------------------
Windows

| File                     | Purpose                       |
|--------------------------|-------------------------------|
| %appdata%\Local\Tomahawk | Local configuration and cache |

Configuration
-------------
To setup [tomahawk to use beets][2], you must enable the beets resolver.

If the resolvers are not automatically installed, try auto-updating

```
help > check for updates
```

```
settings > configure tomahawk > plug-ins
```
 * If not present, click `Install Plug-in`, and manually install the AXE
   file [from the repository here][3]
 * Set `server` to beets server, port 8337


[1]: https://www.tomahawk-player.org/#page-about
[2]: http://beets.io/blog/tomahawk-resolver.html
[3]: https://github.com/tomahawk-player/tomahawk-resolvers
