.. _play-on:

Play-On
#######
Steaming service recorder.

Uses :ref:`wbase` and assumes post template setup scripts have
been run.

System Requirements

+--------+------+
| Memory | Disk |
+========+======+
| 8GB    | 60GB |
+--------+------+

Ports
*****
.. ports:: Play-on Ports
  :value0:    22,     {TCP},  {PUBLIC}, SSHD for sshfs connections
  :value1: 57331, {TCP/UDP}, {DISABLE}, For streaming to other playon apps
  :open:

  .. note::
    Port ``57331`` is only used if you use playon to stream recordings /
    provide a media library; by default this can be safetly disabled.

+---------------+-----------------------------------------------------------------------+
| Service       | Purpose                                                               |
+===============+=======================================================================+
| SSH           | SSHFS remote file access for copying videos.                          |
+---------------+-----------------------------------------------------------------------+
| CRD           | Chrome Remote Desktop for remote login.                               |
+---------------+-----------------------------------------------------------------------+
| RDC           | Remote desktop (localhost connection only) for Chrome Remote Desktop. |
+---------------+-----------------------------------------------------------------------+
| Flash         | Adobe flash used for recording via playon.                            |
+---------------+-----------------------------------------------------------------------+
| Playon Server | mediamallserver.exe Server used to manage recordings and accounts.    |
+---------------+-----------------------------------------------------------------------+

Server Setup
************

#. Setup :ref:`wbase-specific-windows-fixes-hiding-local-desktop-crd`.
#. Setup :ref:`service-ssh-windows-service` with only public key
   authentication.
#. Ensure you are connected via the VM console (not CRD) for install, otherwise
   installer will fail.
#. Install `Playon Desktop`_, but do not launch immediately.
#. Connect via CRD.
#. Launch Playon, skip through helper setup screens.

.. gui::   Playon Video Settings
  :path:   ⚙  --> Video Performance
  :value0: Quality, HD
  :value1: ☑, Allow resumable playback
  :value2: Advanced options › H.264 Recording Profile, High
  :open:

  .. note::
    All unmentioned options are disabled or unused.

.. gui::   Playon System Check
  :path:   ⚙  --> System Check
  :value0: Check, Notify Automatically
  :open:

.. gui::   Playon Channels
  :path:   ⚙  --> Channels
  :value0: ☐, Disable all channels not used
  :open:

  .. note::
    Disable all channels not used. Login to ones that are.

.. rubric:: References

#. `Playon Minimum requirements <https://www.playon.tv/support/minreqs>`_
#. `Playon User Guide <https://www.playon.tv/user-guide/intro>`_
#. `Port forwarding Playon <https://forums.webosnation.com/webos-apps-games/297294-port-forwarding-playon.html>`_

.. _Playon Desktop: https://www.playon.tv/getplayon
