# GIT
GIT version management snippets.

## Global Settings
Rebasing when pulling makes the branch history cleaner, avoiding pull merge
commits. Prune on fetch automatically clean Git objects in your repository
locally whenever you fetch changes from remote, minimizes the number of
branches on your local machine. Highlight moved code block sections.

```bash
git config --global pull.rebase true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
```

Reference

* https://spin.atomicobject.com/2020/05/05/git-configurations-default

## Use GPG keys for Commit Signing
``` bash
# Get keys to use
gpg --list-keys

git config --global commit.gpgsign true
git config --global gpg.program /usr/bin/gpg
git config --global user.signingkey {KEY}

# Manually sign without settings above.
git tag -s {TAG}{COMMIT}
```

Reference:

* https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits
* https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

## Revert Changes and Keep Commit History
``` bash
git revert --no-edit {LAST GOOD COMMIT}..{LAST BAD COMMIT}
```

## Force Repository to Previous Commit
!!! danger
    ``` bash
    git reset --hard {COMMIT ID}
    git push --force origin master
    ```

    This is data destructive. Ensure any files are cleaned up before
    committing.

    Currently checked out versions of this repository will break.

## Force Pull from Master Repository
Forces local repository to be in sync with master, discarding all local changes
and un-pushed commits.

``` bash
git fetch --all
git reset --hard origin/master

# Apply to a branch only
git checkout {BRANCH}
git fetch --all
git branch {BRANCH}-backup
git reset --hard origin/{BRANCH}
```

Reference:

* https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files

## Revert Entire Directory to HEAD
``` bash
git checkout -- {DIR}  # {DIR}/.. target everything in directory.
git clean -fd {DIR}  # {DIR}/.. target everything in directory.
```

## Add Tag to Previous Commit
``` bash
git pull --tags
git tag {TAG} {COMMIT}
git push --tags
```

## Squash Commits to a Single Commit (Rebase)
This will squash a series of commits into a single commit, which is useful to
cleanup multiple commits before pushing upstream.


!!! note
    ``` bash
    git rebase --interactive {COMMIT}
    ```

    The **COMMIT** is the last commit that should be collapsed (e.g. rolled
    into a single commit).

    Editor will appear with rebase configuration. Generally use **pick** for the
    first commit and **squash** for the remaining commits.

!!! note
    ``` bash
    git rebase --continue
    ```

    If done correctly, this will show all commit messages that were rolled up.
    Update as needed and commit as normal.

Reference:

* https://www.internalpointers.com/post/squash-commits-into-one-git

## Modify Specific Historical Commit
!!! warning
    This will re-write commit history from the changed commit. Tags and
    releases will need to be deleted and re-created. Existing clones will
    break. Be careful.

``` bash
git rebase --interactive '{COMMIT}^'  # Rebase one commit **before** change.
```

!!! note
    Set **edit** for the desired commit; save and exit. Make desired changes.

``` bash
git commit --all --amend --no-edit  # Finish rebasing to HEAD
git rebase --continue

# Reset affected tags
git tag -l
git rev-list -n 1 {TAG}
git tag -d {TAG}
git push --delete origin {TAG}
git tag {TAG} {NEW COMMIT HASH}
git push --tags
```

!!! warning
    Ensure affected releases, tags are removed before pushing the changed repo.

Reference:

* https://stackoverflow.com/questions/1186535/how-to-modify-a-specified-commit

## Remove Tracked Files without Deleting Them
``` bash
git rm --cached {FILE TO REMOVE FROM COMMIT}  # Single file.
git rm --cached {FILE1} {FILEN}  # Multiple files.
git rm -r --cached {DIR}  # All contents of a directory.
```

## Highlight Changes in Long Single Lines
``` bash
git diff --word-diff {FILE} {FILE}
```

## Migrate git stash to another machine
Export a stash as a patch to import in another git client.

``` bash
git stash show "stash@{0}" -p > changes.patch  # Export stash 0 to a patch.
git apply changes.patch  # Import patch to client.
git apply changes.patch --reverse  # Patch can be reverted if there are issues.
```

## Repo git hooks
Hooks are located in **.git/hooks** but are not versioned. This enables
repository tracked hooks. See **.git/hooks** for examples. Hooks must have
exact names.

Example **.githooks** (1)
{ .annotate }

1. 0644 {USER}:{USER}
  ``` bash
  #!/usr/bin/env bash
  #
  # Called by "git commit" with no arguments.  The hook should
  # exit with non-zero status after issuing an appropriate message if
  # it wants to stop the commit. See .git/hooks for examples.

  # Unset variables produce errors
  set -u

  if git rev-parse --verify HEAD >/dev/null 2>&1
  then
  	against=HEAD
  else
  	# Initial commit: diff against an empty tree object
  	against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
  fi

  # Redirect output to stderr.
  exec 1>&2

  EXIT_STATUS=0

  # Check that vault files are encrypted.
  # read: -r do not allow backslashes to escape characters; -d delimiter
  while IFS= read -r -d $'\0' file; do
  	[[ "$file" != *.vault &&
  		 "$file" != *.vault.yml &&
  		 "$file" != *vault ]] && continue
  	# cut gets symbols 1-2
  	file_status=$(git status --porcelain -- "$file" 2>&1 | cut -c1-2)
  	file_status_index=${file_status:0:1}
  	file_status_worktree=${file_status:1:1}
  	[[ "$file_status_worktree" != ' ' ]] && {
  		echo "ERROR: *.vault file is modified in worktree but not added to the index: $file"
  		echo "Can not check if it is properly encrypted. Use git add or git stash to fix this."
  		EXIT_STATUS=1
  	}
  	# check is neither required nor possible for deleted files
  	[[ "$file_status_index" = 'D' ]] && continue
  	head -1 "$file" | grep --quiet '^\$ANSIBLE_VAULT;' || {
  		echo "ERROR: non-encrypted *.vault file: $file"
  		EXIT_STATUS=1
  	}
  done < <(git diff --cached --name-only -z "$against")

  exit $EXIT_STATUS
  ```

``` bash
mkdir {REPO}/.githooks
# Set local gitconfig hookspath to custom location.
git config -f .gitconfig core.hooksPath .githooks

.. literalinclude:: source/pre-commit
  :caption: **0755 {USER}:{USER}** **.githooks/pre-commit``

# Use a Makefile or manually run on repo checkout to setup.
git config --local include.path ../.gitconfig
```

!!! note
    Command executes from **.git** directory, hence going up a directory to
    read the config.

Reference:

* https://pilot34.medium.com/store-your-git-hooks-in-a-repository-2de1d319848c
* https://selivan.github.io/2017/04/08/ansible-check-on-commit-vault-files-are-encrypted.html

## List All Repositories for An Organization/User
Useful for determining if there are new repositories to sync.

``` bash
# List all repositories for an organzation.
curl "https://api.github.com/orgs/{ORGANIZATION NAME}/repos?per_page=1000&page=1" | jq -r '.[] | .name' | sort

# List all repositories for a user.
curl "https://api.github.com/users/{USER}/repos?per_page=1000&page=1" | jq -r '.[] | .name' | sort
```
