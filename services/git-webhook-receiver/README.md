Git Webhook Receiver
====================
Automatically update a local git repository when changes are pushed to origin.

This is useful for addressing gitfs issues with saltstack, as well as always
having an up-to-date local copy of head. As this makes a system call, anything
can really be done.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Starting the Server](#starting-the-server)

Ports Exposed
-------------
Service

| Port | Protocol | Purpose                  |
|------|----------|--------------------------|
| 8666 | TCP      | Listen port for webhook. |

Important File Locations
------------------------

| File                                             | Purpose             |
|--------------------------------------------------|---------------------|
| /etc/systemd/system/git-webhook-receiver.service | systemd service.    |
| /srv/sync                                        | Base sync location. |

Server Setup
-------------
### Setup Upstream Git Webhook
Assumes _gitea_ but any git service with webhooks should work. Ensure that you
adjust settings in `git-webhook-receiver.py` if needed.

#### Create User for Pulling Repository
`Site Administration > User Accounts > Create User Account`
* Authentication Source: `local`
* Username: {USER}
* Email Address: {EMAIL}
* Password: {PW}
- [ ] Require user to change password.

Edit the new user:
- [ ] may create organizations

#### Setup webhook for Each Desired Repository
`project > Settings > Collaborators > Add Collaborators`
* {USER}
* Read-Only

`project > Settings > Collaborators > Webhooks`
* target url: http://{MACHINE RUNNING RECEIVER}:8666
* post: `application/json`
* secret: {AUTH TOKEN FOR WEBHOOK}
- [x] Push Events
- [x] Active

### Clone webhook Receiver and Setup Service
```bash
cd /srv/sync
git clone https://github.com/r-pufky/git-webhook-receiver
cp git-webhook-receiver/examples/git-webhook-receiver.service /etc/systemd/service
cp git-webhook-receiver/git-webhook-receiver.py /srv/sync/git-webhook-receiver.py
cp git-webhook-receiver/config.yaml /srv/sync/
```
* Update the service with appropriate restricted user.

#### Add configuration for each repository with a webhook.
/srv/sync/config.yaml `{USER}:{USER} 0600`
```yaml
http://{GIT SERVER}:{PORT}/{USER}/{REPO}:
  command: /srv/sync/repo-sync
  secret: {AUTH TOKEN FOR WEBHOOK}
  background: True
```
* Note: If running git service from a docker container, the URI will most likely
  be _localhost_ instead of DNS name.

#### Setup Saved git Credentials
Save the [user][eb] [credentials][8c] locally remote repository can be sync'ed
automatically.

For each respository to sync:
* Ensure logged in as sync user.
* clone repository to desired location.
* Setup saved credentials:

```bash
cd {CLONED REPO}
git config credential.helper store
git pull
```
* This will prompt for {USER} and {PW}; they will be stored locally in
  `~/.git-credentials`.

#### Setup pull Scripts
These scripts can really do anything. In this case, we are going to pull head to
the local repository.

/srv/sync/repo-sync `{USER}:{USER} 0600`
```bash
#!/bin/bash
cd /srv/{REPO}
git pull
```

Starting the Server
-------------------
```bash
systemctl enable git-webhook-receiver.service
systemctl start git-webhook-receiver
```

### Testing
Create a CL and push it to origin. Check the local repository to see update.

[sf]: https://github.com/r-pufky/git-webhook-receiver
[eb]: https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
[8c]: https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git
