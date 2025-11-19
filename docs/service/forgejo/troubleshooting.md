# Troubleshooting


## Migration Fails
The initial migration ran past the default timeouts; or a previous migration or
mirror of the same name failed during import.

!!! danger ""
    pq: duplicate key value violates unique constraint "{DB TABLE}_pkey"

The DB sequential IDs have a new ID but not created, so creating a new key
results in a [duplicate unique key][a].

``` ini
[git.timeout]
DEFAUlT = 360
MIGRATE = 1200
MIRROR = 1200
CLONE = 300
PULL = 300
GC = 60
```

Backup Forgejo and rebuild database tables.
``` bash
forgejo dump -c /etc/forgejo/forgejo.ini -t /data/forgejo/tmp/ -V
forgejo doctor recreate-table -c /etc/forgejo/forgejo.ini
```

## Mirror Fails with could not read Username
The source repository is no longer public or has been deleted.

!!! danger ""
  [E] Failed to update mirror repository &{272 10 {USER} <nil> {REPO} {REPO} Mirror of https://github.com/{USER}/{REPO}.  2 https://github.com/{USER}/{REPO} master 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 true false false true <nil> 0 map[] map[] [] <nil> false 0 <nil> false 0 <nil> 35674663 <nil> <nil> false false [] default  1582936274 1573978478}:
  Stdout: Fetching origin

  Stderr: fatal: could not read Username for 'https://github.com': terminal prompts disabled
  error: Could not fetch origin

  Err: <nil>

Disable sync by setting Migration Interval to **0**.

[a]: https://github.com/go-gitea/gitea/issues/14692