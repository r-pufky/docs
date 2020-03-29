Docs: A Collection of Setup Notes
#################################
I created this repository as a response to people requesting I share my setup
notes for services I run in my home. These notes have been made generic enough
so that you can implement these services and setups with relative ease. Be sure
to check the :ref:`glossary` if you see unknown symbols.

Where'd everything go?
**********************
Docs were re-organized to keep the growing documentation clean. You should link
to the core doc repo and browse files.

* :ref:`windows-10`
* :ref:`troubleshooting-pc-hardware`

Assumptions
***********
These notes make the following assumptions:

#. You have a advanced to expert competency in Windows, OSX, and Linux.
#. You are comfortable with the following shells/languages: bash, go, cmd,
   powershell.
#. You are familiar with how services work on all three platforms.
#. You are comfortable writing scripts.
#. You can take a generalized command and figure out the specifics
   (e.g. permissions).
#. You can read man pages, and Google if you need to.

Fit & Purpose
*************
I do not consider these setups to be 'secure' in any way shape or form, these
simply get you started off on the right foot. Don't make the assumption that
since this is setup, it is secure. It most definitely is not so. These are not
setup to be massive services either -- don't use these scripts to setup your
business or corporate environment -- you're doing it wrong. For the home gamer,
proceed.

Although I haven't done anything malicious, you should never blindly run
scripts & commands from the internet.

Bugs & Security Concerns
************************
Use :ref:`service-letsencrypt` for free SSL/TLS certs. There's **NO REASON** to
run self-signed certs anymore for hosting anything. Don't do it. Get a Let's
Encrypt Cert.

If you find any bugs or security concerns, file a bug against this project on
git hub, or submit a CL :)

.. toctree::
  :hidden:
  :includehidden:
  :maxdepth: -1

  self

.. toctree::
  :caption: Application Configuration
  :hidden:
  :includehidden:
  :maxdepth: -1

  apps/authy
  apps/bash
  apps/chrome
  apps/git
  apps/gpg/index
  apps/mutt
  apps/putty
  apps/sublime-text/index
  apps/taskwarrior
  apps/vim

.. toctree::
  :caption: Configuration Management
  :hidden:
  :includehidden:
  :maxdepth: -1

  configuration-management/saltstack/index

.. toctree::
  :caption: Networking
  :hidden:
  :includehidden:
  :maxdepth: -1

  networking/netplan
  networking/ubiquiti/edge-os
  networking/ubiquiti/example-vlan-network/index

.. toctree::
  :caption: Operating Systems
  :hidden:
  :includehidden:
  :maxdepth: -1

  operating-systems/windows/10/index
  operating-systems/ubuntu/index

.. toctree::
  :caption: Virtualization
  :hidden:
  :includehidden:
  :maxdepth: -1

  virtualization/hypervisors/xenserver-xcpng/index
  virtualization/hypervisors/kvm/index

.. toctree::
  :caption: Containerization
  :hidden:
  :includehidden:
  :maxdepth: -1

  containerization/docker/index

.. toctree::
  :caption: Services
  :hidden:
  :includehidden:
  :maxdepth: -1

  services/airsonic/index
  services/beets/index
  services/certificate-authority/index
  services/crashplan/index
  services/dashmachine/index
  services/deluge/index
  services/digikam/index
  services/email/index
  services/fail2ban/index
  services/firefly/index
  services/gitea/index
  services/git-webhook-receiver/index
  services/imapsync/index
  services/letsencrypt/index
  services/lidarr/index
  services/mariadb/index
  services/mumble/index
  services/nginx/index
  services/nzbget/index
  services/pihole/index
  services/play-on/index
  services/plex/index
  services/postgres/index
  services/radarr/index
  services/signal/index
  services/sonarr/index
  services/ssh/index
  services/unifi/index
  services/zfs/index
  services/service-template

.. toctree::
  :caption: Game Servers
  :hidden:
  :includehidden:
  :maxdepth: -1

  game/7days/index
  game/conan/index

.. toctree::
  :caption: Scripts
  :hidden:
  :includehidden:
  :maxdepth: -1

  scripts/bulk-downloader-for-reddit
  scripts/copying-data
  scripts/scripts
  scripts/video-editing-conversion
  scripts/wiping-data
  scripts/youtube

.. toctree::
  :caption: Appendix
  :hidden:
  :includehidden:
  :maxdepth: -1

  glossary
  icon-explanation

.. toctree::
  :caption: Buildings Docs
  :hidden:
  :includehidden:
  :maxdepth: -1

  sphinx-style-guide
  sphinx-build
