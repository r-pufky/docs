.. _service-pihole-force-https-admin:

Force HTTPS Admin Page
######################
HTTPS should only be enabled for the FQDN of the Pi-Hole server; as the server
is redirecting traffic, you may get a bunch of `cert wonkiness when DNS resolves
return blocked domains`_.

.. code-block:: bash
  :caption: Create a combined certificate.

  sudo cat privkey.pem cert.pem | sudo tee combined.pem
  sudo chmod www-data -R combined.pem

.. note::
  This contains private information and should not be placed in a web directory.

.. literalinclude:: source/external.conf
  :caption: **0644 root root** ``/etc/lighthttpd/external.conf``

.. code-block:: bash
  :caption: Restart services.

  sudo service lighthttpd restart

.. _cert wonkiness when DNS resolves return blocked domains: https://discourse.pi-hole.net/t/enabling-https-for-your-pi-hole-web-interface/5771