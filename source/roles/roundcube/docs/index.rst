.. _service-roundcube:

Roundcube
#########
:term:`MUA` Webmail client.

Setup :term:`MTA` and :term:`MDA` before configuration. See
:ref:`service-mail`.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration

.. role:: radarr
  :galaxy:      https://galaxy.ansible.com/r_pufky/roundcube
  :source:      https://github.com/r-pufky/ansible_roundcube
  :service_doc: https://github.com/roundcube/roundcubemail/wiki
  :update:      2022-10-09
  :open:

  Roundcube should be run in an isolated network and proxied given the
  sensitive and exposed nature of the data and service.

  * Use the explicit **Common Name (FQDN)** for ``roundcube_imap_host`` URI.
    PHP requires certificate validation by default now; and should match the
    explicit FQDN on the certificate that the mail server uses.
  * ``roundcube_upload_max_filesize`` should match the max file size
    defined on the mail server ``POSTFIX_MESSAGE_SIZE_LIMIT``, accepted
    standard is now 25MB.

  `Reference <https://github.com/roundcube/roundcubemail/wiki/FAQ>`__

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
