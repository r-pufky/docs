# Branches
Multiple branches can be made to focus changes on specific efforts. These are
cut from the current branch; most cases this should be **master**.


## [Create a Branch][a]
``` bash
# List, create, and move to new branch.
git branch -a
git checkout -b {NEW BRANCH}
```
Use git normally.


## Merging Branches
Completed branches can be merged back into any branch, typically **master**.

``` bash
# List branches, switch to master, and merge.
git branch -a
git checkout master
git merge {BRANCH} --no-ff
```

!!! note
    **--no-ff** retains all [commit messages from the branch][b]. Leave this
    off to squish the commit (it may be helpful to get branch log for merge
    message **git --no-pager log > /tmp/git.log**).

    You may reset the merge before committing with no data loss with
    **get merge --abort*.


## Deleting Branches
!!! tip
    Git will throw an error if deleting a branch with commits that has not been
    merged.

``` bash
# Delete merged branch.
git branch -a
git branch -d {BRANCH}
```

## [Create Worktree][c]
Allows the use of multiple branches simultaneously.

``` bash
# Create a new worktree from a branch
git branch -a
git checkout -b {NEW BRANCH}
git checkout master
git worktree add ../{WORKTREE NAME} {BRANCH}
```

### Merge Worktree
Works like normal branch merging. Execute merge from master worktree.

### Removing Worktree
After the branch is merged worktree can be removed.

``` bash
# Remove worktree.
cd {MASTER WORKTREE}
git worktree remove {WORKTREE}
```

Then delete branch as normal. [See Deleting Branches](#deleting-branches).

[a]: https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/
[b]: https://nvie.com/posts/a-successful-git-branching-model
[c]: https://stackoverflow.com/questions/2048470/git-working-on-two-branches-simultaneously
