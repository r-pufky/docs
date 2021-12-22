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

Force Pull from Master Repository
*********************************
Forces local repository to be in sync with master, discarding all local changes
and unpushed commits.

.. code-block:: bash

  git fetch --all
  git reset --hard origin/master

.. code-block:: bash
  :caption: Apply to a branch only

  git checkout {BRANCH}
  git fetch --all
  git branch {BRANCH}-backup
  git reset --hard origin/{BRANCH}

`Reference <https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files>`__

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
  git checkout -b {NEW BRANCH}

Use git normally.

.. _git-merging-branches:

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
  squish the commit (it may be helpful to get branch log for merge message
  ``git --no-pager log > /tmp/git.log``.

  You may reset the merge before committing with no data loss with
  ``get merge --abort``.

`Reference <https://nvie.com/posts/a-successful-git-branching-model/>`__

.. _git-deleting-branches:

Deleting Branches
*****************
Git will throw an error if deleting a branch with commits that has not been
merged.

.. code-block:: bash
  :caption: Delete merged branch.

  git branch -a
  git branch -d {BRANCH}

Create Worktree
***************
Allows the use of `multiple branches simultaneously`_.

.. code-block:: bash
  :caption: Create a new worktree from a branch

  git branch -a
  git checkout -b {NEW BRANCH}
  git checkout master
  git worktree add ../{WORKTREE NAME} {BRANCH}

Merge Worktree
**************
Works like normal branch merging. Execute merge from master worktree.

See :ref:`git-merging-branches`.

Removing Worktree
*****************
After the branch is merged worktree can be removed.

.. code-block:: bash
  :caption: Remove worktree.

  cd {MASTER WORKTREE}
  git worktree remove {WORKTREE}

Then delete branch as normal. See :ref:`git-deleting-branches`.

Migrate git stash to another machine
************************************
Export a stash as a patch to import in another git client.

.. code-block:: bash
  :caption: Export stash 0 to a patch.

  git stash show "stash@{0}" -p > changes.patch

.. code-block:: bash
  :caption: Import patch to client.

  git apply changes.patch

.. code-block:: bash
  :caption: Patch can be reverted if there are issues.

  git apply changes.patch --reverse

Repo git hooks
**************
Hooks are located in ``.git/hooks`` but are not versioned. This enables
`repository tracked hooks`_.

See ``.git/hooks`` for examples. Custom `pre-commit example`_. Hooks must have
exact names.

.. code-block:: bash
  :caption: Create repo hooks

  mkdir {REPO}/.githooks

.. code-block:: bash
  :caption: Set local gitconfig hookspath to custom location

  git config -f .gitconfig core.hooksPath .githooks

.. literalinclude:: source/pre-commit
  :caption: **0755 user user** ``.githooks/pre-commit``

.. code-block:: bash
  :caption: Use a Makefile or manually run on repo checkout to setup.

  git config --local include.path ../.gitconfig

.. note::
  Command executes from ``.git`` directory, hence going up a directory to read
  the config.

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
.. _multiple branches simultaneously: https://stackoverflow.com/questions/2048470/git-working-on-two-branches-simultaneously
.. _repository tracked hooks: https://pilot34.medium.com/store-your-git-hooks-in-a-repository-2de1d319848c
.. _pre-commit example: https://selivan.github.io/2017/04/08/ansible-check-on-commit-vault-files-are-encrypted.html
