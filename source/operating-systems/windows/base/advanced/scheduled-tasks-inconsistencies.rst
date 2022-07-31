.. _wbase-scheduled-tasks-inconsistencies:

Scheduled Tasks Inconsistencies
###############################
Scheduled Tasks are inconsistently applied at login triggers, and do not cover
cases where long-running process like gpg-agent may hang. The remedy for this
is to trigger the Scheduled Task on an Event. Event Triggers cannot be created
using the current powershell cmdlet -- and can only be created interactively or
via a com object.

This will run through configuring a gpg-agent to refresh on screen unlock
(including initial login) using both GUI and using a powershell script options,
and assumes GPG agents have been added to the user's PATH environment variable
already.

`Reference <https://superuser.com/questions/1214736/windows-10-scheduled-tasks-with-workstation-lock-unlock-not-being-triggered/1217125>`__

`Reference <https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/new-scheduledtasktrigger?view=win10-ps>`__

`Reference <https://docs.microsoft.com/en-us/windows/win32/com/com-objects-and-interfaces>`__

.. _scheduled-tasks-logon-logoff:

Enable Logon/Logoff Events
**************************
Logon/Logoff events are not configured to log by default. When enabled,
successful unlock events will have an ID of **4801**, and event login failures
will have an ID of **4800**. The unlock event will trigger at screen unlock as
well as logging into the machine.

.. gpo::   Enable logon logoff events policy
  :path:   Computer Configuration -->
           Windows Settings -->
           Security Settings -->
           Advanced Audit Policy Configuration -->
           System Audit Policies - Local Group Policy Object -->
           Logon/Logoff -->
           Audit Other Login/Logoff Events
  :value0: ☑, Configure the following audit events
  :value1: ☑, {SUCCESS}
  :value2: ☑, {FAILURE}
  :update: 2021-02-19

.. _scheduled-tasks-event-trigger:

Manually Adding Event Triggered Scheduled Task
**********************************************
Setup triggered events to refresh GPG agent on screen unlocks.

See :ref:`scheduled-tasks-powershell-create-event` for a powershell script that
does this for you.

.. dropdown:: Manaually add event triggered scheduled task
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gui::   Manually add general section schedule
    :label:  Task Scheduler
    :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:   Action --> Create Task --> General
    :value0:          Name, GpgAgentRefreshUnlock
    :value1:   Description, Restarts GPG agent on windows unlock
    :value2:         Check, Run only when user is logged on
    :value3: Configure for, Windows 10
    :value4:             ☑, Hidden
    :update: 2021-02-19

  .. gui::   Manually add triggers section schedule
    :label:  Task Scheduler
    :path:   Triggers --> New
    :value0: Begin the task, On an event
    :value1:          Check, Basic
    :value2:            Log, Security
    :value3:         Source, Microsoft Windows security auditing
    :value4:       Event ID, 4801
    :value5:              ☑, Hidden
    :update: 2021-02-19

  .. gui::   Manually add actions section gpg kill schedule
    :label:  Task Scheduler
    :path:   Actions --> New
    :value0:                   Action, Start a program
    :value1:           Program/Script, gpgconf
    :value2: Add arguments (optional), --kill gpg-agent
    :update: 2021-02-19

  .. gui::   Manually add actions section gpg agent schedule
    :label:  Task Scheduler
    :path:   Actions --> New
    :value0:                   Action, Start a program
    :value1:           Program/Script, gpg-connect-agent
    :value2: Add arguments (optional), /bye
    :update: 2021-02-19

    .. note::
      ``gpgconf --kill gpg-agent`` action should always be executed before
      restarting the connect agent.

  .. gui::   Manually add conditions section schedule
    :label:  Task Scheduler
    :path:   Conditions
    :value0: *, ☐
    :update: 2021-02-19

  .. gui::   Manually add settings section schedule
    :label:  Task Scheduler
    :path:   Settings
    :value0:       Allow task to be run on demand, ☑
    :value1: Stop the task if it runs longer than, ☑
    :value2: Stop the task if it runs longer than, 3 days
    :value3:                        All Remaining, ☐
    :update: 2021-02-19

This can be verified to work by restarting your machine or killing the current
agent with ``gpgconf --kill gpg-agent`` and locking/unlocking your screen then
attempting to use Putty. It is registered in :cmdmenu:`Task Scheduler Library`
as *GPGAgentRefreshUnlock*.

You may noticed occasionsally that command windows pop-up while the scheduled
task is executing. If this should be completely hidden, see
:ref:`hiding-command-windows`.

.. _scheduled-tasks-powershell-create-event:

Powershell to Create Event Triggered Scheduled Task
***************************************************
Use a Windows COM object to directly interact with Task Scheduler to create
the Event Trigger and the task. A password is required when adding the task.

This re-creates the same task as manually specified above.

.. literalinclude:: source/gpg-agent-refresh-unlock.ps1
  :language: powershell
  :emphasize-lines: 35,46
  :linenos:

:download:`gpg-unlock.ps1 <source/gpg-agent-refresh-unlock.ps1>`

