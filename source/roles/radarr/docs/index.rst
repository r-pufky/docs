.. _service-radarr:

Radarr
######
Movie Management.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration
   troubleshooting

.. role:: radarr
  :galaxy:       https://galaxy.ansible.com/r_pufky/radarr
  :source:       https://github.com/r-pufky/ansible_radarr
  :service_doc:  https://wiki.servarr.com/radarr
  :update:       2022-10-08
  :open:

  You can copy your existing configuration to ``radarr_config`` directory
  adjusting for paths.

  * The UID/GID should be set to a user/group that has access to your media.
    All media clients should run under the same user to run correctly.
  * Your downloader will report the download path **mapped in the downloader
    service**. You need to map this exact path in Radarr for it to be able to
    post-process downloads properly.
  * See :ref:`service-radarr-basic-configuration` for example configuration.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
