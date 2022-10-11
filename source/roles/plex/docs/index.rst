.. _service-plex:

Plex Media Server
#################
Media streaming service.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   troubleshooting

.. role:: plex
  :galaxy:      https://galaxy.ansible.com/r_pufky/plex
  :source:      https://github.com/r-pufky/ansible_plex
  :service_doc: https://support.plex.tv/articles/
  :update:      2022-10-08
  :open:

  You can copy your existing library from ``/var/lib/plexmediaserver/*`` to
  ``plex_library`` to auto-import your existing plex library.

  * The UID/GID should be set to a user/group that have access to your media.
    All media clients should run under the same user to run correctly.
  * Map your media directly to where it was before to prevent needing to modify
    any libraries. This should be read-only.
  * ``plex_transcode_memory`` maps a portion of RAM to tmpfs for transcoding,
    ensure there is enough memory in the system.
  * ``plex_online_token`` token is used to identify the server for your
    account. See :ref:`service-plex-defaults` for detailed information on
    obtaining token.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

.. _service-plex-defaults:

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
