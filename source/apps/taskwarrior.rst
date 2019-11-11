.. _apps-taskwarrior:

Taskwarrior Configuration
#########################

Installation
************
.. code-block:: bash
  :caption: Install base packages and setup environment redirection

  apt install taskwarrior timewarrior libjson-perl

Add environment variables to bash.

.. code-block:: bash
  :caption: **0644 user user** ``~/.bashrc``

  export TASKRC=~/task/.taskrc
  export TIMEWARRIORDB=~/task/timew
  alias taskopen='taskopen -c ~/task/taskopen/.taskopenrc'

.. code-block:: bash
  :caption: Create a default taskwarrior configuration

  task

.. code-block:: bash
  :caption: Install taskopen

  git clone https://github.com/ValiValpas/taskopen
  cd taskopen
  make PREFIX=/usr install
  mkdir -p ~/task/taskopen ~/task/tasknotes
  taskopen -c ~/.task/taskopen/.taskopenrc

.. code-block:: bash
  :caption: Copy timewarrior hook to auto track tasks

  cp /usr/share/doc/timewarrior/ext/on-modify.timewarrior ~/task/hooks
  chmod +x ~/task/hooks/on-modify.timewarrior

.. code-block:: bash
  :caption: Verify it loads, should see Hooks Enabled

  task diagnostics

  Hooks
       System: Enabled
     Location: /home/{USER}/task/hooks
       Active: on-modify.timewarrior (executable)
     Inactive:

Customize Taskwarrior
=====================
Displayed without comments / unchanged lines.

.. literalinclude:: source/.taskrc
  :caption: **0644 user user** ~/task/.taskrc
  :linenos:

Customized Timewarrior
======================
Displayed without comments / unchanged lines.

.. literalinclude:: source/timewarrior.cfg
  :caption: **0644 user user** ~/task/timew/timewarrior.cfg
  :linenos:

Customize Taskopen
==================
Displayed without comments / unchanged lines.

.. literalinclude:: source/.taskopenrc
  :caption: **0644 user user** ~/task/taskopen/.taskopenrc
  :linenos:
  :emphasize-lines: 2,4,9,12,16

.. rubric:: References

#. `Taskwarrior Examples <https://taskwarrior.org/docs/examples.html>`_
#. `Taskwarrior Commands <https://taskwarrior.org/docs/commands/modify.html>`_
#. `Manage tasks with Taskwarrior <https://youtu.be/zl68asL9jZA>`_
#. `Taskwarrior Tutorials (some takeaways, generally crappy) <https://youtu.be/3iyaS5WwcuQ>`_
