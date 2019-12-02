.. _style-guide:

Style Guide
###########

Use this: https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html#headings

sphinx / rst styling notes.

Callouts (admonitions):
* attention
* caution
* danger
* error
* hint
* important
* note
* tip
* warning
* pull-quote --- quote block, generally unformatted
* highlights -- highlight block, generally unformatted
* epigraph  -- epigraph block, generally unformatted
* todo
* seealso

don't use single line, to break reading as per rendered output

.. note::
  This is a note.

references:
lower-with-dashes. Don't prepend 'ref-' to the definition.

sub-bullet point lists


#. somthing (no highlights)

    * requires a space. Insert begin/trailing vertical white space.

#. something (highlights)
    * No beginning vertical white space.
    * Above line is required to be a single line.

#. some other stuff.

Always prefer ' to " for quotes.

code blocks
***********
* File list: no period.
* File list with extra context text: trailing periods.
* Text only: trailing period.

.. code-block:: python
  :caption: title above block can be wrapped.
  :emphasize-lines: 1
  :linenos:

  # some code here. if longer that a few lines, use ``literalinclude``.
  print('helloworld')

file listing:

statements require periods.
no periods for file lists.
literal includes follow the same rule.
captions may contain double backticks for paths.

.. code-block::
  :caption: **0644 root root** ``/etc/initramfs/modules``
  :lineno-start: 12
  :emphasize-lines: 2

  ...
  k10temp

.. literalinclude:: operating-systems/ubuntu/source/sshd_config
  :caption: **0644 root root** ``/etc/ssh/sshd_config``
  :linenos:
  :emphasize-lines: 2,3
  :start-after: 2
  :end-before: 25

* Always inline all headers, and settings.
* always add TOC section to bottom below links, hidden.

For remote modification of files (e.g. a router) where there is a local file and
a remote file of the same name, specific the remote target host as well.

.. code-block::
  :caption: **0644 root root** ``/etc/initramfs/modules`` (EdgeOS CLI).
  :lineno-start: 12
  :emphasize-lines: 2

  ...
  k10temp


For sections where dynamic deletions are needed for a file and cannot be
pre-determined in documentation or a static file.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/hosts`` EdgeOS CLI.

  #Delete hosts which are no longer used and reboot the router.

GUI

Use :cmdmenu:`action` for all actions
chain with '-->'

cmdmenu:

#. GUI Options should appear as cased in UI.
#. **Any** user typed actions should be all lowercase.

* one component depth (e.g. Application Name)
* Mouse action / shortcut.
* cmdmenu in lists: no trailing period, unless combine with text.



:cmdmenu:`System`

   * Host Name: {ROUTER HOSTNAME}
   * Domain Name: {YOUR DOMAIN}
   * :cmdmenu:`Management Settings > SSH Server`
      * ☑ Enable
         * Port: {SSH Port}
      * ☐ Ubnt Discovery

see: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html

Config Tables:

* Only use custom configuration tables for generic configurations on systems
  (e.g. regedit, unifi controllers) where *repeated, distinct* uses occur.
* Applications and one-offs use a static inline table for configuration.

gpolicy:
title: lowercase if using no_section. Otherwise follow section formatting.
keys: follow actual key cap formatting.

Sections
* title case
* links should be set as `see xyz` if cannot be put in section title.

ms_tables can have all metadata wrapped.



https://unicode-table.com/en


testing documentation links
``make linkcheck``
``make clean html linkcheck``



Sphinx linkcheck setup
https://www.writethedocs.org/guide/tools/testing/




Include source files:

Create a ``source`` directory for each section.



VARS:

{USERNAME}
{PASSWORD}
{HOSTNAME}


references


.. rubric:: References

#. `Create schedule task with event log trigger <https://stackoverflow.com/questions/42801733/creating-a-scheduled-task-which-uses-a-specific-event-log-entry-as-a-trigger>`_
#. `Task scheduler VB scripting <https://community.spiceworks.com/topic/1030490-task-scheduler-vb-script-help?page=1>`_
#. `Powershell password prompt without readhost <https://social.technet.microsoft.com/Forums/office/en-US/f90bed75-475e-4f5f-94eb-60197efda6c6/prompt-for-password-without-using-getcredential-or-readhost-assecurestring-but-not-display-text?forum=winserverpowershell>`_
