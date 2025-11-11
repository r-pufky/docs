# Troubleshooting

## Reduce Repository Size (Prune)
Prune repository and reduce size or remove sensitive material.

!!! warning
    All branches will need to be force pushed to clear entire history. Any
    checked out versions will need to be force synced.

``` bash
# Clone target repo to a clean state.
git clone {REPO}

# Note all tags and commits.
git tag --list

# Note origin URL.
git config --get remote.origin.url

# Remove all files with path molecule/files.
git filter-repo --invert-paths --path-glob 'molecule/files'

# Re-add origin origin URL.
git remote add origin {ORIGIN}

# Retag all tags with new commit ID's (from above).
git tag -d {TAG}
git tag {TAG} {COMMIT}

# Force push all commits and tags.
git push --all --force
git push --tags --force
```

Reference:

* https://stackoverflow.com/questions/2116778/reduce-git-repository-size
* https://github.com/newren/git-filter-repo/blob/main/Documentation/converting-from-bfg-repo-cleaner.md#cheat-sheet-conversion-of-examples-from-bfg
* https://github.com/newren/git-filter-repo
