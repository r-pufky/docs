# Star Rupture

!!! example "Migrated to ansible collection"
    Use [r_pufky.games.star_rupture][a].

  Port | Protocol | Use
 ------|----------|-----
  7777 | UDP      | All player connections; must use Public IP (hairpin NAT for local connections).
  7777 | TCP      | Manage Server connections.

!!! danger "Do not expose 7777/TCP to the Internet."
    There are currently RCE's for exposed remote management. See
    [Vulnerability Announcement][b]. Exposing this port to the internal network
    will allow a local admin to use the 'Manage Server' functionality.

## Configuring Server
Static management is highly recommended as it allows for zero-touch use after
initial configuration.

### Static Management
Server is managed via static configuration files. This enable mitigation of
server vulnerabilities but requires manual file management.

!!! tip "Enables auto loading of most recent autosave on start"
    A script is deployed that is executed before the service starts using the
    session name in DSSettings.ini to automatically set the most recent
    autosave on start.

    This allows for no additional touch needed after a server or service
    restarts.

### Remote Server Management
Remotely manage the server via the game client. Due to the current
[Vulnerability][b] only local network admins should use this method.

!!! warning "Every server reboot requires this setup again"
    Using remote admin management, state is not kept between reboots.

!!! example "Start Game ➔ Manage Server ➔ local IP"
    Any IP in which port **7777/TCP** is accessible will work. Use the admin
    password.

A new game may be created or an old save can be loaded. Be sure to start the
game and quit.

!!! success "Always exit game client before attempting to connect"
    Always exit the game client before attempting to connect to the server via
    **Join Game**. The client will incorrectly report a
    [more than one IP](#more-than-one-server-at-this-ip-please-specify-port)
    error otherwise.

## Troubleshooting

### More than one server at this IP, [please specify port][a]
The **Manage Server** option was used before using **Join Game**. The client
sometimes detects both the admin and standard user connection.

!!! danger ""
    More than one server at this IP, please specify port

Setup the server with **Manage Server** and **restart** the client; join game
will now work correctly.

[a]: https://minestrator.com/en/blog/article/star-rupture-dedicated-server-mybox-setup-2026
[b]: https://wiki.starrupture-utilities.com/en/dedicated-server/Vulnerability-Announcement