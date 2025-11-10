# BASH
Bourne Again Shell snippets.

## Require PIP to use Virtual Environment

**~/.bashrc**
``` bash
export PIP_REQUIRE_VIRTUALENV=true
```

Create a virtual environment
``` bash
python3 -m venv /var/venv/{ENV}
source /var/venv/{ENV}/bin/activate  # 'deactivate' will exit.
```

## Rename All File Extensions to Lowercase
``` bash
find . -type d -execdir rename 's/(\.[A-Z]+$)/lc($1)/ge' *.*[A-Z]* \;

# Alternatively use rename binary.
rename 'y/A-Z/a-z/' *
```

Reference:

* https://askubuntu.com/questions/546426/how-to-rename-file-extension-to-lowercase

## Find Binary in All Files
``` bash
# Sed for a signal file.
sed -n 's/.*[,"\[>[:space:]]\(.*\.exe\).*/\1/p'

# For all files.
find . -name "*.txt" -exec sed -n 's/.*[+,"\[>[:space:]]\(.*\.exe\).*/\1/p' {} \; > result-list

# Using grep is faster.
grep -iroh "\(.*\.exe\)" . | tee result-list
```

## Prompt to require a specific keypress or die
``` bash
echo 'This will cut a production release by overwriting prod with dev.'
read -n 1 -p 'Press Y to continue, any other key to abort: ' READ_CONTINUE

if [ "${READ_CONTINUE}" != 'Y' ]; then
  echo -e '\nAborting.'
  exit 1
fi
