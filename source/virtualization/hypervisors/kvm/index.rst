.. _kvm:

KVM Server
##########
Basic KVM server setup on ubuntu (18.04).

Files
*****
.. files:: KVM Files
  :value0: /etc/libvirtd/, KVM and VM configuration data
  :value1: /var/lib/libvirt/images, Default KVM VM/ISO image pool Location
  :open:
  
Install Service
***************

.. code-block:: bash
  :caption: Ensure hardware can support virtualization.

  egrep -c '(vmx|svm)' /proc/cpuinfo

* Anything ``<= 0`` means that hardware virtualization is disabled or not
  supported with hardware
* AMD Processers: Check BIOS, ensure ``IMMOU`` and ``SVM`` is enabled.
* Intel processors: Check BIOS, ensure ``IMMOU`` and ``VT-d`` is enabled.

.. code-block:: bash
  :caption: Verify KVM accleration can be used.

  apt install cpu-checker
  kvm-ok

* This should clearly state if accleration can be used.

.. code-block:: bash
  :caption: Install KVM packages.

  apt install qemu qemu-kvm qemu-efi qemu-utils libvirt-bin libvirt-clients libvirt-daemon-system virt-manager

.. code-block:: bash
  :caption: Set user group permissions.

  adduser {USER} libvirt
  adduser {USER} libvirt-qemu

* This is so a normal user can run ``virt-manager``, instead of logging in as
  ``root``.

Add/Update storage pools
************************
By default a single location is used for VM's and ISO images. Create/map
additional locations for storage pools to mount ISO images to keep separate from
VM images.

.. code-block:: bash
  :caption: Launch VM manager with X11 forwarding enabled.

  virt-manager

.. ggui::     Add storage pool to KVM
  :key_title: Edit --> Connection Details --> Storage
  :option:    Name,
              Type,
              Target Path
  :setting:   {STORAGE POOL NAME},
              dir: Filesystem Directory,
              {STORAGE POOL LOCATION}
  :no_caption:
  :no_launch:

    .. note::
      Virtual machines should typically **not** have their own storage pool
      defined.

KVM Specific Issues
*******************
There seems to be an issue with Netplan bridging, KVM, and using the same
bridged for host networking traffic as well as VM traffic. The workaround is to
have a separate bridged adapter. This is a `longstanding bug`_ with KVM and
can be fixed by modifying `sysctl settings`_.

See :ref:`docker-bridged-adapters` to resolve Docker issues.

Create a Network Bridge
=======================
This is so VM's can get an IP on the host network, instead of using NAT.

.. code-block:: bash
  :caption: Show all network adapters (including currently unassigned) for
            usage.

  ip link show
  lspci | grep ethernet

.. literalinclude:: source/01-netcfg.yaml
  :caption: **0644 root root** ``/etc/netplan/01-netcfg.yaml``
  :emphasize-lines: 7-8,12-14

.. note::
  MAC is randomly generated on boot if not specified for the bridge network.

  Netplan seems funky in consistently applying changes. In most cases a reboot
  applies the config correctly. See :ref:`netplan` documentation.

.. code-block:: bash
  :caption: Apply the network configuration.

  netplan --debug apply
  networkctl status -a

* ``ip a`` should also display corresponding information.

Add Bridge to KVM Menu Drop Down
================================
By default if you add a bridge, you will have to select :cmdmenu:`Specify
Shared Device Name` then entering your bridge (typically ``br0``). This will add
the bridge directly to the dropdown menu instead.

Create an XML configuration file with your settings:

.. literalinclude:: source/br0.xml
  :caption: **0644 root root** ``/etc/libvertd/qemu/networks/br0.xml``

* See `network XML file format`_.
* See bug for creating `bridged netplan interfaces for libvirtd`_.

.. code-block:: bash
  :caption: Import the network into KVM, start it and set to autostart.

  virsh net-define /etc/libvertd/qemu/networks/br0.xml
  virsh net-start br0
  virsh net-autostart br0

.. code-block:: bash
  :caption: Show virtual networks, persistent should read **yes** for it to autostart.

  virsh net-list --all

Remove Pre-made NAT Virtual Bridge
==================================
This network is not needed if using bridging.

.. code-block:: bash
  :caption: Identify the NAT virtual network.

  virsh net-list -all

.. code-block:: bash
  :caption: Set network inactive, remove it and restart ``libvirtd``.

  virsh net-destroy br1
  virsh net-undefine br1
  service libvirtd restart

.. code-block:: bash
  :caption: Confirm the network no longer exists.

  virsh net-list --all

:ref:`service-ssh-ufw`.

Creating New VM
***************
Setup a standard VM to use the network bridge.

.. code-block:: bash
  :caption: Launch VM manager with X11 forwarding enabled.

  virt-manager

