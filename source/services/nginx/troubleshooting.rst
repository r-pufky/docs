.. _service-nginx-troubleshooting:

NGNIX Troubleshooting
#####################

Validating Upstream Parameters
******************************
To validate parameters passed to upstream services, the request should be dumped
by the service or intercepted by another service temporarily. There is a `docker
container to do this`_. This will dump the recieved headers from both http
and https communication to the upstream service.

.. code-block:: yaml
  :caption: **0640 root root** ``docker-compose.yml``

  http-echo:
    image: mendhak/http-https-echo

.. code-block:: nginx

  location / {
     proxy_pass http://http-echo/;
  }

.. note::
  Headers will be dumped directly to the page.

.. _service-nginx-debug-nginx-configs:

Debug NGINX configs
*******************
There is no existing logging functionality in NGINX to write directly to logs
from configuration files. Work around by directly injecting `debugging headers`_
in configuration files to dump information to logs. NGINX variables may be used
as well.

.. code-block:: nginx

  add_header X-debug-message "some message to write $ssl_client_s_dn" always;

Headers are found in the page response.

.. image:: source/debug-headers.png

.. _if-is-evil:

If is Evil
**********
If operates as a rewrite and is `inherently misunderstood`_.

Within a location block the only **safe** operations are:

* ``return``.
* ``rewrite``.

**All** if operations must be explicitly tested for `appropriate behavior`_.
Other `evil examples`_.

Dump Loaded NGINX Configuration
*******************************
Dump the currently loaded configuration in config file formatting. Useful to
inspect `current nginx state`_.

.. code-block:: bash

  nginx -T

NGINX Queries Originate from Wrong Gateway
******************************************
`Docker does not provide a way`_ to set the `appropriate default gateway`_ for
multi-network containers. This results in `non-deterministic`_ source IP
`routing`_.

.. warning::
  When a container is connected to multiple networks, its external connectivity
  is provided via the first non-internal network, in lexical order.

NGINX expresses this bug by forwarding/proxying any traffic **over** the default
gateway for the first lexical named network that appears.

The current fix is to inspect the container and find the first ``gateway``
listed in the connected networks. This will be the ``default gateway`` for the
container.

There is currently no clean way to set a default gateway via compose.

.. code-block:: bash

  docker inspect proxy_nginx_1

Forward Traffic via Specific Interfaces
***************************************
NGINX can forward traffic via `specific interfaces`_ for *location* definitions.

.. code-block:: yaml
  :caption: **0640 root root** ``{SERVICE}/docker-compose.yml``

  networks:
    custom_net_name:
      external: true

  services:
    my_proxy:
      networks:
        my_proxy_network:
          ipv4_address: 172.1.1.1
        custom_net_name:
          ipv4_address: 172.2.1.1

* ``custom_net_name`` is a network defined in another container. Once this is
  added, the proxy container will be able to do DNS resolution of container
  names as usual, including proxying traffic to that network.
* Use IPv4 address for ``proxy_bind`` command for specific locations.

.. code-block:: nginx

  location / {
    proxy_bind {NGINX NETWORK IP};
    proxy_pass ...
  }

Not Starting with Docker Services
*********************************
Expresses as NGINX not starting or failing to resolve if running (and backend
services were restarted or down at some point).

See :ref:`service-nginx-reverse-proxy-backends` to resolve.

.. code-block:


.. _docker container to do this: https://github.com/mendhak/docker-http-https-echo
.. _debugging headers: https://serverfault.com/questions/404626/how-to-output-variable-in-nginx-log-for-debugging
.. _inherently misunderstood: https://www.nginx.com/resources/wiki/start/topics/depth/ifisevil/
.. _evil examples: https://agentzh.blogspot.com/2011/03/how-nginx-location-if-works.html
.. _appropriate behavior: https://serverfault.com/questions/687033/nginx-use-geo-module-with-allow-deny-directives
.. _current nginx state: https://stackoverflow.com/questions/12832033/dump-conf-from-running-nginx-process
.. _Docker does not provide a way: https://github.com/docker/libnetwork/issues/1141#issuecomment-215522809
.. _appropriate default gateway: https://stackoverflow.com/questions/36882945/change-default-route-in-docker-container
.. _non-deterministic: https://dustymabe.com/2016/05/25/non-deterministic-docker-networking-and-source-based-ip-routing/
.. _routing: https://github.com/moby/moby/issues/21741
.. _specific interfaces: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#proxy_bind
