.. _apps-python-venv:

Python Virtual Environments
###########################
Create python environments for specific app/tooling needs. Used commonly to
prevent scripts/apps from munging systemwide Python installation.

Creating Environment
********************
See `python pip and virtual environment`_ for reference material.

.. code-block::
  :caption: Install pip and virtual environment packages.

  apt install python3-pip python3-venv

.. code-block::
  :caption: Create a virtual environment.

  test -d {ENV DIR} || python3 -m venv {ENV DIR}

.. note::
  All `other virtual environment commands`_ are deprecated now.

.. code-block::
  :caption: Update ``~/.bashrc`` to require virtual environments for ``pip``.

  export PIP_REQUIRE_VIRTUALENV=true

.. _venv-usage:

Using Virtual Environments
**************************

.. code-block::
  :caption: Activate virtual environment for use.

  . {ENV DIR}/bin/activate

.. code-block::
  :caption: Deactivate the environment to return the normal system environment.

  deactivate

Export/Import Environments
**************************
Environments may be exported for easy configuration with services and scripts.

.. code-block::
  :caption: Export current environment.

  . {ENV DIR}/bin/activate
  python3 -m pip freeze > {ENV CONFIG}

.. code-block::
  :caption: Install a specific environment.

  . {ENV DIR}/bin/activate
  python3 -m pip install --requirement {ENV CONFIG}

Updating Environments
=====================
Update environment and re-export.

.. code-block::
  :caption: Update environment.

  . {ENV DIR}/bin/activate
  python3 -m pip install --upgrade --requirement {ENV CONFIG}
  python3 -m pip freeze > {ENV CONFIG}

.. rubric:: References

.. _python pip and virtual environment: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
.. _other virtual environment commands: https://docs.python.org/3/library/venv.html#venv-def
