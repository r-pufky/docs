.. _service-mumble:

`Mumble`_
#########
High quality VOIP server with public certificate authentication, encryption and
ACLs.

Uses :ref:`debian-server-base-install`.

Ports
*****
.. ports:: Mumble Ports
  :value0: 64738, {TCP}, {PUBLIC}, Server/Voice
  :value1: 64738, {UDP}, {PUBLIC}, Voice
  :open:

.. gflocation:: Important File Locations (Mumble)
  :file:    /etc/mumble-server.ini,
            /var/lib/mumble-server/mumble-server.sqlite
  :purpose: Configuration.,
            Server DB.
  :no_key_title:
  :no_caption:
  :no_launch:

Server Setup
************
.. code-block:: bash

  apt install mumble-server

.. literalinclude:: source/mumble-server.ini
  :caption: **0600 mumble-server mumble-server** ``/etc/mumble-server.ini``
  :emphasize-lines: 20-22

.. warning::
  Register password cannot be changed. Don't lose your password.

.. note::
 * ``SERVER_NAME`` appears in the public channel listing.
 * ``SERVER_URL`` is a reference URL for the channel.

.. code-block:: bash
  :caption: Re-configure package and set ``superuser`` mumble password.

  dpkg-reconfigure mumble-server
  systemctl start mumble-server

Mumble Administration
*********************
Adding New Member
=================
#. :cmdmenu:`RMB (on user) --> Register`
#. User should now appear with a :cmdmenu:`+` icon:

   .. image:: source/new-member-01.png

#. :cmdmenu:`RMB (root channel) --> Edit`

   .. image:: source/new-member-02.png

#. Select

   #. :cmdmenu:`Groups`
   #. Select group from the pulldown.
   #. Type in the user’s name (should autopopulate).
   #. :cmdmenu:`Add`
   #. :cmdmenu:`OK`

   .. image:: source/new-member-03.png

#. User should now be able to move into all properly created channels.

Create New Channel
==================
#. :cmdmenu:`RMB (root channel) --> Add`

   .. image:: source/create-channel-01.png

#. Type channel name, leave everything else alone:

   .. image:: source/create-channel-02.png

#. All permissions are inherited from the root channel, so as long as the user
   is added to the group, they have access to all channels created in that
   channel.

.. rubric:: References

#. `Setting superuser password <https://wiki.mumble.info/wiki/Running_Murmur#Setting_the_SuperUser_Password>`_
#. `Registering a mumble user <https://www.typefrag.com/mumble/tutorials/advanced-user-settings/>`_
#. `Creating a mumble channel <https://www.mumble.com/support/mumble-how-to-create-a-channel.php>`_

.. _Mumble: https://wiki.mumble.info/wiki/Main_Page
