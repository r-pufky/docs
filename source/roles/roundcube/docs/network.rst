.. _service-roundcube-network:

Network
#######
Radarr should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. See :ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

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
