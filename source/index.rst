Docs: A Collection of Setup Notes
#################################
I created this repository as a response to people requesting I share my setup
notes for services I run in my home. These notes have been made generic enough
so that you can implement these services and setups with relative ease. Be sure
to check the :ref:`glossary` if you see unknown symbols.

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

  docs/apps/authy
  docs/apps/bash
  docs/apps/chrome
  docs/apps/git
  docs/apps/gpg/index
  docs/apps/movie-studio
  docs/apps/mutt
  docs/apps/putty
  docs/apps/python-venv
  docs/apps/realtek-nahimic
  docs/apps/sublime-text/index
  docs/apps/taskwarrior
  docs/apps/vim

.. toctree::
  :caption: Configuration Management
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/configuration-management/ansible/index

.. toctree::
  :caption: Networking
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/networking/netplan
  docs/networking/ubiquiti/edge-os
  docs/networking/ubiquiti/example-vlan-network/index

.. toctree::
  :caption: Operating Systems
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/operating-systems/manjaro/index
  docs/operating-systems/ubuntu/index
  docs/operating-systems/windows/base/index
  docs/operating-systems/windows/10/21H2/index
  docs/operating-systems/windows/10/20H2/index
  docs/operating-systems/windows/11/index

.. toctree::
  :caption: Printing
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/printing/brother-mfcl2750dw/index

.. toctree::
  :caption: Virtualization
  :hidden:
  :includehidden:
  :maxdepth: -1

  roles/pve/docs/index

.. toctree::
  :caption: Services
  :hidden:
  :includehidden:
  :maxdepth: -1

  roles/acme/docs/index
  roles/ca/docs/index
  roles/crashplan/docs/index
  roles/deluge/docs/index
  roles/dropbear/docs/index
  roles/mail/docs/index
  roles/fail2ban/docs/index
  roles/firefly/docs/index
  roles/git_wrapper/docs/index
  docs/services/imapsync/index
  roles/lidarr/docs/index
  roles/db/docs/mariadb/index
  docs/services/mumble/index
  roles/nginx/docs/index
  roles/nzbget/docs/index
  roles/steam/docs/index
  roles/pihole/docs/index
  docs/services/play-on/index
  roles/plex/docs/index
  roles/db/docs/postgres/index
  roles/radarr/docs/index
  roles/roundcube/docs/index
  roles/sonarr/docs/index
  roles/sshd/docs/index
  roles/unifi/docs/index
  roles/wireguard/docs/index
  roles/zfs/docs/index

.. toctree::
  :caption: Game Servers
  :hidden:
  :includehidden:
  :maxdepth: -1

  roles/steam/docs/satisfactory
  roles/steam/docs/seven_days_to_die
  roles/steam/docs/conan_exiles
  roles/steam/docs/left_4_dead
  roles/steam/docs/left_4_dead_2

.. toctree::
  :caption: Scripts
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/scripts/bulk-downloader-for-reddit
  docs/scripts/copying-data
  docs/scripts/scripts
  docs/scripts/steam-older-game-versions
  docs/scripts/video-editing-conversion
  docs/scripts/wiping-data
  docs/scripts/youtube

.. toctree::
  :caption: Appendix
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/glossary
  docs/icon-explanation

.. toctree::
  :caption: Buildings Docs
  :hidden:
  :includehidden:
  :maxdepth: -1

  docs/sphinx-style-guide
  docs/sphinx-build
