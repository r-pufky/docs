.. _unifi-device-troubleshooting:

Unifi Device Troubleshooting
############################

Slow Adoption
*************
On initial adoption the switch may be adopted multiple times as it is configured
by the Unifi Controller. Adoption takes a few minutes and may look like it is
failing. Generally this will be 3-5 minutes with typically 2 power cycles for it
to finish.

* *Wait* 3-5 minutes or 2-3 cycles.

.. _unifi-adoption-failure:

Adoption Failure
****************
Controller is directly connected device, but consistently fails adoption. This
is caused by the controller getting wedged.

* *Restart* the controller.

Consistenly Failing Repeated Adoptions
**************************************
Once hardware has the :term:`Management VLAN` set in device configuration
:cmdmenu:`Properties --> config --> services --> vlan --> management vlan`, the
Unifi controller must be listening a :term:`Management VLAN` for the controller
to be adopted.

* Ensure controller is on port that allows same VLAN traffic as the
  :term:`Management VLAN` set in the hardware.
* Ensure controller is listening on the correct IP.
* Ensure the hardware is set to inform to the correct controller IP.
* Alternatively, directly connect the unifi controller to the switch with the
  AP connected to it.

Cannot Set Port Name
********************
Port names **cannot** be the same name as the *profile name* being used.

CPU Load is Extremely High on Unifi Switch
******************************************
Unifi Switches run a realtime OS, and you will see consistent CPU utilization
`regardless of switch load`_. This is an artifact of how load is measured.
Nothing is wrong.

DHCP Not Working
****************
Typically a MAC address caching issue, or Trunking ports are swapped/wrong.

Caching Issue
**************
Caused by swapping networks with the same device too quickly, or caches not
being expired when new VLANs are setup.

#. Physically disconnect device from network, wait a few seconds and re-connect.
   If it works, you're done.
#. Restart DHCP services on the edgerouter.

.. code-block:: bash
  :caption: Restart DHCP on EdgeOS (EdgeOS CLI).

  sudo service dhcpd restart

Trunking ports Swapped/Wrong
****************************
Trunk VLANs do not match on Upstream or Downstream ports. If DHCP was confirmed
working before final placement, it is probably a swapped connection.

Verify the device downstream is the *correct device* using the *same trunk port
profile*.

.. ucontroller:: Add Static Host
  :key_title:    Devices -->
                 {UPSTREAM SWITCH} -->
                 Properties -->
                 Ports -->
                 Status
  :option:       Downlink,
                 Profile
  :setting:      {EXPECTED SWITCH},
                 {EXPECTED SWITCH PORT PROFILE}
  :no_section:
  :no_caption:

.. ucontroller:: Add Static Host
  :key_title:    Devices -->
                 {DOWNSTREAM SWITCH} -->
                 Properties -->
                 Ports -->
                 Status
  :option:       Downlink,
                 Profile
  :setting:      {EXPECTED SWITCH},
                 {EXPECTED SWITCH PORT PROFILE}
  :no_section:
  :no_caption:

.. _regardless of switch load: https://community.ubnt.com/t5/UniFi-Routing-Switching/UniFI-Switch-8-POE-60-W-constant-high-CPU-utilization/td-p/2397994