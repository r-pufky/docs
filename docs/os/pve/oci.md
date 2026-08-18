# OCI
[PVE 9.1][a] supports direct OCI container execution without LXC/VM.

## Add OCI Image
!!! example "{NODE} ➔ {STORAGE} ➔ CT Templates ➔ Pull from OCI Registry"
    * Reference: **ghcr.io/{ORG}/{PROJECT}**  # Query tags before setting tag.
    * Tag: **{RELEASE}**

## Creation
Very similar to LXC container creation. Mount options can be added via advanced
options or directly in **/etc/pve/lxc/{ID}.conf** before starting.

!!! info "Currently OCI conversions can **only** mount disk images for container mount points, not bind mounts."
    * Only use SSH key as there is **no login user**.
    * Use Proxmox Firewall. Most containers do **not** have built-in firewalls.
    * Directly add data disk during creation:
        * Mount Point ID: **0**
        * Disk size: **1**
        * Path: **/app/config**  # Use OCI image mount points.
        * Backup: ✔
        * Mount options: **discard, noatime**

## [Upgrade OCI Container][a]
To upgrade an OCI container it must be deleted and re-created with the new
image.

[Prepare Config (State) Disk](#config-state-disk-preparation) first.

!!! example "{LXC} ➔ More ➔ Remove"
    * Purge from job configuration: ✔
    * Destroy unreferenced disks owned by guest: ✘

[Create OCI container](#creation) as normal,
[attaching existing config disk](#config-state-disk-preparation) before
starting the new container.

!!! warning "Re-create PVE firewall rules"
    Most containers do not have firewalls built in and existing rules are
    removed when the container is deleted.

## Config (State) Disk Preparation
Most OCI containers have a specific disk used to persistent state. Backup disk
then use either method to [prevent the disk from being deleted][b] during the
upgrade.

!!! warning "Always make a manual backup of the config disk"
    ``` bash
    cp /d/pve/images/{VID}/vm-{VID}-disk-1.raw /d/pve/images/oci-images
    ```

Use either CLI or WebUI preparation.

### CLI Preparation
``` bash
cp /d/pve/images/{VID}/vm-{VID}-disk-1.raw /d/pve/images/oci-images
vim /etc/pve/lxc/{VID}.conf  # Remove mounted config disk.

# Perform container upgrade (see: Upgrading), then remount disk.
cp /d/pve/images/oci-images /d/pve/images/{VID}/vm-{VID}-disk-1.raw
vim /d/pve/lxc/106.conf  # Add mounted config disk.
```

### WebUI Preparation
Move disk to another container temporarily during upgrade.

!!! example "{LXC} ➔ Resources ➔ MP{#} ➔ Volume Action ➔ Reassign Owner"
    * Target Guest: **{TEMP HOST}**
    * Add as: **Unused 1**

[Create new container](#upgrade-oci-container).

!!! example "{LXC} ➔ Resources ➔ MP{#} ➔ Volume Action ➔ Reassign Owner"
    * Target Guest: **{UPGRADE HOST}**
    * Add as: **Mount point 1**

[a]: https://pve.proxmox.com/wiki/Linux_Container#pct_container_images
[b]: https://forum.proxmox.com/threads/pve-9-2-oci-data-disk-always-deleted-bug-or-working-as-intended.185778/#post-866221
