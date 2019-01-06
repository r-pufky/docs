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
$TaskFolder.RegisterTaskDefinition('GpgAgentUnlockRestartNew',$TaskDefinition,6,$credentials.username,[System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Credentials.password)),3)
