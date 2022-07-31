.. _manjaro-kde-apps-nodejs:

`NodeJS <https://nodejs.org/en/>`__
###################################
Node.js is a javascript runtime that runs on Chrome's V8 javascript engine. It
is used for front and backend tooling. Dependency management is a nightmare.

The default manjaro install installs for the ``root`` user. This shows how to
install on a per-user basis, supporting multiple versions **without** requiring
root.

.. code-block:: bash
  :caption: Install node version manager.

  pacman -Syu nvm

.. code-block:: bash
  :caption: Add nvm to your shell profile to enable nvm commands.

  echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc

.. code-block:: bash
  :caption: restart shell, confirm working, and install current lts release.

  nvm --version
  nvm install --lts

`Reference <https://dev.to/lobo_tuerto/how-to-install-nodejs-in-manjaro-linux--5ha4>`__