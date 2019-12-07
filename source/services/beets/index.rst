.. _service-beets:

`beets.io`_ Media Server
########################
Music organizer.

See `beets.io Docker and Documentation`_.

.. gport:: Ports (beets.io)
  :port:     8337
  :protocol: TCP
  :type:     Exposed
  :purpose:  Web GUI frontend for playback.
  :no_key_title:
  :no_caption:
  :no_launch:

.. gflocation:: Important File Locations (beets.io)
  :file:    /config.yaml,
            /library.sqlite3.db
  :purpose: beets.io configuration.,
            beets.io library metadata database.
  :no_key_title:
  :no_caption:
  :no_launch:

Docker Creation
***************
* The UID/GID should be set to a user/group that have access to your media.
* Map your media directly to where it was before on the docker container to
  prevent needing to modify any libraries.

:download:`Example config.yaml <source/config.yaml>`

.. code-block:: yaml
  :caption: Docker Compose

  beets:
    image: linuxserver/beets:latest
    restart: unless-stopped
    environment:
      - PGID=1001
      - PUID=1001
      - TZ=America/Los_Angeles
    volumes:
      - /data/downloads/complete/music:/data/downloads/complete/music
      - /data/media/music:/data/media/music
      - /data/services/beets:/config
      - /etc/localtime:/etc/localtime:ro

* Proxy will forward traffic to the container, so no ports need to be opened.

Reverse Proxy Setup
*******************
Allows you to isolate your containers as well as wrap connections in SSL. See
:ref:`service-nginx` for more details. See
:ref:`service-nginx-base-proxy-control` for basic proxy configuration.

.. code-block:: yaml
  :caption: **0644 user user** ``beets/config.yaml``

  web:
    host: 0.0.0.0
    port: 8337
    reverse_proxy: yes

Using Subdomains
================
.. literalinclude:: source/subdomain.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Using Subpaths
==============
.. literalinclude:: source/subpath.conf
  :caption: **0644 root root** ``nginx/conf.d/reverse-proxy.conf``

Managing Library
****************
.. code-block:: bash
  :caption: Beets CLI interface

  sudo docker exec -it -u abc beets bash

`Importing Music`_
==================
.. code-block:: bash
  :caption: Import using default options from config.

  beet import /path/to/music

.. warning::
  Pay attention to **unmatched** tracks, these will **not** be imported if the
  current selection is choosen.

.. note::
  It may *freeze* importing. Generally this is fingerprinting music and
  updating metadata with correct info/art. Let this run. Will be longer for
  larger number of imported items.

  Chroma (fingerprinting), musicbrainz, and other background tasks will
  be executed simultaneously in the background for the given directory. This
  should be kept small, such as a single album or artist. This is slow.

* All albums need to be decided on before import starts. Keep import small.
* Generally, go through potential matches. Any non-exact matches are usually
  fairly in accurate.
* Use ``i`` for musicbrainz ID if the top guesses are not accurate. This is
  helpful to force a specific ID.
* **Duplicate** albums that need to be disambiguated should be imported as
  normal. When prompted ``This album is already in the library``, select the
  **K** eep option. This will use ``aunique`` to disambiguate the albums.

Re-importing Music
==================
Music may be re-imported if already existing. just use the library path.

.. code-block:: bash
  :caption: Reimport an existing album.

  beet import -L /data/media/music/existing/artist/album

.. note::
  If you have ``incremental`` enabled, you may have to remove the metadata
  from the library before importing.

Adding to an Existing Album
===========================
Adding a track to an existing album is a bit confusing, especially if it is a
compilation/various artist album.

#. Make sure to select the metadata tracks that match the album.

  .. code-block:: bash
    :caption: Determine the existing album metadata.

    beet info {QUERY}

#. Select the correct album on the import prompt.
#. Beets will ask to merge, list a summary of existing and new tracks; open
   an additional shell, find the track locally and ensure there's no collisions
   with the merge.
#. Select the correct album on the merged import prompt.

Fixing 'featuring' Tracks
=========================
The plugin ``ftintitle`` generally takes care of this, but there are certain
cases where this is not the case. This addresses these cases.

`ftintitle works`_ by using the ``albumartist`` as the *real* artist and
``artist`` field for featured artists ('feat.' artists).

.. code-block:: bash
  :caption: Set the albumartist to the appropriate artist.

  beet modify albumartist='single artist' {QUERY}

.. note::
  You should use ``list`` to find appropriate data to match.

