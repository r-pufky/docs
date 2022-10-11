.. _service-deluge:

Deluge
######
Bittorrent downloader.

.. toctree::
   :hidden:
   :maxdepth: -1

   network

.. role:: deluge
  :galaxy:      https://galaxy.ansible.com/r_pufky/deluge
  :source:      https://github.com/r-pufky/ansible_deluge
  :service_doc: https://dev.deluge-torrent.org/wiki/UserGuide
  :update:      2022-10-08
  :open:

  * The UID/GID should be set to a user/group that has access to your media.
    All media clients should run under the same user to run correctly.
  * Your downloader will report the download path **mapped in the downloader
    service**. You need to map this exact path in Deluge for it to be able to
    post-process downloads properly.
  * Deluge **must** be connected to the Daemon to write configuration changes.
    Ensure you select ``Connect`` on ``Connection Manager`` when logging in.
  * ``max_upload_speed`` should be set to a non-zero number to enable
    downloads.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