* Execution Policy: **Unrestricted** (see: :ref:`wbase-execution-policy`).
* This is registered in :cmdmenu:`Task Scheduler Library` as
  *GPGAgentRefreshUnlock*.
* The ``Subscription`` query on line 35 is extracted from the manually created
  scheduled task, instead of manually generating it. Just
  :cmdmenu:`{RMB} --> export` and look in the XML file for ``Subscription``.

This can be verified to work by restarting your machine or killing the current
agent with ``gpgconf --kill gpg-agent`` and locking/unlocking your screen then
attempting to use Putty. It is registered in :cmdmenu:`Task Scheduler Library`
as ``GPGAgentUnlockRestart``.

You may noticed occasionsally that *command windows* pop-up while the scheduled
task is executing. If this should be completely hidden, see
:ref:`hiding-command-windows`.

`Reference <https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-objects>`__

`Reference <https://docs.microsoft.com/en-us/archive/blogs/wincat/trigger-a-powershell-script-from-a-windows-event>`__

(optional) Prompt on Terminal, Instead of Window
************************************************
You may directly query for a password to use in the terminal if a pop-up
authentication prompt is too much. Just insert this and replace the secure
string marshaller on *line 46* ``RegisterTaskDefinition`` with ``$password``;
though this will leave a unencrypted password in memory. Remember to overwrite
or delete this.

.. code-block:: powershell

  $password = Read-Host -assecurestring "Please enter your password"
  $password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

.. _hiding-command-windows:

Hiding Command Windows
**********************
Windows may appear during the execution of actions involving ``cmd``. However
the built in method to hide windows -- ``start /b`` -- will fail as this is not
the first thing that executed in the scheduled task (it runs a command shell,
then executes start), or fails with the error:

.. pull-quote::
  *The operator or administrator has refused the request.*

The solution to this is to create a small visual basic wrapper that calls your
command with no window defined. The command will execute in the wrapper, thus
hiding the window creation.

It is **absolutely imperative** that this script be **signed and trusted** for
use, and that unsigned vbs scripts are **NOT** trusted. Otherwise you've just
created a way for someone to potentially execute anything they want as *you*
whenever you login. If you don't know what the above means, then **don't do
this**.

.. code-block:: vbscript
  :caption: ``quiet_launcher.vbs``

  CreateObject("Wscript.Shell").Run "" & WScript.Arguments(0) & "", 0, False

.. gui::   Use wrapper script for GPG conf task
  :label:  Task Scheduler
  :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
  :path:   GPGAgentRefreshUnlock --> Actions --> Edit --> Start a Program
  :value0: Program/Script, quiet_launcher.vbs
  :value1:  Add arguments, gpgconf --kill gpg-agent
  :update: 2021-02-19

.. gui::   Use wrapper script for GPG connect task
  :label:  Task Scheduler
  :nav:    ⌘ --> Task Scheduler --> Task Scheduler Library
  :path:   GPGAgentRefreshUnlock --> actions --> edit --> Start a program
  :value0: Program/Script, quiet_launcher.vbs
  :value1:  Add arguments, gpg-connect-agent /bye
  :update: 2021-02-19

`Reference <https://ss64.com/nt/start.html>`__

Demonstration of Scheduled Task at Login Failure
************************************************
As GPG agent can hangup occasionally, only restarting on initial login will
produce problems with long-running systems, or surface scheduling errors within
Task Scheduler itself. This task will work, but will sporadically fail. This is
only kept as an example of the failure condition and should not be used.

.. code-block:: powershell
  :caption: This task will eventually fail on long running systems (powershell
            as admin).

  $job = Register-ScheduledJob `
     -Name GpgAgent `
     -ScriptBlock { gpg-connect-agent.exe /bye } `
     -Trigger (New-JobTrigger -AtLogOn -User $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)) `
     -ScheduledJobOption (New-ScheduledJobOption -StartIfOnBattery -ContinueIfGoingOnBattery) `
     -RunNow

  # Change principal to run only on interactive logon instead of S4U (Service for user login).
  $principal = New-ScheduledTaskPrincipal -LogonType Interactive -UserId $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
  Set-ScheduledTask -TaskPath \Microsoft\Windows\PowerShell\ScheduledJobs\ -TaskName $job.Name -Principal $principal

.. note::
  This job will appear in :cmdmenu:`Task Scheduler` as *GpgAgent* under
  :cmdmenu:`Task Scheduler Library --> Microsoft --> Windows --> PowerShell --> ScheduledJobs`

`Reference <https://www.kaylyn.ink/journal/windows-using-gpg-for-ssh-authentication-and-git/>`__

.. rubric:: References

#. `Create schedule task with event log trigger <https://stackoverflow.com/questions/42801733/creating-a-scheduled-task-which-uses-a-specific-event-log-entry-as-a-trigger>`_
#. `Task scheduler VB scripting <https://community.spiceworks.com/topic/1030490-task-scheduler-vb-script-help?page=1>`_
#. `Powershell password prompt without readhost <https://social.technet.microsoft.com/Forums/office/en-US/f90bed75-475e-4f5f-94eb-60197efda6c6/prompt-for-password-without-using-getcredential-or-readhost-assecurestring-but-not-display-text?forum=winserverpowershell>`_
