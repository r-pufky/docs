.. _bash:

BASH
####
Bourne Again Shell snippets.

Rename All `File Extensions to Lowercase`_
******************************************
.. code-block:: bash

  find . -type d -execdir rename 's/(\.[A-Z]+$)/lc($1)/ge' *.*[A-Z]* \;

.. code-block:: bash
  :caption: Alternatively use rename binary.

  rename 'y/A-Z/a-z/' *

Find Binary in All Files
************************
.. code-block:: bash
  :caption: Sed for a signal file.

  sed -n 's/.*[,"\[>[:space:]]\(.*\.exe\).*/\1/p'

.. code-block:: bash
  :caption: For all files.

  find . -name "*.txt" -exec sed -n 's/.*[+,"\[>[:space:]]\(.*\.exe\).*/\1/p' {} \; > result-list

.. code-block:: bash
  :caption: Using grep is faster.

  grep -iroh "\(.*\.exe\)" . | tee result-list

.. _File Extensions to Lowercase: https://askubuntu.com/questions/546426/how-to-rename-file-extension-to-lowercase