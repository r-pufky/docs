# [High Availability (HA)][a]
High availability enables automatic management of workloads to different
cluster nodes when problems arise. It is **not** required to run workloads.
Workloads must **explicitly** be added to the HA environment to benefit.

!!! warning "Requires shared storage and backbone network."
    See [Mount PVE Storage][b] and [Create Cluster][c].

### Setup

!!! example "Datacenter ➔ Options"
    * Migration Settings: **type=secure**
    * Replication Settings: **type=secure**
    * HA Settings: **shutdown_policy=migrate**

    Use secure data transfer on backbone network for Migration and Replication.
    Automatically migrate workloads to other cluster nodes when hosting node is
    shutdown.

### Workloads

#### NFS Mountpoints
HA migrations require [shared=1][d] on NFS mountpoints manually guaranteeing
those mounts will exist on the target node, otherwise migration will fail.

!!! abstract "/etc/pve/lxc/{VMID}.conf"
    0644 root:root

    ``` bash
    mp0: /d/source,mp=/d/dest,shared=1
    ```

#### Affinity Rules
Dictate how workloads are migrated to other nodes including node and workload
avoidance.

##### GPU Passthrough Avoidance
These rules set two nodes to avoid each other on cluster nodes, falling back to
node 2 when either node 1 or 3 are offline.

!!! example "Datacenter ➔ HA ➔ Affinity Rules ➔ HA Node Affinity Rules ➔ Add"
    * Enabled: ✔
    * HA Resources: **100**  # Node ID.
    * Strict: ✘
    * Affinity: **Prefer Nodes (positive)**
    * Comment: **Prefer nodes: 3,2,1 (avoid 107 GPU use).**
    * Nodes: hv1:1,hv2:2,hv3:3

!!! example "Datacenter ➔ HA ➔ Affinity Rules ➔ HA Node Affinity Rules ➔ Add"
    * Enabled: ✔
    * HA Resources: **107**  # Node ID.
    * Strict: ✘
    * Affinity: **Prefer Nodes (positive)**
    * Comment: **Prefer 1,2,3 (avoid 100 GPU use).**
    * Nodes: hv1:3,hv2:2,hv3:1

#### Migrate Existing Workload to HA
Existing VM's and containers can be migrated to HA but require manual updates
to [Mountpoints](#nfs-mountpoints) and [Affinity Rules](#affinity-rules).

!!! example "Node ➔ Workload ➔ More ➔ Manage HA"
    * Max Restart: ✔
    * Max Relocate: ✔
    * Failback: ✔
    * Auto-Rebalance: ✔
    * Request State: started
    * HA Resources: **100**  # Node ID.
    * Strict: ✘
    * Affinity: **Prefer Nodes (positive)**
    * Comment: **Prefer nodes: 3,2,1 (avoid 107 GPU use).**
    * Nodes: hv1:1,hv2:2,hv3:3

[a]: https://pve.proxmox.com/wiki/High_Availability
[b]: nfs.md#mount-pve-storage
[c]: README.md#create-cluster
[d]: https://pve.proxmox.com/pve-docs/chapter-pvesm.html