.. ggui::     Initial VM setup to use networking bridge
  :key_title: File --> New Virtual Machine
  :option:    ☑,
              ☑,
              ⋮ Network Selection
  :setting:   Select or create custom storage,
              Customize configuration before install,
              Virtual Network 'br0': bridge network
  :no_section:
  :no_caption:
  :no_launch:

  .. note::
    Only explicitly configured options are shown here. Disks should be created
    using the ``RAW`` format for performance.

  .. tip::
    You can manually specify bridge using the
    :cmdmenu:`Specify Shared Device Name` option and explicitly typing your
    bridge name if the Virtual Network bridge is not created.

.. ggui::     Add custom MAC
  :key_title: NIC
  :option:    MAC Address
  :setting:   {SET CUSTOM MAC ADDRESS}
  :no_section:
  :no_caption:
  :no_launch:

.. ggui::     Add virtio device
  :key_title: Add Hardware --> Network
  :option:    Network Source,
              MAC Address,
              Device Model
  :setting:   Virtual Network 'br0': bridge network,
              {CUSTOM MAC ADDRESS},
              virtio
  :no_section:
  :no_caption:
  :no_launch:

.. important::
  Be sure to :cmdmenu:`begin installation` for VM to be created.

Install Guest OS Tools
======================
These are only needed if you want to use a GUI in linux (required for windows).

.. code-block:: bash
  :caption: Linux

  apt install spice-vdagent xserver-org-video-qxl


Windows 10 requires signed virtio drivers. Drivers have been signed with the
`Red Hat vendor signature`_.

`Install signed virtio Guest Tools`_.

:download:`Latest Windows Spice Guest Tools <https://www.spice-space.org/download/windows/spice-guest-tools/spice-guest-tools-latest.exe>`

Convert XenServer XVA to KVM Image
**********************************
XenServer images cannot be directly imported, they must be converted first. VM's
should be exported *1 instance per XVA image* export.

.. code-block:: bash
  :caption: Install Build Tools

  apt install cmake gcc build-essentials libssl-dev

.. code-block:: bash
  :caption: Clone xva-img Tool & Build

  git clone https://github.com/eriklax/xva-img.git
  cd xva-img/
  cmake .
  sudo make install

.. code-block:: bash
  :caption: Extract VM from XVA Image

  mkdir my_vm
  tar -xvf my_vm.xva -C my_vm
  chmod -R 0755 my_vm
  xva-img -p disk-export my_vm/Ref\:{XXX}/ my_vm/ref-{XXX}.raw

* Disks have no permissions by default.
* There will be one ``Ref:XXX`` directory per disk. Generally, keep this named
  as the reference number for sanity, until you know what they are.
* Note: RAW is generally better for performance and long term performance.

.. code-block:: bash
  :caption: (Optional): Convert Disk Image to qcow2

  qemu-img convert -f raw -O qcow2 my_vm/ref-{XXX}.raw my_vm/ref-{XXX}.qcow2

* QCOW images are generally slower but allow for deduplication and consolidation
  of unused space.

