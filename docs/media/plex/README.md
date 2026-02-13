# Plex
Plex Media Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.media.plex][a].

!!! tip
    * The UID/GID should be set to a user/group that have access to your media.
      All media clients should run under the same user to run correctly.
    * Map your media directly to where it was before to prevent needing to
      modify any libraries. This should be **read-only**.


## New Setup
A new plex install (or one requiring a new access token after revocation)
requires the initial manual setup process to be run locally. Use a SSH tunnel
to access the server-side configuration page.

``` bash
ssh -L 32400:localhost:32400 {plex_host}
```

Then connect to http://localhost:32400/web and obtain token:

1. Select media libraries to use.
2. Sign-in on server: upper right ➔ sign-in.
3. Select server and claim: claim now ➔ claim server.
4. Set [PlexOnlineToken](config.md#plexonlinetoken).

## Enable Secure Server Connection
1. Ensure **32400** is forwarded from the router.
2. Enable [DNS Rebinding][b] on router.

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/media/docs
[b]: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections
