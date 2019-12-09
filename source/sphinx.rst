.. _doc-generation:

Document Generation
###################
Site documentation is generated using `sphinx`_ using a python virtual
environment and a custom makefile.

Building
********
Using an `activated`_ virtual environment from the ``git/services/doc``
location.

.. code-block::

  make clean docs

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
    :caption: **0600 {USER}:{USER}** ``~/.bashrc``

    export PIP_REQUIRE_VIRTUALENV=true

.. _activated:

#. Activate virutal environment for use.

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
    mv /tmp/sphinx_rtd_theme/sphinx_rtd_them doc/sphinx/_themes

#. Use custom ``conf.py`` file for site customization.

  .. literalinclude:: ../sphinx/conf.py
    :caption: **0640 {USER}:{USER}** ``doc/sphinx/conf.py``
    :emphasize-lines: 20-22,31-32,35-36,46,52-59,64

  .. todo::
    Until ``pip install sphinx-rtd-theme`` is fixed without error.

#. Use custom ``Makefile`` for building documentation.

  .. literalinclude:: ../Makefile
    :caption: **0640 {USER}:{USER}** ``doc/Makefile``

  .. note::
    This will use the *data/dev* directory as the source, *doc/sphinx* as
    the configuration and */tmp/services/docs* as output directory. A new
    make command ``make clean docs`` will automatically build the documentation
    and remove / update *static/dev/files/d/etc/data/nginx/docs* with the
    latest documentation from the soruce tree.

  See `sphinx makefile`_ for other custom examples.

.. rubric:: References

#. `Video Tutorial on Sphinx <https://www.youtube.com/watch?v=hM4I58TA72g>`_
#. `Sphinx Getting Started Tutorial <https://sphinx-tutorial.readthedocs.io/start/>`_
#. `Ascii Art Figure Manual <https://launchpadlibrarian.net/41870218/aafigure.pdf>`_
#. `Ascii Art Figure Documentation <https://aafigure.readthedocs.io/en/latest/>`_
#. `publishing sphinx docs on github <https://daler.github.io/sphinxdoc-test/includeme.html>`_

#. `RST Primer Tutorial <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer>`_
#. `RST Live Editor <http://rst.ninjs.org>`_
#. `Sphinx Live Editor <https://livesphinx.herokuapp.com/>`_
#. `Sphinx RST Cheetsheet <https://sphinx-tutorial.readthedocs.io/cheatsheet/>`_
#. `Sphinx RST Cheetsheet 2 <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_
#. `Sphinx roles and subsitutions <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#substitutions>`_
#. `Sublime and Sphinx <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/reuse.html#use-a-substitution>`_
#. `nginx Sphinx documentation guidance <https://www.nginx.com/resources/wiki/contributing/writing_docs/>`_

.. rubric:: Development References

#. `Sphinx Development <https://www.sphinx-doc.org/en/master/develop.html>`_
#. `Documented List <https://github.com/sphinx-contrib/documentedlist/blob/master/sphinxcontrib/documentedlist.py>`_
#. `RST Directive option conversion functions <http://docutils.sourceforge.net/docs/howto/rst-directives.html#option-conversion-functions>`_
#. `Sphinx roles <https://github.com/sphinx-doc/sphinx/blob/master/sphinx/roles.py#L382>`_
#. `docutils snippets <https://agateau.com/2015/docutils-snippets/>`_
#. `Unicode Python 3 escape sequences <https://www.quackit.com/python/reference/python_3_escape_sequences.cfm>`_
#. `Unicode triangular bullet <https://www.compart.com/en/unicode/U+2023>`_
#. `Using sphinx with github <https://daler.github.io/sphinxdoc-test/includeme.html>`_

.. _sphinx: http://www.sphinx-doc.org
.. _python pip and virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
.. _sphinx makefile: https://bitbucket.org/lbesson/web-sphinx/src/master/Makefile
.. _contents.rst issue: https://github.com/readthedocs/readthedocs.org/issues/2569
.. _Read the Docs: https://sphinx-rtd-theme.readthedocs.io/en/stable/