Grab Metadata From VM
=====================
VM metadata (such as # of CPU's, memory, MAC) are not extracted by default. This
should be extracted for correct VM import into KVM.

.. code-block:: bash
  :caption: CPU

  grep -o '.\{0,40\}CPU.\{0,40\}' my_vm/ova.xml

.. code-block:: bash
  :caption: Memory

  grep -o '.\{0,40\}memory.\{0,40\}' my_vm/ova.xml

.. code-block:: bash
  :caption: MAC

  grep -o '.\{0,40\}MAC.\{0,40\}' my_vm/ova.xml

.. code-block:: bash
  :caption: Hostname

  grep -o '.\{0,40\}hostname.\{0,40\}' my_vm/ova.xml


Export KVM Image
****************
Useful for a configuration backup or moving to a new system.

.. code-block:: bash
  :caption: Dump the Current VM configuration

  virsh dumpxml {VM NAME} > {VM NAME}.xml

* Copy the XML file and associated disks to new location.

.. code-block:: bash
  :caption: Import VM

  virsh create {VM NAME}.xml

* Update disk location in XML file if location has changed.

Moving KVM Images
=================
KVM images are stored in two locations, configuration and disk images.

#. Ensure VM is stopped.
#. Move VM disk images to new location.
#. Update location information in XML file ``/etc/libvirtd/qemu/{VM}.xml``.
#. Restart service ``service libvirtd restart``.

Moving KVM Storage Pool
***********************
The default image storage location makes sense for linux (``/var``), but not for
servers centralizing data to storage pools.

By default, a single pool ``default`` is used for both VM images and ISO images.
Service requires a restart on changes.

.. code-block:: bash
  :caption: List all pools

  virsh pool-list
  virsh pool-info {POOL NAME}

.. code-block:: bash
  :caption: Delete a pool

  virsh pool-destroy {POOL}

* This will only remove the pool in KVM, not delete the underlying data.
* Alternatively, you can just delete the definition in ``/etc/libvirtd/storage``
  and corresponding autostart file if existing
  ``/etc/libvirtd/storage/autostart``.

.. code-block:: bash
  :caption: Move pool storage location while running

  virsh pool-edit {POOL}

* Update location for storage.
* Generally need to restart `libvirtd` for changes to apply.

.. code-block:: bash
  :caption: Dump Disk Image Pool

  virsh pool-dumpxml default > pool.xml

* Assumes pool name is ``default``.
* Make sure disk images are moved to new location.
* Update disk image locations in XML file.

.. code-block:: bash
  :caption: Destroy existing pool, import new pool from XML dump

  virsh pool-destory default
  virsh pool-create pool.xml

Mount RAW Disk Image
********************
This will enable mounting of a RAW disk image `outside of the VM`_.

.. code-block:: bash
  :caption: Ensure the RAW image is readable

  fdisk -l /var/lib/libvirt/images/{IMAGE}.RAW

* Determine **Sector Size**.
* Determine **Start Sector** for partition to mount.

.. important::
  The sector offset is:

  ``Sector Start * Sector Size = Sector Offset``

.. code-block:: bash
  :caption: Mount the partition as a block loop device

  losetup -r -o {SECTOR OFFSET} /dev/loop0 /var/lib/libvirt/{IMAGE}.RAW

* ``losetup -d /dev/loop0`` can be used to detach device later.
* ``losetup -l`` will show looped devices current mounted.

.. code-block:: bash
  :caption: Mount the Filesystem

  mount /dev/loop0 /mnt/image

Threadripper BSOD Windows 10 1803+
**********************************
Windows 10 versions 1803+ will `BSOD on installation`_ due to a unavaliable
`MSR`_ `registers`_ in KVM.

A `registers`_ patch has been created and will be avaliable in the **4.20+**
kernel release.

Temporary Workaround
====================
Emulating a ``Opteron Generation 5`` processer will prevent bluescreens from
happening. This will be an emulated CPU instead of passthrough.

Create a VM as normal and shutdown. Edit the VM definition to force emulate an
Opteron processor, and reload the definition.

.. literalinclude:: source/threadripper-vm.xml
  :caption: **0644 root root** ``/etc/libvirt/qemu/threadripper-vm.xml``

.. code-block:: bash
  :caption: Define the VM profile for KVM

  virsh define /etc/libvirt/qemu/threadripper-vm.xml

.. rubric:: References

#. `Virt Manager <https://virt-manager.org/download>`_
#. `KVM on Ubuntu 18.04 Server <https://www.linuxtechi.com/install-configure-kvm-ubuntu-18-04-server/>`_
#. `Alternative KVM on Ubuntu 18.04 Server <https://linuxconfig.org/install-and-set-up-kvm-on-ubuntu-18-04-bionic-beaver-linux>`_
#. `Netplan bridging <https://netplan.io/examples#configuring-network-bridges>`_
#. `Netplan example with bridge <https://askubuntu.com/questions/971126/17-10-netplan-config-with-bridge>`_
#. `Static IP address on Ubuntu 18.04 <https://websiteforstudents.com/configure-static-ip-addresses-on-ubuntu-18-04-beta/>`_
#. `Netplan Ubtuntu 18.04 Static IP <https://askubuntu.com/questions/1054350/netplan-bridge-for-kvm-on-ubuntu-server-18-04-with-static-ips>`_
#. `Netplan Bug <https://bugs.launchpad.net/netplan/+bug/1718607>`_
#. `Convert XenServer image to KVM <https://chariotsolutions.com/blog/post/convert-citrix-xenserver-xva-image-to-kvm/>`_
#. `QCOW2 versus RAW Performance <https://unix.stackexchange.com/questions/227792/what-are-tha-main-differences-between-an-iso-and-a-qco2-image>`_
#. `Moving KVM VMs to another Machine <https://askbot.fedoraproject.org/en/question/29704/how-do-i-move-a-virtual-machine-in-gnome-boxes-to-another-host/?answer=29839>`_
#. `Default libvirtd image locations <http://ask.xmodulo.com/change-default-location-libvirt-vm-images.html>`_
#. `Disabling virbr0 interface <https://www.cyberciti.biz/faq/linux-kvm-disable-virbr0-nat-interface/>`_
#. `libvirtd networking <https://wiki.libvirt.org/page/Networking>`_
#. `Spice Tools <https://www.spice-space.org/download.html>`_

.. _network XML file format: https://libvirt.org/formatnetwork.html
.. _bridged netplan interfaces for libvirtd: https://bugs.launchpad.net/ubuntu/+source/libvirt/+bug/1770345
.. _longstanding bug: https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093
.. _sysctl settings: https://serverfault.com/questions/431590/how-to-make-sysctl-network-bridge-settings-persist-after-a-reboot
.. _Red Hat vendor signature: https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/index.html
.. _Install signed virtio Guest Tools: https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/
.. _outside of the VM: http://whazenberg.blogspot.com/2012/12/mounting-raw-virtual-machine-disk-image.html
.. _BSOD on installation: https://bugzilla.redhat.com/show_bug.cgi?id=1593190
.. _registers: https://bugzilla.redhat.com/show_bug.cgi?id=1592276
.. _MSR: https://www.kernel.org/doc/Documentation/virtual/kvm/msr.txt
