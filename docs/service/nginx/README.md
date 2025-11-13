# NGINX
Advanced Load Balancer, Web Server, Reverse Proxy, and Streaming.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.nginx][a]

## [Manual Configuration](manual/README.md)
This provides a way to place services behind a proxy and enforce SSL for those
applications, as well as being able to offer a clean namespace for multiple
microservices.

This setup will focus on creating a reverse proxy, enforcing SSL for all
connections using Let's Encrypt; and enforcing client certificate
authentication.

A detailed [Nginx Administration Handbook is here][b]


## Reference[^1]

[^1]: https://www.nginx.com

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: https://github.com/trimstray/nginx-admins-handbook/blob/master/README.md
