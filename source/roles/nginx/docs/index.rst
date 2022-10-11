.. _service-nginx:

NGINX
#####
Advanced Load Balancer, Web Server, Reverse Proxy, and Streaming. Started as a
web server designed for maximum performance and stability.

.. toctree::
   :hidden:
   :maxdepth: -1

   manual-configuration/index
   troubleshooting

.. role:: nginx
  :service_doc: https://nginx.org/en/docs/
  :ref:         https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
  :update:      2022-10-10
  :private:
  :open:

  Role handles all steps that are provided in this documentation. You must
  provide your own NGINX configuration files.

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml

Stream
******
.. literalinclude:: ../defaults/main/stream.yml
