.. _service-nzbget:

NZBGet
#######
Usenet downloader.

.. toctree::
   :hidden:
   :maxdepth: -1

   network

.. role:: nzbget
  :galaxy:      https://galaxy.ansible.com/r_pufky/nzbget
  :source:      https://github.com/r-pufky/ansible_nzbget
  :service_doc: https://nzbget.net/documentation
  :update:      2022-10-09
  :open:

  You can copy your existing configuration to ``nzbget_config`` directory
  adjusting for paths.

  * The UID/GID should be set to a user/group that has access to your media.
    All media clients should run under the same user to run correctly.
  * Your downloader will report the download path **mapped in the downloader
    service**. You need to map this exact path in Radarr for it to be able to
    post-process downloads properly.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml

