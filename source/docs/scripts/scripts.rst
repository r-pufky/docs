.. _scripts:

Scripts
#######
One off scripting commands and small QOL improvement scripts not needing their
own repository.

.. code-block:: bash
  :caption: Bash script to require a specific keypress or die.

  echo 'This will cut a production release by overwriting prod with dev.'
  read -n 1 -p 'Press Y to continue, any other key to abort: ' READ_CONTINUE

  if [ "${READ_CONTINUE}" != 'Y' ]; then
    echo -e '\nAborting.'
    exit 1
  fi

:download:`fflength <source/fflength>` determines the length of a video file.

.. literalinclude:: source/fflength
  :caption: **0700 user user** ``fflength``
  :linenos:

:download:`playon-to-mkv <source/playon-to-mkv>` converts playon videos to MKV
containers.

.. literalinclude:: source/playon-to-mkv
  :caption: **0700 user user** ``playon-to-mkv``
  :linenos: