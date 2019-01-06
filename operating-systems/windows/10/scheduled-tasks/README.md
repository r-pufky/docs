
Scheduled Tasks
---------------
Scheduled Tasks are inconsistently applied and therefore will run into issues if
 you depend on the scheduled tasks to [trigger at login][1] or may potentially
die after the initial login occurred. The remedy for this is to trigger the
Scheduled Task on an Event trigger. However, Event Triggers cannot be created
using the [current powershell cmdlet][2] -- they can only be created
interactively or via a [com object][3].

This will run through configuring a gpg-agent to refresh on screen unlock (
include initial login) manually and using a powershell script, and assumes GPG
agents have been added to the user's PATH environment variable already.

1. [Manually Adding Event Triggered Scheduled Task](#manually-adding-event-triggered-scheduled-task)
1. [Powershell to Create Event Triggered Scheduled Task](#powershell-to-create-event-triggered-scheduled-task)
1. [Hiding Command Windows](#hiding-command-windows)
1. [Demonstration of Scheduled Task At Login](#demonstration-of-scheduled-task-at-login)

Enable Logon/Logoff Events
--------------------------
Logon/Logoff events are not configured to log by default. When enabled,
successful unlock events will have an ID of `4801`, and event login failures
will have an ID of `4800`. The unlock event will trigger at screen unlock as
well as logging into the machine.

```win + r > gpedit.msc```
> Key: Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration > System Audit Policies - Local Group Policy Object > Logon/Logoff

> Policy: Audit Other Login/Logoff Events > Success = Enabled

> Policy: Audit Other Login/Logoff Events > Failure = Enabled.

Manually Adding Event Triggered Scheduled Task
----------------------------------------------
```start > Task Scheduler > Task Scheduler Library```
* `Action > Create Task`

General
* Name: `GpgAgentRefreshUnlock`.
* Description: `Restarts GPG agent on windows unlock`.
* Check: `Run only when user is logged on`.
* Configure for: `Windows 10`.
* Check: `Hidden`.

Triggers
* `New`.
* Being the task: `On an event`.
* Check: `Basic`.
* Log: `Security`.
* Source: `Microsoft Windows security auditing`.
* Event ID: `4801`.
* Check: `Enabled`.

Actions
1. `New`
  * Action: `Start a program`.
  * Program/Script: `gpgconf`.
  * Add arguments (optional): `--kill gpg-agent`.
2. `New`
  * Action: `Start a program`.
  * Program/Script: `gpg-connect-agent`.
  * Add arguments (optional): `/bye`.
* Ensure order is correct.

Conditions
* Uncheck: `ALL`.

Settings
* Check: `Allow task to be run on demand`.
* Check: `Stop the task if it runs longer than` `3 days`.
* Uncheck: `All Remaining`.

This can be verified to work by restarting your machine or killing the current
agent with `gpgconf --kill gpg-agent` and locking/unlocking your screen then
attempting to use Putty. It is registered in `Task Scheduler Library` as
`GPGAgentRefreshUnlock`.

You may noticed occasionsally that _command windows_ pop-up while the scheduled
task is executing. If this should be completely hidden, see [Hiding Command
Windows](#hiding-command-windows).

Powershell to Create Event Triggered Scheduled Task
---------------------------------------------------
Use a [Windows COM object][4] to directly interact with Task Scheduler to create
the Event Trigger and the task. A password is required when adding the task.

This re-creates the same task as manually specified above.

Powershell as Admin ([script here][8])
```powershell
$Hostname = $Env:computername

$Service = new-object -ComObject ("Schedule.Service")
$Service.Connect($Hostname)
$TaskFolder = $Service.GetFolder("\")
$TaskDefinition = $Service.NewTask(0)
$RegistrationInfo = $TaskDefinition.RegistrationInfo
$RegistrationInfo.Description = 'Restarts GPG agent on windows unlock'
$RegistrationInfo.Author = $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)

$Principal = $TaskDefinition.Principal
$Principal.LogonType = 3
$Principal.UserId = $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)

$Settings = $taskDefinition.Settings
$Settings.Enabled = $true
$Settings.Hidden = $true
$Settings.Compatibility = 2
$Settings.MultipleInstances = 2
$Settings.DisallowStartIfOnBatteries = $false
$Settings.StopIfGoingOnBatteries = $false
$Settings.AllowHardTerminate = $false
$Settings.StartWhenAvailable = $false
$Settings.RunOnlyIfNetworkAvailable = $false
$Settings.AllowDemandStart = $true
$Settings.RunOnlyIfIdle = $false
$Settings.DisallowStartOnRemoteAppSession = $false
$Settings.UseUnifiedSchedulingEngine = $true
$Settings.WakeToRun = $false
$Settings.ExecutionTimeLimit = 'PT72H'
$Settings.Priority = 7

$Triggers = $TaskDefinition.Triggers
$Trigger = $Triggers.Create(0)
$Trigger.Subscription = "<QueryList><Query Id='0' Path='Security'><Select Path='Security'>*[System[Provider[@Name='Microsoft-Windows-Security-Auditing'] and EventID=4801]]</Select></Query></QueryList>"
$Trigger.Enabled = $true

$GpgKillAction = $TaskDefinition.Actions.Create(0)
$GpgKillAction.Path = 'gpgconf'
$GpgKillAction.Arguments = '--kill gpg-agent'
$GpgRestartAction = $TaskDefinition.Actions.Create(0)
$GpgRestartAction.Path = 'gpg-connect-agent'
$GpgRestartAction.Arguments = '/bye'

$Credentials = Get-Credential
$TaskFolder.RegisterTaskDefinition('GpgAgentRefreshUnlock',$TaskDefinition,6,$credentials.username,[System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Credentials.password)),3)
```
* This is registered in `Task Scheduler Library` as `GPGAgentRefreshUnlock`.
* The `Subscription` query is [extracted from the manually][5] created scheduled
  task, instead of manually generating it. Just `Right Click > Export` and look
  in the XML file for `Subscription`.

This can be verified to work by restarting your machine or killing the current
agent with `gpgconf --kill gpg-agent` and locking/unlocking your screen then
attempting to use Putty. It is registered in `Task Scheduler Library` as
`GPGAgentUnlockRestart`.

You may noticed occasionsally that _command windows_ pop-up while the scheduled
task is executing. If this should be completely hidden, see [Hiding Command
Windows](#hiding-command-windows).

### (optional) Prompt on Terminal, Instead of Window
You may directly query for a password to use in the terminal if a pop-up
authentication prompt is too much. Just insert this and replace the secure
string marshaller on `RegisterTaskDefinition` with `$password`; though this will
leave a unencrypted password in memory. Remember to overwrite / delete this.

```powershell
$password = Read-Host -assecurestring "Please enter your password"
$password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))
```

Hiding Command Windows
----------------------
Windows may appear during the execution of actions involving `cmd`. However, the
build in method to hide windows [`start /b`][6] will fail as this is not the
first thing that executed in the scheduled task (it runs a command shell, then
executes start), or fail with the error `The operator or administrator has
refused the request`. The solution to this is to create a small visual basic
wrapper that calls your command with no window defined. The command will execute
in the wrapper, thus hiding the window creation.

It is **absolutely imperative** that this script be **signed and trusted** for
use, and that **non-signed vbs scripts are NOT trusted**. Otherwise, you've just
created a way for someone to potentially execute anything they want _as you_
whenever you login. If you don't know what the above means, then **don't do
this**.

quiet_launcher.vbs
```vbs
CreateObject("Wscript.Shell").Run "" & WScript.Arguments(0) & "", 0, False
```

Then modify Actions so that:
* Program/Script: `quiet_launcher.vbs`.
* Add arguments (optional): `full command with args`.

Demonstration of Scheduled Task at Login
----------------------------------------
As GPG agent can hangup [occasionally][7], only executing the restart on initial
login will produce problems with long-running systems, or surface scheduling
errors within Task Scheduler itself. This task will work, but will
sporadically fail. This is only kept as an example of the failure condition and
should not be used.

Powershell as Admin
```powershell
$job = Register-ScheduledJob `
   -Name GpgAgent `
   -ScriptBlock { gpg-connect-agent.exe /bye } `
   -Trigger (New-JobTrigger -AtLogOn -User $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)) `
   -ScheduledJobOption (New-ScheduledJobOption -StartIfOnBattery -ContinueIfGoingOnBattery) `
   -RunNow

# Change principal to run only on interactive logon instead of S4U (Service for user login).
$principal = New-ScheduledTaskPrincipal -LogonType Interactive -UserId $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
Set-ScheduledTask -TaskPath \Microsoft\Windows\PowerShell\ScheduledJobs\ -TaskName $job.Name -Principal $principal
```
* This job will appear in `Task Scheduler` as `GpgAgent` under
  `Task Scheduler Library > Microsoft > Windows > PowerShell > ScheduledJobs`

[1]: https://superuser.com/questions/1214736/windows-10-scheduled-tasks-with-workstation-lock-unlock-not-being-triggered/1217125
[2]: https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/new-scheduledtasktrigger?view=win10-ps
[3]: https://docs.microsoft.com/en-us/windows/desktop/com/com-objects-and-interfaces
[4]: https://docs.microsoft.com/en-us/windows/desktop/taskschd/task-scheduler-objects
[5]: https://blogs.technet.microsoft.com/wincat/2011/08/25/trigger-a-powershell-script-from-a-windows-event/
[6]: https://ss64.com/nt/start.html
[7]: https://www.kaylyn.ink/journal/windows-using-gpg-for-ssh-authentication-and-git/
[8]: gpg-agent-refresh-unlock.ps1

[ref1]: https://stackoverflow.com/questions/42801733/creating-a-scheduled-task-which-uses-a-specific-event-log-entry-as-a-trigger
[ref2]: https://community.spiceworks.com/topic/1030490-task-scheduler-vb-script-help?page=1#entry-4758670
[ref3]: https://social.technet.microsoft.com/Forums/office/en-US/f90bed75-475e-4f5f-94eb-60197efda6c6/prompt-for-password-without-using-getcredential-or-readhost-assecurestring-but-not-display-text?forum=winserverpowershell