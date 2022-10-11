.. _doc-generation:

Document Generation
###################
Site documentation is generated using sphinx with a python virtual
environment and a custom makefile.

.. _sphinx-build:

Building
********
Environment automatically setup via the Makefile when building documentation,
for Debian and Manjaro platforms.

Documentation should be linkchecked for linkrot before building a new set of
docs to be published.

.. code-block::
  :caption: Setup sphinx build environment.

  make deps

.. code-block::
  :caption: One shot build and link verification.

  make clean docs linkcheck

.. code-block::
  :caption: Build docs, then verify links separately.

  make clean docs
  make linkcheck

.. code-block::
  :caption: Clean docs/ to upload only source changes.

  make head

Troubleshooting
***************

.. pull-quote::
  *master file [...] checkouts/latest/contents.rst not found*

Usually occurs when *no* sphinx modules are found in the python environment.
Ensure environment is properly and retry. See :ref:`venv-usage`.

Additionally, you may force specify an alternative index in ``conf.py``
using ``master_doc = 'index'``.

`Reference <https://github.com/readthedocs/readthedocs.org/issues/2569>`__

.. rubric:: References

#. `Video Tutorial on Sphinx <https://www.youtube.com/watch?v=hM4I58TA72g>`_
#. `Sphinx Getting Started Tutorial <https://sphinx-tutorial.readthedocs.io/start/>`_
#. `Ascii Art Figure Manual <https://launchpadlibrarian.net/41870218/aafigure.pdf>`_
#. `Ascii Art Figure Documentation <https://aafigure.readthedocs.io/en/latest/>`_
#. `RST Primer Tutorial <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer>`_
#. `RST Live Editor <http://rst.ninjs.org>`_
#. `Sphinx Live Editor <https://livesphinx.herokuapp.com/>`_
#. `Sphinx RST Cheetsheet <https://sphinx-tutorial.readthedocs.io/cheatsheet/>`_
#. `Sphinx RST Cheetsheet 2 <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_
#. `Sphinx roles and subsitutions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#substitutions>`_
#. `Sublime and Sphinx <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/reuse.html#use-a-substitution>`_
#. `nginx Sphinx documentation guidance <https://www.nginx.com/resources/wiki/contributing/writing_docs/>`_
#. `Sphinx Tools <https://www.writethedocs.org/guide/tools/testing/>`_

.. rubric:: Development References

#. `Sphinx Development <https://www.sphinx-doc.org/en/master/develop.html>`_
#. `Documented List <https://github.com/sphinx-contrib/documentedlist/blob/master/sphinxcontrib/documentedlist.py>`_
#. `RST Directive option conversion functions <https://docutils.sourceforge.io/docs/howto/rst-directives.html#option-conversion-functions>`_
#. `Sphinx roles <https://github.com/sphinx-doc/sphinx/blob/master/sphinx/roles.py#L382>`_
#. `docutils snippets <https://agateau.com/2015/docutils-snippets/>`_
#. `Unicode Python 3 escape sequences <https://www.quackit.com/python/reference/python_3_escape_sequences.cfm>`_
#. `Unicode triangular bullet <https://www.compart.com/en/unicode/U+2023>`_
#. `Using sphinx with github <https://www.docslikecode.com/articles/github-pages-python-sphinx/>`_
#. `Custom Sphinx Makefile <https://bitbucket.org/lbesson/web-sphinx/src/master/Makefile>`_
#. `Sphinx Docs <https://www.sphinx-doc.org/en/master/>`_
#. `Read the Docs Theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_
