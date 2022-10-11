.. _example-vlan-network:

Example Unifi VLAN
##################
Edgerouter using Docker Unifi Controller with VLAN Setup.

Example walkthorugh of creating a VLAN based network using an edgerouter as a
router/firewall with a Docker Unifi Controller managing Unifi Switch/APs.

.. danger::
  The most recent firmware update (~2019-10) has added `telemetry`_ to ubiquity
  devices; disabled by default.

  **Block or blackhole** ``trace.svc.ui.com``.

Read through :ref:`network-overview` and prep these things before starting:

* Always set an spare port on your router with a static management address
  without VLANS so you can get in if something breaks.
* Set a spare port on switches for :term:`Management VLAN` or :term:`ALL` access
  so you can locally manage devices if something goes wrong.
* Make *backups of existing Edgerouter & Unifi Controller configs*. Export all
  data.
* Install Unifi controller on a laptop.
* Set static IP for laptop, on the :ref:`Management Network <vlan-table>`.
* Always **factory-reset** equipment before configuring. This garantees fresh
  state.
* Always physically label your switch ports so you can easily remember them when
  you come back in a year.
* Switches/APs/Routers should always have static IP information set, so they are
  at a known address if they ever get mis-configured. Plan and document static
  IPs for these devices before implementation.

.. rubric:: References

#. `Create schedule task with event log trigger <https://stackoverflow.com/questions/42801733/creating-a-scheduled-task-which-uses-a-specific-event-log-entry-as-a-trigger>`_
#. `Unifi Controller V5 Manual <https://dl.ubnt.com/guides/UniFi/UniFi_Controller_V5_UG.pdf>`_
#. `VLANs with Unifi and PFSense <https://www.youtube.com/watch?v=b2w1Ywt081o>`_
#. `Complete UniFi Setup Start to Finish <https://www.youtube.com/watch?v=HcfIpTso_Ys>`_
#. `UAP with Guest WLAN & VLAN Trunks VIF <https://www.youtube.com/watch?v=SKeFqFhBwJY&t=>`_
#. `Unifi Enterprise Networking <https://www.youtube.com/watch?v=L9gZQh1rAMc>`_
#. `Ubiquiti EdgeRouter Lite SOHO Network Design <https://www.handymanhowto.com/ubiquiti-edgerouter-lite-soho-network-design/>`_
#. `This is software-defined networking, apparently <https://arstechnica.com/information-technology/2018/07/enterprise-wi-fi-at-home-part-two-reflecting-on-almost-three-years-with-pro-gear/5/>`_

.. _telemetry: https://community.ui.com/questions/Update-UniFi-Phone-Home-Performance-Data-Collection/f84a71c9-0b81-4d69-a3b3-45640aba1c8b

.. toctree::
   :hidden:
   :maxdepth: -1

   Initial Edgerouter Configuration <edgerouter-vlan>
   unifi-controller-vlan
   core-switch
   server-switch
   wired-switch
   unifi-controller-wifi
   unifi-ap
   migrate-controller-to-docker
   unifi-device-troubleshooting
   network-overview
   example-network-diagram
   vlan-101
