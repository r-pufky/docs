.. _doc-generation:

Document Generation
###################
Site documentation is generated using `sphinx`_ using a python virtual
environment and a custom makefile.

.. _sphinx-build:

Building
********
Using an `activated`_ virtual environment for the ``git/docs``
location.

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

.. note::
  *master file [...] checkouts/latest/contents.rst not found*

  Usually occurs when *no* sphinx modules are found in the python environment.
  Ensure environment is `activated`_ properly and retry.

  Additionally, you may force specify an alternative index in ``conf.py``
  using ``master_doc = 'index'``. See `contents.rst issue`_.

Installation
************
See `python pip and virtual environment`_ for reference material.

#. Install pip and virtual environment packages.

  .. code-block::

    apt install python3-pip python3-venv

#. Create virtual environment for *sphinx*.

  .. code-block::

    mkdir ~/.python-env
    cd !$
    python3 -m venv sphinx

#. Update ``.bashrc`` to force require virtual environments for ``pip``.

  .. code-block::
    :caption: **0600 user user** ``~/.bashrc``

    export PIP_REQUIRE_VIRTUALENV=true

.. _activated:

#. Activate virtual environment for use.

  .. code-block::

    . ~/.python-env/sphinx/bin/activate

  .. note::
    Environment may be deactivated at any time by issuing ``deactivate``
    command.

#. Install sphinx and sphinx plugins.

  .. code-block::

    pip install Sphinx sphinxcontrib-aafig2 sphinxcontrib-applehelp sphinxcontrib-devhelp sphinxcontrib-htmlhelp sphinxcontrib-jsmath sphinxcontrib-qthelp sphinxcontrib-serializinghtml

#. Install custom theme `Read the Docs`_ for sphinx.

  .. code-block::

    git clone https://github.com/readthedocs/sphinx_rtd_theme /tmp
    mv /tmp/sphinx_rtd_theme/sphinx_rtd_them docs/sphinx/_themes

#. Use custom ``conf.py`` file for site customization.

  .. literalinclude:: ../sphinx/conf.py
    :caption: **0640 user user** ``docs/sphinx/conf.py``
    :emphasize-lines: 20-22,30-33,37,50,53,60,69-71,73,75,77-78

  .. todo::
    Until ``pip install sphinx-rtd-theme`` is fixed without error.

#. Use custom ``Makefile`` for building documentation.

  .. literalinclude:: ../Makefile
    :caption: **0640 user user** ``docs/Makefile``

  .. note::
    This will use:

    * ``docs/source`` directory as the source.
    * ``docs/sphinx`` as the configuration.
    * ``/tmp/docs`` as build directory.
    * ``docs/docs`` is the output directory.

    A new make command ``make clean docs`` will automatically build the
    documentation and remove / update ``docs/docs`` with the latest
    documentation from the soruce tree.

  See `sphinx makefile`_ for other custom examples.

.. _sphinx-build-link-checking:

Link Checking
*************
Documentation can be automatically link checked:

.. code-block:: bash
  :caption: Verify documentation links work.

  make linkcheck
  make clean docs linkcheck

.. rubric:: References

#. `Video Tutorial on Sphinx <https://www.youtube.com/watch?v=hM4I58TA72g>`_
#. `Sphinx Getting Started Tutorial <https://sphinx-tutorial.readthedocs.io/start/>`_
#. `Ascii Art Figure Manual <https://launchpadlibrarian.net/41870218/aafigure.pdf>`_
#. `Ascii Art Figure Documentation <https://aafigure.readthedocs.io/en/latest/>`_
#. `RST Primer Tutorial <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer>`_
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

.. _sphinx: http://www.sphinx-doc.org/en/master/
.. _python pip and virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
.. _sphinx makefile: https://bitbucket.org/lbesson/web-sphinx/src/master/Makefile
.. _contents.rst issue: https://github.com/readthedocs/readthedocs.org/issues/2569
.. _Read the Docs: https://sphinx-rtd-theme.readthedocs.io/en/stable/
