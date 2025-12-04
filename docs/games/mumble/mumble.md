# [Mumble][a]
High quality VOIP server with public certificate authentication, encryption,
and ACLs.

## Ports
64738: UDP - Encrypted Voice Data.

64738: UDP - Encrypted Control Data.

/var/lib/mumble-server/mumble-server.sqlite, Server user/channel data.

/etc/mumble-server.ini, Server configuration.

## Setup
!!! warning
    Registration password cannot be changed.

``` bash
apt install mumble-server
```

!!! abstract "/etc/mumble-server.ini"
    0600 mumble-server:mumble-server

    ``` bash
    # Database contains all save user information.
    database=/var/lib/mumble-server/mumble-server.sqlite
    dbus=system
    ice="tcp -h 127.0.0.1 -p 6502"
    icesecretwrite=
    autobanAttempts = 10
    autobanTimeframe = 30
    logfile=/dev/null
    pidfile=/var/run/mumble-server/mumble-server.pid

    # Welcome message sent to clients when they connect.
    welcometext="<br /><br />
    WELCOME TEXT<br /><br />
    MORE WELCOME TEXT<br /><br />
    <br />"

    # Server accepts connections on TCP/UDP.
    port=64738
    serverpassword=
    bandwidth=1000000
    users=100
    # Appears in public channel listing.
    registerName={PUBLIC SERVER NAME TO REGISTER}
    registerPassword={REGISTER PASSWORD}
    # Reference URL for server.
    registerUrl={SERVER OR REFERENCE URL}
    bonjour=False
    uname=mumble-server
    certrequired=True
    rememberchannel=True
    suggestPushToTalk=True
    defaultchannel=8
    [Ice]
    Ice.Warn.UnknownProperties=1
    Ice.MessageSizeMax=65536
    ```

Re-configure package and set **superuser** mumble password.
``` bash
dpkg-reconfigure mumble-server
systemctl start mumble-server
```


## Administration

### Adding New Member
1. {USER} ➔ RMB ➔ Register
2. User should now appear with a +: ![Icon](icon.png)
3. {ROOT CHANNEL} ➔ RMB ➔ Edit:

    ![Edit Root Channel](edit_root_channel.png)

4. Select
    * **1** Groups.
    * **2** Select group from the pulldown.
    * **3** Type in user name (should auto populate).
    * **4** Add.
    * **5** OK.

    ![Add Member](add_member.png)

5. User should now be able to move into all properly created channels.

### Create New Channel
1. {ROOT CHANNEL} ➔ RMB ➔ Add

    ![Create Channel](create_channel.png)

2. Type channel name, leave everything else alone:

    ![Name Channel](name_channel.png)

3. All permissions are inherited from the root channel, so as long as the user
   is added to the group, they have access to all channels created in that
   channel.

### Reset superuser password
``` bash
dpkg-reconfigure mumble-server
```


## References[^1][^2][^3]

[^1]: https://wiki.mumble.info/wiki/Running_Murmur#Setting_the_SuperUser_Password
[^2]: https://www.typefrag.com/mumble/tutorials/advanced-user-settings/
[^3]: https://www.mumble.com/support/mumble-how-to-create-a-channel.php

[a]: https://wiki.mumble.info/wiki/Main_Page
