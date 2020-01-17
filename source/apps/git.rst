.. _git:

GIT
###
GIT version management snippets.

.. _revert-with-history:

Revert Changes and Keep Commit History
**************************************
.. code-block:: bash

  git revert --no-edit {LAST GOOD COMMIT}..{LAST BAD COMMIT}

Force Repository to Previous Commit
***********************************
Should use :ref:`revert-with-history`.

.. code-block:: bash

  git reset --hard {COMMIT ID}
  git push --force origin master

.. danger::
  This is data destructive. Ensure any files are cleaned up before committing.

  Currently checked out versions of this repository will break.

Revert Entire Directory to HEAD
*******************************
.. code-block:: bash

  git checkout -- {DIR}
  git clean -fd {DIR}

.. note::
  ``{DIR}/..`` can be used to target all files and directories within that
  directory.

Add Tag to Previous Commit
**************************
.. code-block:: bash

  git pull --tags
  git tag {TAG} {COMMIT}
  git push --tags

Squash Commits to a Single Commit (Rebase)
******************************************
This will squash a series of commits into a single commit, which is useful to
cleanup multiple commits before pushing upstream.

.. code-block:: bash

  git rebase -i {COMMIT}

.. note::
  The ``COMMIT`` is the last commit that should be collapsed (e.g. rolled into a
  single commit).

Remove Tracked Files without Deleting Them
******************************************
.. code-block:: bash
  :caption: Single file.

  git rm --cached {FILE TO REMOVE FROM COMMIT}

.. code-block:: bash
  :caption: Multiple files.

  git rm --cached {FILE1} {FILEN}

.. code-block:: bash
  :caption: All contents of a directory.

  git rm -r --cached {DIR}

Pull `Latest Tarball Release`_ from Github
******************************************
Useful for projects that have periodic releases but are not in OS packages.

.. literalinclude:: source/update_latest_tarball
  :caption: **0755 user user** ``update_latest_tarball``

.. _Latest Tarball Release: https://gist.github.com/lukechilds/a83e1d7127b78fef38c2914c4ececc3c#gistcomment-2574561