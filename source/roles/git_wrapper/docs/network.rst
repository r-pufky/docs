.. _service-gitea-network:

Network
#######
Gitea should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. See :ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

.. note::
  Adjust ``client_max_body_size`` to expected max size of data in a git change.

See `Gitea reverse proxy reference <https://docs.gitea.io/en-us/reverse-proxies/>`__.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Using Subdomains
****************
This requires a hard IP resolution. Hairpin NAT / NAT reflection will result in
the web front working but git pull/push/clones failing. This is due to the way
Gitea handles these requests with custom written handlers. Setup DNS resolution
or add to ``hosts`` file.

.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

`Reference <https://discuss.gogs.io/t/reverse-proxy-unauthorized-401-windows/2057>`__

Using Subpaths
**************
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

SSL Client Cert Authentication
******************************
A reverse proxy requiring SSL client certification authentication requires no
change in the Gitea configuration.

See :ref:`service-nginx-cert-auth-git` to configure your git client.
