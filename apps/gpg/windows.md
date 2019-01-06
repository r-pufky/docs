Windows GPG Yubikey Config for Putty/SSH
----------------------------------------
Configure yubikey for SSH authentication on windows. Assumes [Yubikey has GPG
Subkeys pre-loaded](README.md).

1. [Creating GPG Keys][1]
1. [Export GPG Subkeys to Yubikey][2]
1. [Windows GPG Yubikey Setup][3]
1. [Ubuntu GPG Yubikey Setup][4]

Required Materials
------------------
1. [gpg4win][5] downloaded. **Verify Integrity**.
1. [Yubikey Manager][6] installed. Only required if you are changing keypress
   and NFC settings.
1. [Putty][7] installed.
1. Pre-configured Yubikey.

### Install GPG4Win on machine
This will provide GPG interactions as well as an agent to provide key material
to putty, winscp, etc.

1. Only install **gnupg**

### Add GPG to User Path
This will enable you to use commands anywhere on the system. Path is modified
using the [System Preferences][ref6] control panel plugin.

1. `win+r > sysdm.cpl > Advanced > Environment Variables`
1. Select `Path` under `User Variables`, click `edit`
1. Click `new` add `C:\Program Files (x86)\GnuPG\bin`
1. Ensure path is added at end of list and save.

Configure Yubikey
-----------------
Configure behavior of Yubikey so short touches will provide GPG material, while
long touches will provide Yubico OTP. This prevents accidental touches spewing
keystrokes into whatever is open. NFC is also disable.

1. Open Yubikey Manager
1. Select `Applications > OTP`
1. Delete `Slot 1`
1. Configure `Slot 2` to use `Yubico OTP`

Results should look like this:
![Yubikey OTP setup](yubikey-otp.png)

If your key has NFC support, this can be disabled as well.

1. Open Yubikey Manager
1. Select `Interfaces`
1. Uncheck **all** NFC options
1. Click `Save Interfaces`

Results should look like this:
![Yubikey interfaces setup](yubikey-nfc.png)

Configure GPG Agent
-------------------
### Import & Ultimate Trust Your Certificate
This will set ultimate trust for the [GPG public][12] certificate you created
when making your GPG key.

Open a command shell `win+x > command prompt`
```cmd
gpg --import YOUR_PUBLIC_GPG_KEY.asc
gpg --list-key
gpg --edit-key KEYID
trust
5
save
gpg --list-secret-keys
```
* `gpg --card-edit; fetch` will pull the GPG public key from the [URL
  provided][8] on the yubikey. This is better if you are using from multiple or
  new machines.
* KEYID is listed from `--list-key`
* `--list-secret-keys` should show `#` for private cert not on machine, and `>`
  for your signing, authentication and encryption certs on the Yubikey.

### Setup GPG Agent for SSH and Putty
This will enable SSH and Putty usage with the gpg-agent.

%appdata%\gnupg\gpg-agent.conf
```
enable-ssh-support
enable-putty-support
```

### Restart GPG Agent and Connect Agent
This will apply [configuration changes][9] made.
```cmd
gpgconf --kill gpg-agent
"c:\Program Files (x86)\GnuPG\bin\gpg-connect-agent.exe" /bye
```

Configure Putty
---------------
Ensure yubikey is readable by GPG. This assumes you have setup your _exported
GPG ssh key_ on the server you are connecting to already (e.g.
~/.ssh/authorized_keys).

```cmd
gpg --card-status
```
* If the Yubikey does not appear, reinsert the key.

### Setup Putty
Configure a host as your normally would. Ensure these additional optiosn are
enabled:

* Check `Connection > SSH > Auth` > Attempt authentication using Pageant
* Remove `Connection > SSH > Auth` > Private key file for authentication

Be sure to **save** your configuration changes.

### Logging In

1. Connect with putty as normal.
1. a `PinEntry` pop-up window should appear. It may not be in focus. Enter your
   **User PIN**. Click `OK`.

   ![PinEntry](pinentry.png)
   * Number is the Yubikey serial number.
   * Holder is the First/Last name of the GPG certificate on the key.
   * Your key will blink when waiting for password or touch.

1. There _will be no prompt_. **Tap Your Key**. If successful you will login.

Run GPG Agent on Login
----------------------
Scheduled Tasks are inconsistently applied and therefore you will run into
issues if you depend on the scheduled tasks to always run at login to refresh
your GPG agent. This is remedied by triggering on screen unlock events and
refreshing the GPG agent, ensuring that the agent is always ready and preventing
the need for manual restarts.

### Enable [Event Logging of Screen Lock & Unlock][14]
Configure Group Policy to log login/logout events so we can trigger.

```win + r > gpedit.msc```
> Key: Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration > System Audit Policies - Local Group Policy Object > Logon/Logoff >

> Policy: Audit Other Login/Logoff Events > Success = Enabled

> Policy: Audit Other Login/Logoff Events > Failure = Enabled4.
* Successful unlock events will be `4801`, and failures will be `4800`.

### Add Task Triggered on Unlock Events
This task will trigger on unlock events, even when logging in the first time.