.. code-block:: bash
  :caption: Set artist to appropriate 'feat.' text (if needed).

  beet modify artist='single artist feat. other artist' {QUERY}

.. note::
  Generally this is setup correctly in musicbrainz.

.. code-block:: bash
  :caption: Re-run ``ftintitle``.

  beet -v ftintitle {QUERY}

.. note::
  This should pickup your artist changes and act appropriately.

Manually Moving Files
=====================
Sometimes if an import half-way through, some files will be imported, others
will not.

.. code-block:: bash
  :caption: Execute moves based on existing music metadata.

  beet move

.. note::
  Use ``-p`` to test before applying.

Update the Library
==================
This will update the database with any new file metadata, as well as organize
existing files according to metadata:

.. code-block:: bash

  beet update

.. note::
  Use ``-p`` to test before applying.

Changing Music Metadata
=======================
Useful for fixing bad imports, or for getting music to re-import correctly.

.. code-block:: bash

  beet modify [attribute]=[value] {QUERY}

.. note::
  Ensure to use ``list`` to make sure you are only modifying the tracks that
  you want.

Removing Tracks
===============
This is useful for re-importing tracks, as well as permenant deletion.

.. code-block:: bash

  beet remove {QUERY}

.. note::
  This will remove file metadata from library (does not delete files).

  Use ``-d`` to actually delete files.

Querying Music
**************
By default queries all fields for matches. Can use ``path`` specifier to
specify an exact file, as well as attribute matching. See `additional querying
options`_.

Query Matching Fields
=====================
.. code-block:: bash

  beet list {FIELD}:{VALUE}

Match Exact String
==================
.. code-block:: bash

  beet list 'some exact title'

Find Empty Fields
=================
.. code-block:: bash
  :caption: Finding empty fields (uses regex matching).

  beet list [field]::^$

Match All Fields
================
.. code-block:: bash

  beet list ":^$"

Path Matching
=============
.. code-block:: bash
  :caption: Path matching (useful for files with exact same metadata).

  beet list path:/my/music/directory/or/file

.. note::
  Path is implied with ``/``.

  .. code-block:: bash

    beet list /my/music/directory/or/file

  Works as well.

Importing Gotchas
*****************
Sometimes beets just doesn't import correctly.

Modify Pre-import Data
======================
Use ``avprobe`` and `mid3v2`_ modify pre-import metadata. For cases where
pre-manipulation of track data will help for a better match, or fixing a bad
match detection.

.. code-block:: bash
  :caption: List current metadata.

  mid3v2 -l {FILE}

.. code-block:: bash
  :caption: Update metadata.

  mid3v2 -t 'new title' {FILE}
  mid3v2 -T '1/5' {FILE}
  mid3v2 -A 'new album' {FILE}
  mid3v2 -a 'new artist' {FILE}

.. note::
  In practice, usually just the track and title need to be changed. See man page
  for all options.

Get File Info/Track Length/Bitrate
==================================
.. code-block:: bash
  :caption: Useful for matching duplicates in beets, or track lengths to albums.

  avprobe {FILE}

Force Import a Track as a Single Specific Track
===============================================
This will resolve tracks that are consistently mis-identified even after munging
the metadata.

Find the recording ID for musicbrains (the individual track ID on musicbrainz).

.. code-block:: bash
  :caption: Import singleton track.

  bash beet import -s /import/album/track.mp3

.. note::
  * **S** option to import singleton.
  * **I** to select a *recording ID*.

Re-import the now correct track into the existing album. Find the album ID from
musicbrains or existing album in beets.

.. code-block:: bash
  :caption: Re-import now correct track.

  beets beet import /data/media/music/Non-Albums/imported-track-from-above.mp3

.. note::
  * **I** to select a *release ID*.
  * **M** merge tracks into album.

.. rubric:: References

#. `beets.io reverse proxy <https://github.com/beetbox/beets/blob/master/docs/plugins/web.rst>`_

.. _beets.io Docker and Documentation: https://hub.docker.com/r/linuxserver/beets/
.. _beets.io: https://beets.readthedocs.io/en/latest/reference/index.html
.. _ftintitle works: https://github.com/beetbox/beets/issues/1766
.. _additional querying options: https://beets.readthedocs.io/en/latest/reference/query.html
.. _Importing Music: http://beets.readthedocs.io/en/latest/guides/tagger.html
.. _mid3v2: https://unix.stackexchange.com/questions/4961/which-mp3-tagging-tool-for-linux