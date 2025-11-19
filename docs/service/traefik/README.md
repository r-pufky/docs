# Traefik
Application Proxy.

!!! example "Migrated to ansible collection"
    Use [r_pufky.srv.traefik][a]

!!! tip
    * All defined routes are required to have a **router**, optionally
      **middleware**, and a backend **service**.
    * Using **@file** instructs Traefik to locate router/middleware/service
      definitions in local files.
    * Items defined in **web** and **webs** are applied globally to all routers
      that use that entrypoint. Middleware is layered with additional router
      definitions.
    * Examples use separate dynamic configuration files but it may be more
      beneficial in complex configurations to group definitions together by
      functionality (e.g. **dynamic/media.yml** or **dynamic/hypervisor.yml**).

## Concepts

### Install Configuration (traefik.yml)
Contains all parameters that require a **restart** of Traefik. This is
typically stored in **traefik.yml**.

### Routing Configuration (dynamic)
Contains all parameters that do not require a service restart and are reloaded
on file changes. This is typically stored in a **dynamic** directory.

Examples here use **file** providers for non-docker/kubernetes installs. There
are plenty of non-file examples.

### Routers
Define how incoming connections through **entrypoints** are directed to backend
**services**, optionally applying **middleware** as well as connection
requirements.

[HTTP Routing][b]

[TCP Routing][c]

[UDP Routing][d]

### Middleware
!!! note
    Traefik uses **middlewares** in configuration but **middleware** in
    documentation.

Manipulates incoming connection requests before sending to the backend service
or before responding to the client. UDP does not have middleware - Traefik does
maintain state to response to the correct clients - backend services must
manage this themselves.

[HTTP Middleware][e]

[TCP Middleware][f]

Middleware [chained][k] together using effectively grouping middleware in a
group to apply consistently across many routers.

### Service
Defines how incoming connections are distributed to backend services. All
services are load-balanced, even if there is only one backend.

[HTTP Service][h]

[TCP Service][i]

[UDP Service][j]


## Reference[^1]

[^1]: https://traefik.io/traefik
[^2]: https://github.com/Haxxnet/Compose-Examples/blob/main/examples/traefik/traefik.yml

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/srv/docs
[b]: https://doc.traefik.io/traefik/reference/routing-configuration/http/routing/router
[c]: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/routing/router
[d]: https://doc.traefik.io/traefik/reference/routing-configuration/udp/routing/router
[f]: https://doc.traefik.io/traefik/reference/routing-configuration/http/middlewares/overview
[e]: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/middlewares/overview
[h]: https://doc.traefik.io/traefik/reference/routing-configuration/http/load-balancing/service
[i]: https://doc.traefik.io/traefik/reference/routing-configuration/tcp/service
[j]: https://doc.traefik.io/traefik/reference/routing-configuration/udp/service
[k]: https://doc.traefik.io/traefik/reference/routing-configuration/http/middlewares/chain