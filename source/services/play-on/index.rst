.. _play-on:

Play-On
#######
Steaming service recorder.

Uses :ref:`w10-pro-base` and assumes post template setup scripts have
been run.

.. gtable:: System Requirements.
  :header: Memory,
           Disk
  :c0:     8GB
  :c1:     60GB
  :no_key_title:
  :no_caption:
  :no_launch:

.. gport:: Ports Exposed (Play-on)
  :port:     22,
             57331*
  :protocol: TCP,
             TCP/UDP
  :type:     External,
             External
  :purpose:  SSHD for sshfs connections.,
             For streaming to other playon apps.
  :no_key_title:
  :no_caption:
  :no_launch:

    .. note::
      Port ``57331`` is only used if you use playon to stream recordings /
      provide a media library; by default this can be safetly disabled.

.. gtable:: Services Used (Play-on)
  :header: Service,
           Purpose
  :c0:     SSH,
           CRD,
           RDC,
           Flash,
           Playon Server
  :c1:     SSHFS remote file access for copying videos.,
           Chrome Remote Desktop for remote login.,
           Remote desktop (localhost connection only) for Chrome Remote Desktop.,
           Adobe flash used for recording via playon.,
           mediamallserver.exe Server used to manage recordings and accounts.
  :no_key_title:
  :no_caption:
  :no_launch:

Server Setup
************

#. Setup :ref:`w10-hiding-local-desktop-crd`.
#. Setup :ref:`service-ssh-windows-setup` with only public key authentication.
#. Ensure you are connected via the VM console (not CRD) for install, otherwise
   installer will fail.
#. Install `Playon Desktop`_, but do not launch immediately.
#. Connect via CRD.
#. Launch Playon, skip through helper setup screens.

.. ggui:: Playon Video Settings
  :key_title: ⚙  --> Video Performance
  :option:    Quality,
              ☑,
              Advanced options › H.264 Recording Profile
  :setting:   HD,
              Allow resumable playback,
              High
  :no_section:
  :no_launch:

    .. note::
      All unmentioned options are disabled or unused.

.. ggui:: Playon System Check
  :key_title: ⚙  --> System Check
  :option:    Check
  :setting:   Notify Automatically
  :no_section:
  :no_launch:

.. ggui:: Playon Channels
  :key_title: ⚙  --> Channels
  :option:    ☐
  :setting:   Disable all channels not used
  :no_section:
  :no_launch:

    .. note::
      Disable all channels not used. Login to ones that are.

.. rubric:: References

#. `Playon Minimum requirements <https://www.playon.tv/support/minreqs>`_
#. `Playon User Guide <https://www.playon.tv/user-guide/intro>`_
#. `Port forwarding Playon <https://forums.webosnation.com/webos-apps-games/297294-port-forwarding-playon.html>`_

.. _Playon Desktop: https://www.playon.tv/getplayon
