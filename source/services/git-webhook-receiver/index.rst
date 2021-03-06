.. _service-git-webhook-receiver:

Git Webhook Receiver
####################
Automatically update a local git repository when changes are pushed to origin.

This is useful for addressing gitfs issues with saltstack, as well as always
having an up-to-date local copy of head. As this makes a system call, anything
can really be done.

Ports
*****
.. ports:: Git Webhook Receiver Ports
  :value0: 8666, {TCP}, {EXPOSED}, Listen port for webhook
  :open:

Ports
*****
.. files:: Git Webhook Receiver Files
  :value0: /etc/systemd/system/git-webhook-receiver.service, systemd service
  :value1: /srv/sync, Base sync location
  :open:

Setup Upstream Git Webhook
**************************
Assumes **gitea** but any git service with webhooks should work. Ensure that you
adjust settings in ``git-webhook-receiver.py`` if needed.

Create User for Pulling Repository
==================================
.. gui::   Add Webhook User
  :path:   Site Administration -->
           User Accounts -->
           Create User Account
  :value0: Authentication Source, {LOCAL}
  :value1: Username, {USER}
  :value2: Email Address, {EMAIL}
  :value3: Password, {PASS}
  :value4: ☐, Require user to change password
  :open:

.. gui::   Edit New User
  :path:   Site Administration -->
           User Accounts -->
           Edit
  :value0: ☐, may create organizations
  :open:

.. gui::   Setup webhook for Each Desired Repository
  :path:   Project -->
           Settings -->
           Collaborators -->
           Add Collaborators
  :value0: {USER}, Read-Only
  :open:

.. gui::   Add webhook
  :path:   Project -->
           Settings -->
           Collaborators -->
           Webhooks
  :value0: Target URL, http://{RECEIVER}:8666
  :value1: Post, application/json
  :value2: Secret, {TOKEN}
  :value3: ☑, Push Events
  :value4: ☑, {ACTIVE}
  :open:

Clone webhook Receiver and Setup Service
========================================
Using a simple `git webhook receiver`_.

.. code-block:: bash
  :caption: Clone webhook receiver.

  cd /srv/sync
  git clone https://github.com/r-pufky/git-webhook-receiver
  cp git-webhook-receiver/examples/git-webhook-receiver.service /etc/systemd/service
  cp git-webhook-receiver/git-webhook-receiver.py /srv/sync/git-webhook-receiver.py
  cp git-webhook-receiver/config.yaml /srv/sync/

.. note::
  Update the service with appropriate restricted user.

Add configuration for each repository with a webhook.

.. code-block:: yaml
  :caption: **0600 user user** ``/srv/sync/config.yaml``

  http://{GIT SERVER}:{PORT}/{USER}/{REPO}:
    command: /srv/sync/repo-sync
    secret: {AUTH TOKEN FOR WEBHOOK}
    background: True

.. note::
  If running git service from a docker container, the URI will most likely be
  ``localhost`` instead of DNS name.

Setup Saved git Credentials
===========================
Save the `user`_ `credentials`_ locally remote repository can be sync'ed
automatically.

For each respository:

#. Ensure logged in as sync user.
#. Clone repository to desired location.
#. Setup saved credentials:

   .. code-block:: bash

     cd {CLONED REPO}
     git config credential.helper store
     git pull

.. note::
  This will prompt for {USER} and {PASS}; they will be stored locally in
  ``~/.git-credentials``.

Setup pull Scripts
==================
These scripts can really do anything. In this case, we are going to pull head to
the local repository.

.. code-block:: bash
  :caption: **0700 user user** ``/srv/sync/repo-sync``

  #!/bin/bash
  cd /srv/{REPO}
  git pull

Starting the Server
*******************

.. code-block:: bash
  :caption: Enable webhook service and start.

  systemctl enable git-webhook-receiver.service
  systemctl start git-webhook-receiver

Testing
*******
Create a CL and push it to origin. Check the local repository to see update.

.. _git webhook receiver: https://github.com/r-pufky/git-webhook-receiver
.. _user: https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
.. _credentials: https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git-gitextension
