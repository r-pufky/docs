.. _service-plex-network:

Network
#######
Reverse proxy configurations have not be finalized yet.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Enable Secure Server Connection
*******************************
* Ensure ``32400`` is forwarded from the router.
* Enable `DNS Rebinding <https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections/>`_
  on router.

If not using a plex claim token or manual port forwarding you may need to setup
plex manually from the machine.

.. code-block:: bash
  :caption: Setup SSH port forward.

  ssh -L 32400:{HOST}:32400 -N {USER}@{HOST}

Then nagivate to http://localhost:32400/web/index.html to finish setup.
