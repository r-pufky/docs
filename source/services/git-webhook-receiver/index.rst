.. _service-git-webhook-receiver:

Git Webhook Receiver
####################
Automatically update a local git repository when changes are pushed to origin.

This is useful for addressing gitfs issues with saltstack, as well as always
having an up-to-date local copy of head. As this makes a system call, anything
can really be done.

.. gport:: Ports (Git Webhook Receiver)
  :port:     8666
  :protocol: TCP
  :type:     Exposed
  :purpose:  Listen port for webhook.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (Git Webhook Receiver)
  :file:    /etc/systemd/system/git-webhook-receiver.service,
            /srv/sync
  :purpose: systemd service.,
            Base sync location.
  :no_key_title:
  :no_caption:
  :no_launch:

Setup Upstream Git Webhook
**************************
Assumes **gitea** but any git service with webhooks should work. Ensure that you
adjust settings in ``git-webhook-receiver.py`` if needed.

Create User for Pulling Repository
==================================
.. ggui:: Add Webhook User.
  :key_title: Site Administration -->
              User Accounts -->
              Create User Account
  :option:    Authentication Source,
              Username,
              Email Address,
              Password,
              ☐
  :setting:   local,
              {WEBHOOK USER},
              {WEBHOOK EMAIL},
              {PASSWORD},
              Require user to change password
  :no_section:
  :no_launch:

.. ggui:: Edit New User.
  :option:  ☐
  :setting: may create organizations
  :no_key_title:
  :no_section:
  :no_launch:

.. ggui:: Setup webhook for Each Desired Repository.
  :key_title: Project -->
              Settings -->
              Collaborators -->
              Add Collaborators
  :option:    {USER}
  :setting:   Read-Only
  :no_section:
  :no_launch:

.. ggui:: Add webhook.
  :key_title: Project -->
              Settings -->
              Collaborators -->
              Webhooks
  :option:    Target URL,
              Post,
              Secret,
              ☑,
              ☑
  :setting:   http://{MACHINE RUNNING RECEIVER}:8666,
              application/json,
              {AUTH TOKEN FOR WEBHOOK},
              Push Events,
              Active
  :no_section:
  :no_launch:

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
  This will prompt for {USER} and {PASSWORD}; they will be stored locally in
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
.. _credentials: https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git