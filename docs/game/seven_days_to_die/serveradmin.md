# [serveradmin.xml][a]
Specifying admins and restrictions requires user ID lookups on platforms that
users are on. Recommendation is to modify only through [console commands][d].

## Users

### User ID
SteamID64 is **required** (e.g. 76561198021925107) for user ID. Steam ID may be
retrieved from any of the following:

* https://steamdb.info/calculator/
* https://steamid.io/lookup
* http://steamid.co/

Input the player's name in the search field or steam page URL.

``` bash
# Easier to look in server logs to obtain user ID's for non-steam users.
tail -F /home/steam/seven_days_to_die/output_log__*.txt

grep -i {PLAYER} ~/.local/share/7DaysToDie/Saves/.../players.xml
```

Or via the [built-in web console][b].

!!! abstract "http://{IP}:8080 ➔ Login ➔ console"

### Permission levels
A user may run any command equal to or above their permission level. Users not
given a permission level in this file will have a default permission level of
**1000** (no privileges).

**0** effectively grants the specified user root access.

## Options

### users

``` xml
<users>
<user platform="Steam" userid="76561198021925107" name="Name" permission_level="0" />
<group steamID="103582791434672565" name="All steam users (Steam Universe)" permission_level_default="1000" permission_level_mod="0" />
</users>
```

### whitelist
Enabling whitelisting will disable blacklisting. Nobody can join that ISN'T in
the whitelist or admins once whitelist only mode is enabled.

Name is optional for display purposes only.

``` xml
<whitelist>
<user platform="" userid="" name="" />
<group steamID="" name="" />
</whitelist>
```

### blacklist
Name is optional for display purposes only.

``` xml
<blacklist>
<blacklisted platform="" userid="" name="" unbandate="" reason="" />
</blacklist>
```

### commands
Commands use [permissions levels](#permission-levels).

* Commands are granted access by all levels *above* the assigned permission.
* Commands not specified have default permission level **0** (root access).

``` xml
<!-- default permissions for all commands -->
<commands>
<permission cmd="dm" permission_level="0" />
<permission cmd="kick" permission_level="1" />
<permission cmd="say" permission_level="1000" />
<permission cmd="chunkcache" permission_level="1000" />
<permission cmd="createwebuser" permission_level="1000" />
<permission cmd="cvar" permission_level="1000" />
<permission cmd="debugshot" permission_level="1000" />
<permission cmd="debugweather" permission_level="1000" />
<permission cmd="decomgr" permission_level="1000" />
<permission cmd="getgamepref" permission_level="1000" />
<permission cmd="getgamestat" permission_level="1000" />
<permission cmd="getlogpath" permission_level="1000" />
<permission cmd="getoptions" permission_level="1000" />
<permission cmd="gettime" permission_level="1000" />
<permission cmd="gfx" permission_level="1000" />
<permission cmd="graph" permission_level="1000" />
<permission cmd="help" permission_level="1000" />
<permission cmd="listplayerids" permission_level="1000" />
<permission cmd="listthreads" permission_level="1000" />
<permission cmd="loot" permission_level="1000" />
<permission cmd="memcl" permission_level="1000" />
<permission cmd="meshdatamanager" permission_level="1000" />
<permission cmd="settempunit" permission_level="1000" />
<permission cmd="uioptions" permission_level="1000" />
</commands>
```

### apitokens
Authenticate user for elevated access.

``` xml
<apitokens>
<token name="adminuser1" secret="supersecrettoken" permission_level="0" />
</apitokens>
```


## Reference[^1]
[^1]: https://developer.valvesoftware.com/wiki/7_Days_to_Die_Dedicated_Server

[a]: https://7daystodie.fandom.com/wiki/Server:_serveradmin.xml
[b]: https://shockbyte.com/help/knowledgebase/articles/how-to-find-a-player-s-eos-id-in-7-days-to-die
[c]: https://www.gameserverkings.com/knowledge-base/7-days-to-die/7d2d-new-user-guide/
[d]: https://7daystodie.fandom.com/wiki/Command_Console
