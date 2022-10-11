.. _service-wireguard-key-generation:

Key Generation
##############
Public/Private keys need to be generated for each machine using wireguard. A
barebones utility is provided, generated keys are not OS specific.

.. code-block:: bash
  :caption: **0755 user user** wggen

  #!/bin/bash
  # Generate wireguard keys.
  WG=/usr/bin/wg
  TEE=/usr/bin/tee

  if [ -z "$1" ]; then
      echo "Requires name for output files."
      exit 1
  else
      name=$1
  fi

  ${WG} genkey | ${TEE} ${1}.key | ${WG} pubkey > ${1}.pub
  chmod 0400 ${1}.{key,pub}

.. important::
  Standard precautions should be used for private key material. The private key
  will enable anyone to impersonate that client on the VPN.
