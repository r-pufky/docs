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


## [Rename All File Extensions to Lowercase][a]
``` bash
find . -type d -execdir rename 's/(\.[A-Z]+$)/lc($1)/ge' *.*[A-Z]* \;

# Alternatively use rename binary.
rename 'y/A-Z/a-z/' *
```


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
```


## Last CLI Argument
Use last argument in current command.

``` bash
!$
$_

# Alternatively 'alt + .' will copy the string.
```


## Switch to a User with no login shell
``` bash
su - -s /bin/bash {USER}
```


## [Parse INI value from file][b]
``` bash
#!/bin/sh
if [ "$1" != "${1#*[0-9].[0-9]}" ]; then
  echo IPv4
elif [ "$1" != "${1#*:[0-9a-fA-F]}" ]; then
  echo IPv6
else
  echo "Unrecognized IP format '$1'"
fi
```

[a]: https://askubuntu.com/questions/546426/how-to-rename-file-extension-to-lowercase
[b]: https://stackoverflow.com/questions/6318809/how-do-i-grab-an-ini-value-within-a-shell-script#6318837
