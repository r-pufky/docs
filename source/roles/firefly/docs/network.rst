.. _service-firefly-network:

Network
#######
Firefly should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. See :ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

Set ``firefly_trusted_proxies`` to ``**`` or specific proxy IP before enabling
the reverse-proxy.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Using Subdomains
****************
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpath
*************
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``
