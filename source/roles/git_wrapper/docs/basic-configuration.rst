.. _service-gitea-basic-configuration:

Basic Configuration
###################
Initial Gitea setup with restricted permissions for configuration.

Navigate to: ``{REVERSE PROXY URI}/install``.

.. gui::   Database Settings
  :path:   Database Settings
  :value0: Database, postgres
  :value1: Host, {IP}:5432
  :value2: Database Name, gitea
  :value3: Username, {USER}
  :value4: Password, {PASS}
  :value5: SSL, {DISABLE}

  Use specific postgres settings according to your installation.

.. gui::   General Settings
  :path:   General Settings
  :value0: Site Title, {SITE}
  :value1: Repository Root Path, /data/git/repositories
  :value2: Git LFS Root Path, /data/git/lfs
  :value3: Run As Username, git
  :value4: SSH Server Domain, {LOCALHOST}
  :value5: SSH Server Port, 22
  :value6: Gitea HTTP Listen Port, 3000
  :value7: Gitea Base URL, https://{YOUR SUBDOMMAIN OR DOMAIN/PATH}/
  :value8: Log Path, /data/gitea/log

  .. warning::
    If the base URL in web admin configuration page is not set to your domain,
    it will appear that everything is working, however intersite links will fail
    (such as issue updates). This can be changed by editing ``gitea_root_url``
    file post initial configuration.

.. gui::    Optional Settings
  :path:    Optional Settings
  :value0:  ☑, Enable Local Mode
  :value1:  ☑, Disable Gravatar
  :value2:  ☐, Enable Federated Avatars
  :value3:  ☐, Enable OpenID Sign-In
  :value4:  ☑, Disable Self-Registration
  :value5:  ☐, Allow Registration Only Through External Services
  :value6:  ☐, Enable OpenID Self-Registration
  :value7:  ☑, Enable CAPTCHA
  :value8:  ☑, Require Sign-In to View Pages
  :value9:  ☐, Hide Email Addresses by Default
  :value10: ☑, Allow Creation of Organizations by Default
  :value11: ☑, Enable Time Tracking by Default
  :value12: Hidden Email Domain, users.noreply.{DOMAIN}
  :value13: Administrator Account Settings,
  :value14: › Administration Username, {USER}
  :value15: › Password, {PASS}
  :value16: › Confirm Password, {PASS}
  :value17: › Email Address, {EMAIL}
