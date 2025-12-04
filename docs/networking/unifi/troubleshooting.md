# Troubleshooting


## Slow Adoption
Device adopted multiple times as it is configured by the UniFi Controller.

**Wait** 3-5 minutes or 2-3 cycles.

Adoption takes a few minutes and may look like it is failing. Generally this
will be 3-5 minutes with typically 2 power cycles for it to finish.


## Adoption Failure
Controller is directly connected device but consistently fails adoption.

**Restart** the controller.


## Consistently Failing Repeated Adoptions
Adoption device **must** be connected to [Management VLAN][a] for adoption.

* Ensure controller is on port that allows same VLAN traffic as the set in the
  hardware.
* **Restart** switch if port profiles were changed.
* Ensure controller is listening on the correct IP.
* Ensure the hardware is set to inform to the correct controller IP.
* Alternatively directly connect the UniFi controller to switch with the device
  connected to it.


## Cannot Set Port Name
Port names **cannot** be the same name as the **profile name** being used.


## CPU Load is Extremely High on UniFi Switch
UniFi Switches run a realtime OS, and you will see consistent CPU utilization
[regardless of switch load][b]. This is an artifact of how load is measured.

Nothing is wrong.


## DHCP Not Working
Typically a MAC address caching issue, or Trunking ports are swapped/wrong.


## Caching Issue
Caused by swapping networks with the same device too quickly or caches not
being expired when new VLANs are setup.

1. Physically disconnect device from network wait a few seconds and re-connect.
2. Restart DHCP services on the router.


## Trunking ports Swapped/Wrong
Trunk VLANs do not match on Upstream or Downstream ports. If DHCP was confirmed
working before final placement, it is probably a swapped connection.

Verify the device downstream is the **correct device** using the same trunk
**port profile**.

[a]: ../../glossary/vlan.md#management-vlan-default
[b]: https://community.ui.com/questions/6068efd3-bc6f-4db3-b2f1-ee1fba98c178
