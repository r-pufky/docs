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

* :ref:`windows-10-pro-setup`
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
Use `letsencrypt`_ for free SSL/TLS certs. There's **NO REASON** to run
self-signed certs anymore for hosting anything. Don't do it. Get a Let's Encrypt
Cert.

If you find any bugs or security concerns, file a bug against this project on
git hub, or submit a CL :)

.. _letsencrypt: https://letsencrypt.org

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
  apps/chrome
  apps/gpg/index
  apps/mutt
  apps/putty
  apps/sublime-text/sublime
  apps/taskwarrior

.. toctree::
  :caption: Configuration Management
  :hidden:
  :includehidden:
  :maxdepth: -1

  Saltstack <configuration-management/saltstack/index>

.. toctree::
  :caption: Networking
  :hidden:
  :includehidden:
  :maxdepth: -1

  Netplan <networking/netplan>
  EdgeOS <networking/ubiquiti/edge-os>
  Example Unifi VLAN <networking/ubiquiti/example-vlan-network/index>

.. toctree::
  :caption: Operating Systems
  :hidden:
  :includehidden:
  :maxdepth: -1

  Windows 10 <operating-systems/windows/10/index>
  Ubuntu <operating-systems/ubuntu/index>

.. toctree::
  :caption: Virtualization
  :hidden:
  :includehidden:
  :maxdepth: -1

  Xenserver / XCP-NP <virtualization/hypervisors/xenserver-xcpng/index>
  KVM <virtualization/hypervisors/kvm/index>
  virtualization/vm-templates/index

.. toctree::
  :caption: Containerization
  :hidden:
  :includehidden:
  :maxdepth: -1

  Docker <containerization/docker/index>

.. toctree::
  :caption: Services
  :hidden:
  :includehidden:
  :maxdepth: -1

  services/airsonic/index
  services/beets/index
  services/crashplan/index
  services/deluge/index
  services/nginx/index
  services/certificate-authority/index

.. toctree::
  :caption: Scripts
  :hidden:
  :includehidden:
  :maxdepth: -1

  scripts/copying-data
  scripts/video-editing-conversion
  scripts/wiping-data
  scripts/youtube
  scripts/scripts

.. toctree::
  :caption: Appendix
  :hidden:
  :includehidden:
  :maxdepth: -1

  glossary
  style-guide