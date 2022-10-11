.. _service-radarr-network:

Network
#######
Radarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. See :ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

See `Radarr reverse proxy reference <https://gist.github.com/IronicBadger/362c408d1f2c27a0503cb9252b508140#file-bash_aliases>`__.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Using Subdomains
****************
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
**************
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

.. note::
  Set ``radarr_url_base`` to **/radarr** before enabling the reverse-proxy.

  .. code-block:: yaml
    :caption: ``ansible_radarr_vars.yaml``

    radarr_url_base: '/radarr'
