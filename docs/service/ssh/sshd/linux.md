# Linux

## Require Certificate and disable root logins
This will provide a default configuration which only allows non-root public key
authenticated users to login.

``` bash
AllowAgentForwarding no
AllowGroups _ssh
AuthorizedKeysFile %h/.ssh/authorized_keys
ChallengeResponseAuthentication no
HostbasedAuthentication no
PasswordAuthentication no
PermitEmptyPasswords no
PermitRootLogin no
PubkeyAuthentication yes
RSAAuthentication no
RhostsRSAAuthentication no
StreamLocalBindUnlink yes
UsePrivilegeSeparation yes
```

## Add Users to Access Group
``` bash
addgroup {USER} _ssh
systemctl restart ssh
```

Reference:

* https://www.cyberciti.biz/tips/openssh-deny-or-restrict-access-to-users-and-groups.html

## Allow SSH Connections Through UFW
UFW may be configured by default to block connections, verify this is not the
case. The general default is to deny incoming connections, allow outgoing, and
enable SSH.

``` bash
ufw status

# Deny incoming connections except SSH, allow outgoing.
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
```

Reference:

* https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04

## Create a Port Forwarding Only User
Useful to forward services without providing shell a login.

``` bash
adduser --disabled-password --home /etc/ssh/port-forwards-only --shell /bin/false port-forwards-only
addgroup port-forwards-only ssh
mkdir /etc/ssh/port-forwards-only
chmod 0700 /etc/ssh/port-forwards-only
chown port-forwards-only:port-forwards-only /etc/ssh/port-forwards-only
ssh-keygen -b 4096 -t rsa -f /etc/ssh/port-forwards-only/port-forwards-only
cat /etc/ssh/port-forwards-only/port-forwards-only.pub >> /etc/ssh/port-forwards-only/authorized_keys
```

### Verify Restrictions
Attempt to login with a shell as well as port forwarding working.

``` bash
# Only port forwarding should work (-N). Interactive logins with and without
# cert should fail.
ssh -vvv -N -L 5901:{SERVER}:5900 -i ~/.ssh/port-forwards-only port-forwards-only@{SERVER}
ssh -vvv -i ~/.ssh/port-forwarding-only port-forwards-only@{SERVER}
ssh -vvv -i port-forwards-only@{SERVER}
```
