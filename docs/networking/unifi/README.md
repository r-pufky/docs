# UniFi

### Security

#### [Telemetry](https://community.ui.com/questions/Update-UniFi-Phone-Home-Performance-Data-Collection/f84a71c9-0b81-4d69-a3b3-45640aba1c8b)
Options exists but are disable by default. Block or blackhole:
**trace.svc.ui.com**.

#### Default Login

 Username | Password
----------|----------
 ubnt     | ubnt
 root     | ubnt
 root     | ui

## Best Practices
* Always enable Layer 2 discovery (⚙ ➔ System ➔ Network Discovery: ✔) on
  controller. L2 device discovery will help to adopt controllers which are not
  receiving a [UniFi controller DHCP option](../edge_os/README.md#add-dhcp-server).
* Set a spare port on switches for [Management VLAN](../../glossary/vlan.md#management-vlan-default)
  or [ALL](../../glossary/vlan.md#all-all-networks) access so you can locally
  manage devices if something goes wrong.
* Always **factory-reset** equipment before configuring. This guarantees fresh
  state.
* Always physically label your switch ports so you can easily remember them
  when you come back in a year.
* Switches/APs/Routers should always have [static IP information](#set-static-ip-on-management-vlan)
  set, so they are at a known address if they ever get mis-configured. Plan and
  document static IPs for these devices before implementation.

## Configure Controller

### Define VLAN Networks
These should match VLAN networks defined at the router.

!!! example "⚙ ➔ Networks ➔ Net Virtual Network"
    * Name: **{NAME}**
    * Router: **Third Party Router**
    * VLAN ID: **{ID}**

### Define Port Profiles
Port profiles apply consistent settings across multiple ports. Highly recommend
defining trunking profiles and port profiles which are easy to understand:

!!! example "⚙ ➔ Overview ➔ Ethernet Port Profiles ➔ Create New"
    * trunk-all-default:
        * Native: **Default**
        * Tagged VLAN Management: **Allow All**
        * PoE: **Auto**
    * trunk-wifi:
        * Native: **Default**
        * Tagged VLAN Management: **Custom**
        * Tagged VLANs: **iot(3), wifi(4)**
        * PoE: **Auto**
    * trunk-iot:
        * Native: **Default**
        * Tagged VLAN Management: **Custom**
        * Tagged VLANs: **iot(3)**
        * PoE: **Auto**
    * port-wired:
        * Native: **wired(2)**
        * Tagged VLAN Management: **Block All**
    * port-wifi:
        * Native: **wifi(4)**
        * Tagged VLAN Management: **Block All**
    * port-iot:
        * Native: **iot(3)**
        * Tagged VLAN Management: **Block All**

## Set Static IP on [Management VLAN](../../glossary/vlan.md#management-vlan-default)
All managed devices should be set with a static IP on the
[Management VLAN](../../glossary/vlan.md#management-vlan-default) to ensure
they are at known locations in case the controller fails.

!!! example "Devices ➔ Switch ➔ Properties ➔ Config ➔ Network"
    * Network Override: ✔
        * Virtual Network: **Default**
    * Configure IP: **Static**
        * IP Address: **{VLAN1_IP}**
        * Preferred DNS: **{DNS}**
        * Subnet Mask: **{VLAN1_SUBNET}**
        * Gateway: **{ROUTER_IP}**
        * DNS Suffix: **{DOMAIN}**

## Migrating Controllers
The easiest migration path is to replace the controller with the same IP. This
requires no additional setup other than replacing the controller.

### New Controller IP

#### Update Inform IP and Backup Existing Controller
!!! example "Devices ➔ Device Updates and Settings ➔ Device Settings"
    * Inform Host Override: ✔
        * Controller Hostname/IP: **{NEW_IP}**

    Update for all devices. These devices **may** appear to disconnect from the
    controller - *this is expected*.

!!! example "⚙ ➔ System ➔ Backups ➔ Download"
    * Download Current Backup: **Settings Only**

    At least settings need to be downloaded. **Shutdown** original Controller.

#### Update [DHCP Inform Addresses](../edge_os/README.md#add-dhcp-server).

#### Start New Controller
!!! example "⚙ ➔ System ➔ Backups ➔ Restore"
    Update controller IP after restoring from settings.

### Manually Update Devices
Some devices may not pickup the new inform IP of the new controller. These may
be manually set if SSH is enabled; otherwise factory reset them and re-adopt -
current settings are stored in the
[backup](#update-inform-ip-and-backup-existing-controller).

Manually Update Controller Inform IP on Device
``` bash
ssh root@{DEVICE}  # Use SSH account that is setup in controller.

info

# Device should appear within a minute.
set-inform http://{IP}:8080/inform
```

## References

* https://dl.ubnt.com/guides/UniFi/UniFi_Controller_V5_UG.pdf
* https://www.youtube.com/watch?v=b2w1Ywt081o
* https://www.youtube.com/watch?v=HcfIpTso_Ys
* https://www.youtube.com/watch?v=SKeFqFhBwJY&t=
* https://www.youtube.com/watch?v=L9gZQh1rAMc
* https://www.handymanhowto.com/ubiquiti-edgerouter-lite-soho-network-design/
* https://arstechnica.com/information-technology/2018/07/enterprise-wi-fi-at-home-part-two-reflecting-on-almost-three-years-with-pro-gear/5/
* https://help.ui.com/hc/en-us/articles/204962144#1
* https://help.ui.com/hc/en-us/articles/219654087-UniFi-Using-VLANs-with-UniFi-Wireless-Routing-Switching-Hardware
