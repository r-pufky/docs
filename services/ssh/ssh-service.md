SSH Server
----------

1. [Centralize Authorized Key Files](#centralize-authorized-key-files)
1. [Create a Port Forwarding Only User](#create-a-port-forwarding-only-user)

Centralize Authorized Key Files
-------------------------------
Redirect all key files to a specific directory and link to users; allowing for
easier central management of keys.

See [example configuration](#sshd_config)

Only allow users in SSH group to access
`AllowGroups ssh`

Use authorized_keys file in /etc/ssh/<user> for authenticating <user>
`AuthorizedKeysFile /etc/ssh/%u/authorized_keys`

Ensure to add users to `ssh` group
```bash
addgroup <user> ssh
```

Create a Port Forwarding Only User
----------------------------------
Useful to forward services without providing a login.

```bash
adduser --disabled-password --home /etc/ssh/port-forwards-only --shell /bin/false port-forwards-only
addgroup port-forwards-only ssh
mkdir /etc/ssh/port-forwards-only
chmod 0700 /etc/ssh/port-forwards-only
chown port-forwards-only:port-forwards-only /etc/ssh/port-forwards-only
ssh-keygen -b 4096 -t rsa -f /etc/ssh/port-forwards-only/port-forwards-only
cat /etc/ssh/port-forwards-only/port-forwards-only.pub >> /etc/ssh/port-forwards-only/authorized_keys
```

See [Restrict SSH Tunneling](README.md#restricting-ssh-tunneling); add only
`permitopen` lines.

### Verify restrictions
Attempt to login with a shell as well as port forwarding working.

```bash
ssh -vvv -N -L 5901:10.2.2.20:5900 -i ~/.ssh/port-forwards-only port-forwards-only@<SERVER>
ssh -vvv -i ~/.ssh/port-forwarding-only port-forwards-only@<SERVER>
ssh -vvv -i port-forwards-only@<SERVER>
```
 * only port forwarding should work (-N)
 * interactive logins with and without cert should fail

References
----------
[Basic SSH Public Key Authentication Setup][1]

[Deny/Allow/Restrict SSH access to users and groups][2]

[1]: https://help.ubuntu.com/community/SSH/OpenSSH/Keys
[2]: http://www.cyberciti.biz/tips/openssh-deny-or-restrict-access-to-users-and-groups.html