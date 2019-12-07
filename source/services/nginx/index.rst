.. _service-nginx:

NGINX Server
############
`Reverse proxy and load balancer`_ This provides a way to place services behind
a proxy and enforce SSL for those applications, as well as being able to offer a
clean namespace for multiple microservices.

This setup will focus on creating a docker-based reverse proxy, enforcing SSL
for all connections to docker containers using Let's Encrypt; and enforcing
client certification authentication.

See `NGINX Docker and Documentation`_.

A detailed `Nginx Administration Handbook is here`_.

#. :ref:`service-nginx-setup`.
#. :ref:`service-nginx-reverse-proxies`.
#. :ref:`service-nginx-custom-error-pages`.
#. :ref:`service-nginx-cert-based-authentication`.
#. :ref:`service-nginx-configuration-patterns`.
#. :ref:`service-nginx-troubleshooting`.

.. _NGINX Docker and Documentation: https://hub.docker.com/_/nginx
.. _Reverse proxy and load balancer: https://www.nginx.com/
.. _Nginx Administration Handbook is here: https://github.com/trimstray/nginx-admins-handbook/blob/master/README.md

.. toctree::
   :hidden:
   :maxdepth: -1

   setup
   reverse-proxies
   custom-error-pages
   cert-based-authentication
   configuration-patterns
   troubleshooting