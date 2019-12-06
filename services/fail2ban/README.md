[fail2ban][3n]
==============
Automatically ban repeated failed authentication attempts across system and
docker services.

1. [Docker Capabilities](#docker-capabilities)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [System Setup](#system-setup)
1. [Docker Setup](#docker-setup)
1. [Bans Not Triggering](#bans-not-triggering)
1. [Common Commands](#common-commands)

Docker Capabilities
-------------------

| Capability | Action |
|------------|--------|
| NET_ADMIN  | ADD    |
| NET_RAW    | ADD    |

Important File Locations
------------------------
Relative to docker container.

| File           | Purpose                             |
|----------------|-------------------------------------|
| /data/jail.d   | Defines how services are watched.   |
| /data/filter.d | Defines actions on services.        |
| /var/log       | Mapped log location to watch.       |

Docker Creation
---------------
* Other containers may map their _logging_ directories to the system _/var/log_
  which will enable fail2ban to monitor docker container services.
* Containers should be separated from everything else. No need for external
  network access.
* Add capabilities are needed to modify iptable rules for the system and docker.

Docker Compose:
```yaml
f2b-docker:
  image: crazymax/fail2ban:latest
  restart: unless-stopped
  network_mode: host
  cap_add:
    - NET_ADMIN
    - NET_RAW
  environment:
    - F2B_LOG_LEVE=DEBUG
    - F2B_DB_PURGE_AGE=30d
    - F2B_MAX_RETRY=5
    - F2B_ACTION=%(action_)s
    - F2B_IPTABLES_CHAIN=DOCKER-USER
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/fail2ban/docker:/data
    - /etc/localtime:/etc/localtime:ro
    - /var/log:/var/log:ro
f2b-system:
  image: crazymax/fail2ban:latest
  restart: unless-stopped
  network_mode: host
  cap_add:
    - NET_ADMIN
    - NET_RAW
  environment:
    - F2B_LOG_LEVE=DEBUG
    - F2B_DB_PURGE_AGE=30d
    - F2B_MAX_RETRY=5
    - F2B_ACTION=%(action_)s
    - F2B_IPTABLES_CHAIN=INPUT
    - TZ=America/Los_Angeles
  volumes:
    - /data/services/fail2ban/system:/data
    - /etc/localtime:/etc/localtime:ro
    - /var/log:/var/log:ro
```

### Send nginx Logs to System
If using nginx as a proxy for dockers, setup to log to system.

Docker Compose:
```yaml
nginx:
  ...
  volumes:
    - /var/log/nginx:/var/log/nginx
```
* Restart nginx container. Logs should appear in _/var/log/nginx/*.log_ on host.
  Logs will no longer be accessible via `docker logs`.

System Setup
------------
Enable [fail2ban for sshd][d8] system service.

fail2ban/system/jail.d/sshd.conf: `root:root 0644`
```conf
[sshd]
enabled = true
port = ssh
filter = sshd[mode=aggressive]
logpath = /var/log/auth.log
bantime = -1
findtime = 86400
maxretry = 5
```
* Restart _f2b-system_.
* Attempt an invalid ssh login and watch the docker logs to see if ssh is
  getting properly identified `docker logs f2b-system`.
* `bantime` of `-1` means forever.
* `findtime` of `86400` is one day.

Docker Setup
------------
Enable fail2ban for a docker based [reverse-proxy][8b].

### Enable nginx Jails
This will enable jails for proxy auth, bad bots, home directories, open proxy,
and open scripts.

fail2ban/docker/jail.d/nginx.conf `root:root 0644`
```conf
# enable filtering of nginx http auth.
[nginx-http-auth]
enabled  = true
filter   = nginx-http-auth
port     = http,https
logpath  = /var/log/nginx/error.log
bantime  = -1
findtime = 86400
maxretry = 3

# Invalid file / directory access attempts.
[nginx-no-file-directory]
enabled  = true
filter   = nginx-no-file-directory
port     = http,https
logpath  = /var/log/nginx/error.log
bantime  = -1
findtime = 86400
maxretry = 2

# Forbidden index access attempts.
[nginx-forbidden]
enabled  = true
filter   = nginx-forbidden
port     = http,https
logpath  = /var/log/nginx/error.log
bantime  = -1
findtime = 86400
maxretry = 2

# Ban repeated client errors.
[nginx-errors]
enabled  = true
filter   = nginx-errors
port     = http,https
logpath  = /var/log/nginx/access.log
bantime  = -1
findtime = 86400
maxretry = 2

# Ban clients looking for scripts.
[nginx-noscript]
enabled  = true
filter   = nginx-noscript
port     = http,https
logpath  = /var/log/nginx/access.log
bantime  = -1
findtime = 86400
maxretry = 6

# Ban known malicious bad bots.
[nginx-badbots]
enabled  = true
filter   = nginx-badbots
port     = http,https
logpath  = /var/log/nginx/access.log
bantime  = -1
findtime = 86400
maxretry = 2

# Ban requests for user home directories.
[nginx-nohome]
enabled  = true
filter   = nginx-nohome
port     = http,https
logpath  = /var/log/nginx/access.log
bantime  = -1
findtime = 86400
maxretry = 2

# Ban attempts to use as an open proxy.
[nginx-noproxy]
enabled  = true
filter   = nginx-noproxy
port     = http,https
logpath  = /var/log/nginx/access.log
bantime  = -1
findtime = 86400
maxretry = 2
```

### Enable nginx Filters
This will allow fail2ban to take action on matches and ban IPs. Most of these
filters are [based off the default filters][2x], see [reverse-proxy notes][8b].

fail2ban/docker/filter.d/nginx-badbots.conf `root:root 0644`
```conf
# Fail2Ban configuration file
#
# Regexp to catch known spambots and software alike. Please verify
# that it is your intent to block IPs which were driven by
# above mentioned bots.

[Definition]

badbotscustom = EmailCollector|WebEMailExtrac|TrackBack/1\.02|sogou music spider|(?:Mozilla/\d+\.\d+ )?Jorgee
badbots = Atomic_Email_Hunter/4\.0|atSpider/1\.0|autoemailspider|bwh3_user_agent|China Local Browse 2\.6|ContactBot/0\.2|ContentSmartz|DataCha0s/2\.0|DBrowse 1\.4b|DBrowse 1\.4d|Demo Bot DOT 16b|Demo Bot Z 16b|DSurf15a 01|DSurf15a 71|DSurf15a 81|DSurf15a VA|EBrowse 1\.4b|Educate Search VxB|EmailSiphon|EmailSpider|EmailWolf 1\.00|ESurf15a 15|ExtractorPro|Franklin Locator 1\.8|FSurf15a 01|Full Web Bot 0416B|Full Web Bot 0516B|Full Web Bot 2816B|Guestbook Auto Submitter|Industry Program 1\.0\.x|ISC Systems iRc Search 2\.1|IUPUI Research Bot v 1\.9a|LARBIN-EXPERIMENTAL \(efp@gmx\.net\)|LetsCrawl\.com/1\.0 \+http\://letscrawl\.com/|Lincoln State Web Browser|LMQueueBot/0\.2|LWP\:\:Simple/5\.803|Mac Finder 1\.0\.xx|MFC Foundation Class Library 4\.0|Microsoft URL Control - 6\.00\.8xxx|Missauga Locate 1\.0\.0|Missigua Locator 1\.9|Missouri College Browse|Mizzu Labs 2\.2|Mo College 1\.9|MVAClient|Mozilla/2\.0 \(compatible; NEWT ActiveX; Win32\)|Mozilla/3\.0 \(compatible; Indy Library\)|Mozilla/3\.0 \(compatible; scan4mail \(advanced version\) http\://www\.peterspages\.net/?scan4mail\)|Mozilla/4\.0 \(compatible; Advanced Email Extractor v2\.xx\)|Mozilla/4\.0 \(compatible; Iplexx Spider/1\.0 http\://www\.iplexx\.at\)|Mozilla/4\.0 \(compatible; MSIE 5\.0; Windows NT; DigExt; DTS Agent|Mozilla/4\.0 efp@gmx\.net|Mozilla/5\.0 \(Version\: xxxx Type\:xx\)|NameOfAgent \(CMS Spider\)|NASA Search 1\.0|Nsauditor/1\.x|PBrowse 1\.4b|PEval 1\.4b|Poirot|Port Huron Labs|Production Bot 0116B|Production Bot 2016B|Production Bot DOT 3016B|Program Shareware 1\.0\.2|PSurf15a 11|PSurf15a 51|PSurf15a VA|psycheclone|RSurf15a 41|RSurf15a 51|RSurf15a 81|searchbot admin@google\.com|ShablastBot 1\.0|snap\.com beta crawler v0|Snapbot/1\.0|Snapbot/1\.0 \(Snap Shots&#44; \+http\://www\.snap\.com\)|sogou develop spider|Sogou Orion spider/3\.0\(\+http\://www\.sogou\.com/docs/help/webmasters\.htm#07\)|sogou spider|Sogou web spider/3\.0\(\+http\://www\.sogou\.com/docs/help/webmasters\.htm#07\)|sohu agent|SSurf15a 11 |TSurf15a 11|Under the Rainbow 2\.2|User-Agent\: Mozilla/4\.0 \(compatible; MSIE 6\.0; Windows NT 5\.1\)|VadixBot|WebVulnCrawl\.unknown/1\.0 libwww-perl/5\.803|Wells Search II|WEP Search 00

failregex = ^<HOST> -.*"(GET|POST|HEAD).*HTTP.*"(?:%(badbots)s|%(badbotscustom)s)"$

ignoreregex =

datepattern = ^[^\[]*\[({DATE})
              {^LN-BEG}

# DEV Notes:
# List of bad bots fetched from http://www.user-agents.org
# Generated on Thu Nov  7 14:23:35 PST 2013 by files/gen_badbots.
#
# Author: Yaroslav Halchenko
```
* This is a direct copy of the [apache-badbots filter][fp].

fail2ban/docker/filter.d/nginx-http-auth.conf `root:root 0644`
```conf
# fail2ban filter configuration for nginx
[Definition]

failregex = ^ \[error\] \d+#\d+: \*\d+ user "(?:[^"]+|.*?)":? (?:password mismatch|was not found in "[^\"]*"), client: <HOST>, server: \S*, request: "\S+ \S+ HTTP/\d+\.\d+", host: "\S+"(?:, referrer: "\S+")?\s*$
            ^ \[error\] \d+#\d+: \*\d+ no user/password was provided for basic authentication, client: <HOST>, server: \S+, request: "\S+ \S+ HTTP/\d+\.\d+", host: "\S+"\s*$

ignoreregex =

datepattern = {^LN-BEG}

# DEV NOTES:
# Based on samples in https://github.com/fail2ban/fail2ban/pull/43/files
# Extensive search of all nginx auth failures not done yet.
#
# Author: Daniel Black
```
* This is the basic [nginx-http-auth filter][db] with an additional line to
  handle basic auth with no username or password.

fail2ban/docker/filter.d/nginx-nohome.conf `root:root 0644`
```conf
[Definition]

failregex = ^<HOST> -.*GET .*/~.*

ignoreregex =
```
* Detect home directory usage.

fail2ban/docker/filter.d/nginx-noproxy.conf `root:root 0644`
```conf
[Definition]

failregex = ^<HOST> -.*GET http.*

ignoreregex =
```
* Detect use of server as a ad-hoc proxy.

fail2ban/docker/filter.d/nginx-noscript.conf `root:root 0644`
```conf
[Definition]

failregex = ^<HOST> -.*GET.*(\.php|\.asp|\.exe|\.pl|\.cgi|\.scgi)

ignoreregex =
```
* Detect attempts to directly access/execute scripts.

fail2ban/docker/filter.d/nginx-forbidden.conf `root:root 0644`
```conf
[Definition]

failregex = ^.*\[error\] \d+#\d+: .* is forbidden, client: <HOST>.*$

ignoreregex =
```
* Detect access to forbidden indexes.

fail2ban/docker/filter.d/nginx-no-file-directory.conf
```conf
[Definition]

failregex = ^.*\[error\] \d+#\d+: .* No such file or directory\), client: <HOST>.*$

ignoreregex =
```
* Detect attempts to access invalid files and directories.

fail2ban/docker/filter.d/nginx-errors.conf
```conf
# https://www.restapitutorial.com/httpstatuscodes.html
[Definition]

failregex = ^<HOST> -.*"(GET|POST|HEAD).*HTTP.*" (40[0-7,9]|4[1-8][0-9]) .*$

ignoreregex =
```
* Detect multiple client error codes.

Restart fail2ban.

Bans Not Triggering
-------------------
Commonly this is due to either invalid regex filters, timezone differences in
logs and fail2ban container, or database wonkiness.

Ensure regex filter is actually catching known bannable attempts:
```bash
fail2ban-regex /path/to/log.log /etc/fail2ban/filter.d/my-filter.conf
```
* If there are known lines that should be caught, these should appear in the
  output as _matched_.

Ensure regex filter is loaded properly:
```bash
fail2ban-client --dp
```
* This will show the loaded filters and jails. They should match your config.
* Restart the service to reload if different.

Set to debug and set if known bannable attempts are triggering:
```bash
docker-compose logs -f f2b-docker
```
* Bans should clearly appear in logs after logs are updated.

Reset fail2ban state:
```bash
fail2ban-client unban --all
docker-compose down
docker rmi crazymax/fail2ban:latest
rm /path/to/f2b/db/fail2ban.sqllite
docker-compuse up -d
```
* Sometimes the DB gets in a weird state where actions are not triggered. This
  will reset fail2ban to a default state (including the database) and actions
  should be triggered again.

Common Commands
---------------
### Show Overall Ban Status
```bash
docker exec -it f2b sh
fail2ban-client status
```

### Show Specific Jail Bans
```bash
docker exec -it f2b sh
fail2ban-client status {F2B JAIL NAME}
```

### Unban an IP
```bash
docker exec -it f2b sh
fail2ban-client set {F2B JAIL NAME} unbanip {IP}
```

### Show current config value
```bash
docker exec -it f2b sh
fail2ban-client get {F2B JAIL NAME} {CONFIG SETTING}
```

### Show iptables rules
```bash
iptables -S
```

[docker-service-template.md|14f2197][XX]

[3n]: https://hub.docker.com/r/crazymax/fail2ban
[d8]: https://github.com/crazy-max/docker-fail2ban/tree/master/examples/jails/sshd
[8b]: https://www.digitalocean.com/community/tutorials/how-to-protect-an-nginx-server-with-fail2ban-on-ubuntu-14-04
[2x]: https://github.com/fail2ban/fail2ban/blob/master/config/filter.d
[db]: https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/nginx-http-auth.conf
[fp]: https://github.com/fail2ban/fail2ban/blob/master/config/filter.d/apache-badbots.conf

[XX]: https://github.com/r-pufky/docs/blob/14f219752a17cf0017eccef6157c7957c16a9f78/services/docker-service-template.md