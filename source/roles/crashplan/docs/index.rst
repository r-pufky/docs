.. _service-crashplan:

Crashplan Pro
#############
Crashplan Pro (For Small Business) is now the only consumer level option for
crashplan.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration
   troubleshooting

.. role:: crashplan
  :galaxy:       https://galaxy.ansible.com/r_pufky/crashplan
  :source:       https://github.com/r-pufky/ansible_crashplan
  :service_doc:  https://support.code42.com/Small_Business/Get_Started/CrashPlan_for_Small_Business_requirements
  :update:       2022-10-08
  :open:

  Pay attention to basic configuration steps to correctly adopt existing backup
  sets.

  * If using LXC containers, you must run as privileged (``unprivileged: 0``)
    or use ``idmap`` to map all permissions to the container; otherwise mounted
    data will appear empty.
  * Run Crashplan as **root** to be able to read/backup all files.
  * Mount filesystems to backup **read-only** to prevent data loss.
  * Mount filesystems to backup under ``/``, such as ``/data``. This will allow
    for container migration to other machines without destroying backup sets,
    and keep it idempotent from the container OS.
  * Increase :ref:`service-crashplan-troubleshooting-inotify` to prevent
    warnings.
  * See minimum requirements in :ref:`service-crashplan-defaults`.

  .. warning::
    Read :ref:`service-crashplan-basic-configuration-backup-set` to adopt
    existing backup sets without losing data.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

.. _service-crashplan-defaults:

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
