.. _service-gitea-troubleshooting:

Troubleshooting
###############

Migration Fails with ``pq: duplicate key value violates unique constraint "{DB TABLE}_pkey"``
*********************************************************************************************
The initial migration ran past the default timeouts; or a previous
migration/mirror of the same name failed during import. The DB sequential ID's
have a new ID but not created, so creating a new key results in a `duplicate
unique key <https://github.com/go-gitea/gitea/issues/14692>`_.

.. code-block:: bash
  :caption: gitea.log

  2021/07/15 04:26:59 ...ules/task/migrate.go:67:func1() [E] DeleteRepository: repository does not exist [id: 705, uid: 33, owner_name: , name: ]
  2021/07/15 04:26:59 modules/task/task.go:54:handle() [E] Run task failed: pq: duplicate key value violates unique constraint "topic_pkey"

Increase default timeout of mirroring:

.. code-block:: yaml
  :caption: ``ansible_gitea_vars.yaml``

  gitea_repository_extra_config: |
    DEFAUlT = 360
    MIGRATE = 1200
    MIRROR  = 1200
    CLONE   = 300
    PULL    = 300
    GC      = 60

.. code-block:: bash
  :caption: Backup gitea and rebuild database tables.

  gitea dump -c /etc/gitea/gitea.ini -t /data/gitea/tmp/ -V
  gitea doctor recreate-table -c /etc/gitea/gitea.ini

Mirror Fails with 'could not read Username'
*******************************************
The source repository is no longer public or has been deleted. Disable sync by
setting Migration Interval to ``0``.

.. code-block:: bash
  :caption: Example log when source repo is deleted/private.

  2021/07/15 03:53:42 ...ces/mirror/mirror.go:242:runSync() [E] Failed to update mirror repository &{272 10 {USER} <nil> {REPO} {REPO} Mirror of https://github.com/{USER}/{REPO}.  2 https://github.com/{USER}/{REPO} master 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 true false false true <nil> 0 map[] map[] [] <nil> false 0 <nil> false 0 <nil> 35674663 <nil> <nil> false false [] default  1582936274 1573978478}:
  Stdout: Fetching origin

  Stderr: fatal: could not read Username for 'https://github.com': terminal prompts disabled
  error: Could not fetch origin

  Err: <nil>