```start > Task Scheduler > Task Scheduler Library```
* `Action > Create Task`
  1. General
    * Name: `GpgAgentUnlockRestart`.
    * Description: `Restarts GPG agent on windows unlock`.
    * Check: `Run only when user is logged on`.
    * Configure for: `Windows 10`.
    * Check: `Hidden`.
  1. Triggers
    * `New`.
    * Being the task: `On an event`.
    * Check: `Basic`.
    * Log: `Security`.
    * Source: `Microsoft Windows security auditing`.
    * Event ID: `4801`.
    * Check: `Enabled`.
  1. Actions
    1. `New`
      * Action: `Start a program`.
      * Program/Script: `gpgconf`.
      * Add arguments (optional): `--kill gpg-agent`.
    2. `New`
      * Action: `Start a program`.
      * Program/Script: `gpg-connect-agent`.
      * Add arguments (optional): `/bye`.
    * Ensure order is correct.
  1. Conditions
    * Uncheck: `ALL`.
  1. Settings
    * Check: `Allow task to be run on demand`.
    * Check: `Stop the task if it runs longer than` `3 days`.
    * Uncheck: `All Remaining`.

This can be verified to work by restarting your machine or killing the current
agent `gpgconf --kill gpg-agent` and locking/unlocking your screen then
attempting to use putty.

### Deprecated Scheduled Job Instructions
Setup a [scheduled job][10] to ensure gpg-agent is automatically running on
login.
* These are deprecated in favor of above, and will remain until above
  instructions are converted to powershell commands to run once.

Powershell as Admin
```powershell
$job = Register-ScheduledJob `
   -Name GpgAgent `
   -ScriptBlock { gpg-connect-agent.exe /bye } `
   -Trigger (New-JobTrigger -AtLogOn -User $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)) `
   -ScheduledJobOption (New-ScheduledJobOption -StartIfOnBattery -ContinueIfGoingOnBattery) `
   -RunNow

# Change principal to run only on interactive logon instead of S4U.
$principal = New-ScheduledTaskPrincipal -LogonType Interactive -UserId $([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
Set-ScheduledTask -TaskPath \Microsoft\Windows\PowerShell\ScheduledJobs\ -TaskName $job.Name -Principal $principal
```
* This also ensures it is started on power resume / on battery.
* This job will appear in `Task Scheduler` as `GpgAgent` under
  `Task Scheduler Library > Microsoft > Windows > PowerShell > ScheduledJobs`

Forward GPG Agent to Multiple Sub-Servers
-----------------------------------------
This is effectively using a single server as an SSH Bastion and SSH'ing to
additional machines through the bastion. Please note that while the connection
is active, it is possible to [**use them as you while you are connected**][13];
so a secured and monitored system should be used, if at all. Machines are
referred to as `putty` for your client machine, `bastion` for the machine you
will be SSH'ing through and `target` for remote SSH targets.

![Bastion](bastion.png)

### Putty
* Ensure `Connection > SSH > Auth > Allow agent forwarding` is enabled.

### Bastion
/etc/ssh/sshd_config
```bash
StreamLocalBindUnlink yes
AllowAgentForwarding yes
```
* _Exported GPG ssh key_ added to `authorized_keys` file for user.
* This will allow you to forward your credentials again to the next server.
* Removes current socket file for forwarding before creating a new one.
* Confirm new settings loaded with `sshd -T | grep -i allowagent`

### Target
* _Exported GPG ssh key_ added to `authorized_keys` file for user.

/etc/ssh/sshd_config
```bash
AllowAgentForwarding no
```
* Target does not need to enable outbound agent forwarding for this to work.

Errors & Problems
-----------------
### SSH connection failed, Server sent: publickey
Happens because of a standard publickey not provided / matched failure.

1. SSH public key is not loaded on the SSH server. Confirm your public SSH key
   (exported from GPG with `--export-ssh-key`) is added to `authorized_keys` for
   the user you are attempting to login with.
1. GPG agent configuration is not reloaded. Ensure ssh and putty support in
   configuration is set and `gpg-agent` and `gpg-connect-agent` are both
   restarted.

### Please insert card with serial number
![PinEntry wrong key](pinentry-wrong-key.png)

Occurs because the original key used for authentication is not the key being
used now. [GPG Agent caches the serial number][11] of the card for the KeyStub
used. This just needs to be removed.

1. Show all keygrips in GPG, these will be used to match cache in private store.
   ```cmd
   gpg --with-keygrip --list-keys
   ```
1. Identify keygrip in `%appdata%\gnupg\private-keys-v1.d\` and delete it, or
   you can just remove all keys in that directory.

[1]: README.md
[2]: yubikey.md
[3]: windows.md
[4]: ubuntu.md
[5]: https://www.gpg4win.org/package-integrity.html
[6]: https://www.yubico.com/products/services-software/download/yubikey-manager/
[7]: https://www.putty.org/
[8]: https://withinboredom.info/2017/11/18/signing-commits-ssh-with-yubikey-and-windows/
[9]: https://superuser.com/questions/1075404/how-can-i-restart-gpg-agent
[10]: https://www.kaylyn.ink/journal/windows-using-gpg-for-ssh-authentication-and-git/
[11]: https://security.stackexchange.com/questions/165286/how-to-use-multiple-smart-cards-with-gnupg
[12]: https://stackoverflow.com/questions/31784368/how-to-give-highest-trust-level-to-an-openpgp-certificate-in-kleopatra
[13]: http://www.unixwiz.net/techtips/ssh-agent-forwarding.html
[14]: https://superuser.com/questions/1214736/windows-10-scheduled-tasks-with-workstation-lock-unlock-not-being-triggered/1217125

[ref1]: https://developers.yubico.com/PGP/SSH_authentication/Windows.html
[ref2]: https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/
[ref3]: https://codingnest.com/how-to-use-gpg-with-yubikey-wsl/
[ref4]: https://ttmm.io/tech/yubikey/
[ref5]: https://occamy.chemistry.jhu.edu/references/pubsoft/YubikeySSH/index.php
[ref6]: https://ss64.com/nt/run.html
[ref7]: https://superuser.com/questions/161973/how-can-i-forward-a-gpg-key-via-ssh-agent