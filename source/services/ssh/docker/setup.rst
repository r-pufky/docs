.. _service-ssh-docker-setup:

SSHD Docker Setup
#################
SSHD using docker to enable dynamic read-only chroot directories.

See `SSHD Docker and Documentation`_. This assumes a similiar setup to
:ref:`service-ssh-linux-setup` with the additional of chrooting users into
read-only directories.

Ports
*****
.. ports:: SSHD Docker Ports
  :value0: 55555, {TCP}, {EXPOSED}, SSH Connections
  :open:

Files
*****
.. files:: SSHD Docker Files
  :value0: /etc/ssh, SSHD configuration files
  :value1: /etc/authorized_keys,
           Authorized keys location (cannot be changed based on container)
  :value2: /data, Mounted data for users
  :open:

Docker Creation
***************

* The UID/GID for the defined SSH user should be set to a user/group that has
  access to your media.
* See :ref:`service-ssh-docker-basic-configuration` for example configuration.

.. code-block:: yaml
  :caption: Docker Compose

  sshd:
    image: panubo/sshd:latest
    restart: unless-stopped
    logging:
      driver: syslog
      options:
        tag: sshd
    ports:
      - '55555:22'
    environment:
      - SSH_ENBALE_ROOT=false
      - SSH_ENABLE_PASSWORD_AUTH=false
      - SFTP_MODE=true
      - SFTP_CHROOT=/data
      - GATEWAY_PORTS=false
      - TCP_FORWARDING=false
      - SSH_USERS={USER}:{UID}:{GID}
      - TZ=America/Los_Angeles
    volumes:
      - /data/sshd/sshd:/etc/ssh
      - /data/sshd/authorized_keys:/etc/authorized_keys
      - /data/media:/data/media:ro
      - /etc/localtime:/etc/localtime:ro

.. _SSHD Docker and Documentation: https://hub.docker.com/r/panubo/sshd
