.. _service-nginx-reverse-proxies:

Adding Reverse Proxies
######################
This will cover the basic usage of NGINX as a reverse proxy; covering services
on the URI path, not as a custom subdomain. See subdomain reverse proxy for
setting up subdomains.

Use reference documentation and location block references for additional
information.

``location`` blocks should be placed in the ``server`` block.

`Reference <https://community.home-assistant.io/t/nginx-reverse-proxy-set-up-guide-docker/54802>`__

`Reference <https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/>`__

`Reference <https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms>`__

Service Gotchas
***************
Ensure the services running behind the proxy are in a known configuration:

* Running on expected protocols (http or https) and ports.
* Have firewalls setup to only allow traffic in/out of those ports to and from
  the proxy.

Trailing Slash Gotchas
======================
In Short:

* Services already using URI paths for the services should leave **off**
  trailing slashes in ``location`` and ``proxy_pass``.
* Services using **no** additional URI paths for services should use trailing
  slashes in ``location`` and ``proxy_pass``.

Explanation:

If the ``proxy_pass`` directive is specified with a URI, then when a request is
passed to the server, the part of a *normalized request URI matching the
location is replaced by a URI specified in the directive*:

.. code-block:: nginx
  :caption: Trailing slash example.

  location /name/ {
    proxy_pass http://app/remote/;
  }

* Assume request: ``http://proxy/name/path?params=1``.
* ``http://app/remote/`` sees request as ``https://app/remote/path?params=1``.
* Essentially the matched URI path is **removed** and the rest is passed as
  though it was called from app's page.

If ``proxy_pass`` is specified without a URI, the request URI is passed to the
server *in the same form* as sent by a client when the original request is
processed, or the *full normalized request URI is passed when processing the
changed URI*:

.. code-block:: nginx
  :caption: No trailing slash example.

  location /name/ {
      proxy_pass http://app/remote;
  }

* Assume request: ``http://proxy/name/path?params=1``.
* ``http://app/remote/`` sees request as ``https://app/remote/name/path?params=1``.
* Essentially the URI path is **concatenated** to the end of the remote path.

`Reference <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass>`__

`Reference <https://stackoverflow.com/questions/22759345/nginx-trailing-slash-in-proxy-pass-url>`__

Regex Versus Trailing Slashes
=============================
Most examples on the web use regex, but regex is generally slow, error prone
and hard to read. In NGINX most regexes may be replaced with trailing slash to
replace the matched URI path instead. It's cleaner and easier to read, and
usually covers the regex case.

