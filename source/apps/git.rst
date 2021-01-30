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

Squash Commits to a Single Commit (`Rebase`_)
*********************************************
This will squash a series of commits into a single commit, which is useful to
cleanup multiple commits before pushing upstream.

.. code-block:: bash

  git rebase --interactive {COMMIT}

.. note::
  The ``COMMIT`` is the last commit that should be collapsed (e.g. rolled into a
  single commit).

  Editor will appear with rebase configuration. Generally use ``pick`` for the
  first commit and ``squash`` for the remaining commits.

.. code-block:: bash

  git rebase --continue

.. note::
  If done correctly, this will show all commit messages that were rolled up.
  Update as needed and commit as normal.

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

`Create a Branch`_
******************
Multiple branches can be made to focus changes on specific efforts. These are
cut from the current branch; most cases this should be ``master``.

.. code-block:: bash
  :caption: List, create, and move to new branch.

  git branch -a
  git branch -b {NEW BRANCH}
  git checkout {NEW BRANCH}

Use git normally.

Merging Branches
****************
Completed branches can be merged back into any branch, typically ``master``.

.. code-block:: bash
  :caption: List branches, switch to master, and merge.

  git branch -a
  git checkout master
  git merge {BRANCH} --no-ff

.. note::
  ``--no-ff`` retains all commit messages from the branch. Leave this off to
  squish the commit.

Deleting Branches
*****************
Git will throw an error if deleting a branch with commits that has not been
merged.

.. code-block:: bash
  :caption: Delete merged branch.

  git branch -a
  git branch -d {BRANCH}

List All Respositories for An Organization/User
***********************************************
Useful for determining if there are new repositories to sync.

.. code-block:: bash
  :caption: List all repositories for an organzation.

  curl "https://api.github.com/orgs/{ORGANIZATION NAME}/repos?per_page=1000&page=1" | jq -r '.[] | .name' | sort

.. code-block:: bash
  :caption: List all repositories for a user.

  curl "https://api.github.com/users/{USER}/repos?per_page=1000&page=1" | jq -r '.[] | .name' | sort

Pull `Latest Tarball Release`_ from Github
******************************************
Useful for projects that have periodic releases but are not in OS packages.

.. literalinclude:: source/update_latest_tarball
  :caption: **0755 user user** ``update_latest_tarball``

.. _Latest Tarball Release: https://gist.github.com/lukechilds/a83e1d7127b78fef38c2914c4ececc3c#gistcomment-2574561
.. _Rebase: https://www.internalpointers.com/post/squash-commits-into-one-git
.. _Create a Branch: https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/
