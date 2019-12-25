.. _apps-vim:

VIM
###
VI Improved.

See `vim adventure`_ for a game to learn vim, and `stackoverflow most useful vim
shortcuts`_.

Commands
********

Quit with Error
===============
Useful for aborting mid-commit without submitting.

.. code-block:: vim

  :cq

Insert Unicode Characters
=========================
.. code-block:: vim

  i
  ctrl+v
  u####

Increment/Decrement A Number
============================
.. code-block:: vim

  ctrl+A  # Increment
  ctrl+X  # Decrement

Visual Mode
===========
.. code-block:: vim

  v       # character
  V       # line
  ctrl+v  # block

Indentation
===========
.. code-block:: vim

  v
  >
  <

Goto Last Edit
==============
.. code-block:: vim

  gi

Delete to End of Line
=====================
.. code-block:: vim

  d$  # Delete only
  c$  # Delete and enter insert mode

Macros
======
.. code-block:: vim

  qq   # start recording
  {PERFORM ACTIONS}
  q    # stop recording
  @q   # repeat recorded actions (first time)
  @@   # report recorded actions (every time after)
  20@@ # repeat 20 times

Troublshooting
**************

VIM 'Frozen'
============
Generally happens when stopping terminal output with control floww.

.. code-block:: vim

  ctrl+s  # stops terminal output (causes freeze) (XON)
  ctrl+q  # starts terminal output (XOFF)

Customize VIM
*************
Displayed without comments / unchanged lines.

.. literalinclude:: source/.vimrc
  :caption: **0644 user user** ``~/.vimrc``
  :linenos:

.. _vim adventure: https://vim-adventures.com/
.. _stackoverflow most useful vim shortcuts: https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim/1220118#1220118