.. code-block:: nginx
  :caption: Web Regex Example (**bad**) proxies ``/nzbget`` to ``https://nzbget:6791/``.

  location ~ ^/nzbget$ {
    return                302 $scheme://$host$request_uri/;
  }
  location ~ ^/nzbget($|./*) {
    rewrite               /nzbget/(.*) /$1 break;
    proxy_pass            https://nzbget:6791;
    include               /etc/nginx/conf.d/proxy.conf;
    proxy_set_header Host $host;
  }

* First rule regex matches ``nzbget`` and returns a **302** to the same URI
  with a trailing slash.
* Second rule accepts ``/nzbget`` with parameters and proxies to the service.
* This results in two proxy hits and two regex comprehensions; it's also hard
  to understand what the regex is doing immediately.

.. code-block:: nginx
  :caption: Using trailing slashes (**good**) proxies ``/nzbget`` to ``https://nzbget:6791/``.

  location /nzbget/ {
    proxy_pass            https://nzbget:6791/;
    include               /etc/nginx/conf.d/proxy.conf;
    proxy_set_header Host $host;
  }

`Reference <https://stackoverflow.com/questions/764247/why-are-regular-expressions-so-controversial>`__

Redirect Path to Base URI
*************************
.. code-block:: nginx
  :caption: For applications that serve ``https://app/``.

  location /gogs/ {
    proxy_pass https://gogs:3000/;
  }

.. note::
  Note trailing slashes.

Redirect Path to Service URI Path
*********************************
.. code-block:: nginx
  :caption: For applications that serve ``https://app/path``.

  location /sonarr {
    proxy_pass http://sonarr:8989/sonarr;
    include /etc/nginx/conf.d/proxy-control.conf;
  }

.. note::
  Note **no** trailing slashes.

Custom Path for Service
***********************
.. code-block:: nginx
  :caption: Enable different paths to the same service.

  location /tv {
    return     301 $scheme://$host/sonarr/;
  }
  location /sonarr {
    proxy_pass http://sonarr:8989/sonarr;
    include    /etc/nginx/conf.d/proxy-control.conf;
  }

.. note::
  **tv** will automatically redirect to **sonarr**.

Enable Websockets
*****************
.. code-block:: nginx
  :caption: Allow for apps requiring websockets to be used.

  location /crashplan/ {
    proxy_pass                    https://crashplan:5800/;
    include                       /etc/nginx/conf.d/proxy-control.conf;

    location /crashplan/websockify {
      proxy_pass                  https://crashplan:5800/websockify/;
      include                     /etc/nginx/conf.d/proxy-control.conf;
      proxy_set_header Upgrade    $http_upgrade;
      proxy_set_header Connection $connection_upgrade;
    }
  }

* Upgrade and Connection must be used, and pass values through the websocket map
  to enable the connection upgrade or close the connection.
* ``proxy_http_version 1.1`` is required, but included in
  ``proxy-control.conf``.

Rewrite Reponses with Subpath
*****************************
Some applications are not URI Path aware and will re-write all responses behind
the proxy using a static relative path or hostname; which will cause 404 errors
and the app to break. Partially fixed using http_sub_module.

.. note::
  Re-writing the proxy respones generally won't fix a complicated application as
  there will be a large number of unknown responses that need to be re-written.
  Usually this is resolved using a sub-domain instead.

.. code-block:: nginx

  sub_filter      https://app:port/ https://reverse-proxy-server/subpath/;
  sub_filter      'href="/' 'href="https://reverse-proxy-server/subpath/';
  sub_filter_once off;

* First rule rewrites responses from the app: ``https://app:port/page.html`` to
  ``https://reverse-proxy-server/subpath/page.html``.
* Second rules rewrites relative responses ``href="/other-page.html"`` to
  ``href="https://reverse-proxy-server/subpath/other-page.html"``.

`Reference <https://stackoverflow.com/questions/32542282/how-do-i-rewrite-urls-in-a-proxy-response-in-nginx>`__

`Reference <http://nginx.org/en/docs/http/ngx_http_sub_module.html>`__

.. _service-nginx-reverse-proxy-backends:

Enable NGINX Start/Running with Backends Down
*********************************************
By design NGINX will prevent startup or running if upstream backends are down
as it is intepreted to be a configuration error.

Services which are down may not resolve via DNS, and therefore will trigger
this condition, requiring all services to be up for NGINX to function.

Another expression is a long running NGINX server where a backend has been
restarted. This will mark the backend as bad and NGINX will no longer serve it
even though the service may be running now.

By specifying an explicit IP no DNS lookup is required which prevents the
service health check, allowing NGINX to start or run with backends down. This
will show ``502`` errors when the service is down. Does not affect
cert-based authentication setups.

.. code-block:: nginx
  :caption: Static IP for upstream service.

  upstream my-backend {
    server {IP}:{PORT};
  }

  server {
    listen 443 ssl http2;
    server_name myservice.example.com myservice;

    location / {
      proxy_pass http://my-backend;
    }
  }

`Reference <https://trac.nginx.org/nginx/ticket/1040>`__

`Reference <https://stackoverflow.com/questions/32845674/setup-nginx-not-to-crash-if-host-in-upstream-is-not-found>`__
