.. _sphinx-style-guide:

`Sphinx Style Guide`_
#####################
General style-guide for sphinx.

* 80 character limit, exception for code blocks.
* Always verify links (:ref:`sphinx-build`) before uploading
  changes.

  .. note::
    All issues must be addressed. Do not use ``!http`` in source docs.

    ``sphinx/conf.py`` contains specific exceptions for linkchecking.

* No submission of docs with breakages or warnings (red text).
* Remain consistent. See existing documentation for examples.

Common Replacements
*******************
Use ``{CAPS WITH SPACE}``.

Standardized replacements used:

* ``{USER}`` - user account.
* ``{PASS}`` - account password.
* ``{EMAIL}`` - user email address.
* ``{HOST}`` - Host DNS name.
* ``{IP}`` - Host IP.
* Windows drives are **lowercased** ``c:\``.

.. note::
  All can be modified with additional context as needed. E.g. ``{WEBHOOK
  EMAIL}``.

Callouts (`admonitions`_)
*************************

* ``attention``
* ``caution``
* ``danger``
* ``error``
* ``hint``
* ``important``
* ``note``
* ``tip``
* ``warning``
* ``pull-quote`` -- quote block, generally unformatted.
* ``highlights`` -- highlight block, generally unformatted.
* ``epigraph`` -- epigraph block, generally unformatted.
* ``todo``
* ``seealso``

Only use multi-line admonitions.

References
**********
``lower-with-dashes``. Do not prepend ``ref-`` to the definition.

.. code-block:: RST
  :caption: sub-bullet point lists

  #. Somthing (no highlights)

      * requires a space. Insert begin/trailing vertical white space.

  #. Something (highlights)
      * No beginning vertical white space.
      * Above line is required to be a single line.

  #. Some other stuff.

  Always prefer ' to " for quotes.

code blocks
***********
* File list: no period.
* File list with extra context text: trailing periods.
* Text only: trailing period.

.. code-block:: RST
  :caption: Example code-block.

  .. code-block:: python
    :caption: title above block can be wrapped.
    :emphasize-lines: 1
    :linenos:

    # some code here. if longer that a few lines, use ``literalinclude``.
    print('helloworld')

For remote modification of files (e.g. a router) where there is a local file and
a remote file of the same name, specific the remote target host as well.

.. code-block:: RST
  :caption: Remote modification template.

  .. code-block::
    :caption: **0644 root root** ``/etc/initramfs/modules`` (EdgeOS CLI).
    :lineno-start: 12
    :emphasize-lines: 2

    ...
    k10temp

For sections where dynamic deletions are needed for a file and cannot be
pre-determined in documentation or a static file.

.. code-block:: RST
  :caption: dyanmic deletions template.

  .. code-block:: bash
    :caption: **0644 root root** ``/etc/hosts`` EdgeOS CLI.

    #Delete hosts which are no longer used and reboot the router.

File Listings
*************
* Statements require periods.
* No periods for file lists.
* Literal includes follow the same rule.
* Captions may contain double backticks for paths.
* Always use local ``source`` directories for downloads / file listings. See
  existing examples.

.. code-block:: RST
  :caption: code-block template for showing file content.

  .. code-block::
    :caption: **0644 root root** ``/etc/initramfs/modules``
    :lineno-start: 12
    :emphasize-lines: 2

    ...
    k10temp

.. code-block:: RST
  :caption: literalinclude  template for showing file content.

  .. literalinclude:: source/sshd_config
    :caption: **0644 root root** ``/etc/ssh/sshd_config``
    :linenos:
    :emphasize-lines: 2,3
    :lines: 2-25

* Always inline all headers, and settings.
* always add TOC section to bottom below links, hidden.

GUI
***
Use ``cmdmenu`` directive for all actions. Do not use ``guilabel``.

* GUI Options should appear as cased in UI.
* **Any** user typed actions should be all lowercase.
* one component depth (e.g. Application Name).
* Mouse action / shortcut.
* cmdmenu in lists: no trailing period, unless combine with text.
* Windows shortcut to different settings:
  :cmdmenu:`⌘ + r --> ms-settings:{LABEL}` See `run reference`_.

.. code-block:: RST
  :caption: cmdmenu example.

  :cmdmenu:`System --> Preferences`

     * Host Name: {ROUTER HOSTNAME}
     * Domain Name: {YOUR DOMAIN}
     * :cmdmenu:`Management Settings > SSH Server`
        * ☑ Enable
           * Port: {SSH Port}
        * ☐ Ubnt Discovery

see `roles`_.

Config Tables Extension
***********************
* Only use custom configuration tables for generic configurations on systems
  (e.g. regedit, unifi controllers) where *repeated, distinct* uses occur.
* Applications and one-offs use generic ConfigTables for configuration.
* Documentation for ConfigTable is contained within Python module.

TOC
***
Main ``index.rst`` used to land in areas, and sub-TOC's used to generate TOC for
those sub areas.

* See ``source/index.rst`` for main TOC.
* See ``source/networking/ubiquiti/exmaple-vlan-network/index.rst`` for sub TOC.

.. _roles: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html
.. _admonitions: http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions
.. _Sphinx Style Guide: https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html#headings
.. _run reference: https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app