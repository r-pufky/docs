# Windows

!!! tip
    See [Trust GPG Key Locally][a]for importing your public key and assigning
    ultimate trust for use.

    Requires **~/.ssh/authorized_keys** on target machine with your exported
    GPG SSH RSA Public Key. See [GPG Export Keys][b]. See [SSH][c] for remote
    SSH configuration.


## Configure GPG4win
GPG4Win provides middleware to enable Yubikey GPG use. Download [gpg4win][d]
and verify integrity.

!!! example "⌘ ➔ sysdm.cpl ➔ Advanced ➔ Environment Variables ➔ User variables for {USER} ➔ Path ➔ Edit ➔ New"
    * Path: **c:\Program Files (x86)\GnuPG\bin**

    Add GPG path to end of list for global user profile access.

### Configure [GPG Agent][e]
!!! example "⌘ ➔ Device Manager ➔ Software Devices"
    Get Yubico device name as listed. **Show Hidden Devices** may be necessary.

    Use the **full name** in **scdaemon.conf**.

!!! abstract "%appdata%\gnupg\scdaemon.conf"

    ``` bash
    # Prevent Windows Hello from acting as an pagent device.
    # Results in no key found errors.

    # Device Manager Yubico full name.
    reader-port Yubico YubiKey OTP+FIDO+CCID 0
    ```

!!! abstract "%appdata%\gnupg\gpg-agent.conf"

    ``` bash
    enable-ssh-support
    enable-putty-support
    ```

Restart GPG Agent and Connect Agent to apply changes.
``` bash
gpgconf --kill gpg-agent

# Once path is set: gpg-connect-agent.exe /bye
"c:\Program Files (x86)\GnuPG\bin\gpg-connect-agent.exe" /bye
```

### Configure Putty
Download [Putty][f].

!!! example "Putty ➔ Connection ➔ SSH ➔ Auth"
    * Attempt authentication using Pageant: ✔
        * Private key file for authentication: **{EMPTY}**

Save host changes.

#### Verify Putty Works
1. Connect with Putty as normal.
2. A **Pin Entry** pop-up window should appear. It may not be in focus. Enter
   your **user** [PIN][g].

    ![Pin Entry](pin_entry.png)

3. Touch key to confirm (key will blink during wait for password).

## WinSCP Transfer File Through a Bastion
Import a working GPG Putty configuration into WinSCP. Create a copy of the
working configuration and edit it.

### Enable [GPG Agent Forwarding in Putty][h]
!!! example "WinSCP ➔ Site"
    * Host name: {Internal IP}
    * Port number: {Internal Port}
    * User name: {USER}
    * Password: **Empty**
    * Private key file: **Empty**

### Define [Bastion Tunnel][h]
!!! example "WinSCP ➔ Site ➔ Advanced Site Settings ➔ Connection ➔ Tunnel"
    * Connect through SSH Tunnel: ✔
    * Host name: **{Bastion External Address}**
    * Port number: **{Bastion External Port}**
    * User name: **{USER}**
    * Password: **{EMPTY}**
    * Private key file: **{EMPTY}**

### Enable [SSH Agent Forwarding][h]
!!! example "WinSCP ➔ Site ➔ Advanced Site Settings ➔ SSH ➔ Authentication"
    * Attempt authentication using Pageant: ✔
    * Allow agent forwarding: ✔

Save the configuration and connect. May be prompted for two authentication
touches, one for each system.

## Run GPG Agent on Login
Scheduled Tasks are inconsistently applied and therefore you will run into
issues if you depend on the scheduled tasks to always run at login to refresh
your GPG agent. This is compounded by GPG agent occasionally hanging and needing
to be force restarted. Resolve by triggering GPG agent refresh on screen unlock
events, ensuring that the agent is always ready.

### Enable Login/Logoff Events
!!! example "Computer Configuration ➔ Windows Settings ➔ Security Settings ➔ Advanced Audit Policy Configuration ➔ System Audit Policies - Local Group Policy Object ➔ Logon/Logoff ➔ Audit Other Login/Logoff Events"
    * Configure the following audit events: ✔
    * Success: ✔
    * Failure: ✔

### Trigger GPG agent refresh on Login/Logoff Event
!!! example "⌘ ➔ Task Scheduler ➔ Task Scheduler Library ➔ Action ➔ Create Task"
    * General:
        * Name: **GpgAgentRefreshUnlock**
        * Description: **Restarts GPG agent on windows unlock**
        * Check: **Run only when user is logged on**
        * Configure for: **Windows {VERSION}**
        * Hidden: ✔
    * Triggers:
        * Begin the task: **On an event**
        * Check: **Basic**
        * Log: **Security**
        * Source: **Microsoft Windows security auditing**
        * Event ID: **4801**
        * Hidden: ✔
    * Actions:
        * First Action (Always execute first)
            * Action: **Start a program**
            * Program/Script: **gpgconf**
            * Add arguments: **–kill gpg-agent**
        * Second Action (Always execute last)
            * Action: **Start a program**
            * Program/Script: **gpg-connect-agent**
            * Add arguments: **/bye**
    * Conditions: ✘
    * Settings:
        * Allow task to be run on demand: ✔
        * Stop the task if it runs longer than: ✔
        * Stop the task if it runs longer than: **3 days**
        * All Remaining: ✘

## Forward GPG Agent [Through Multiple Servers][i]
!!! warning
    While the connection is active it is possible for others to use them as you
    while you are connected even though your private credential are on your
    local machine.

Machines are referred to as **putty** for your client machine, **bastion** for
the machine you will be SSH'ing through and **target** for remote SSH targets.

![Bastion](bastion.png)

### Enable GPG Agent Forwarding in Putty
!!! example "Putty ➔ Connection ➔ SSH ➔ Auth"
    * Allow agent forwarding: ✔

### Bastion Configuration
!!! abstract "/etc/ssh/sshd_config"
    0644 root:root

    ``` bash
    # Remove current socket file for forwarding before creating a new one.
    StreamLocalBindUnlink yes

    # Enable forwarding your credentials again to the next server.
    AllowAgentForwarding yes
    ```

Confirm new settings are loaded on Bastion.
``` bash
sshd -T | grep -i allowagent
```

### Target Configuration
Target does not need to enable outbound agent forwarding.

!!! abstract "/etc/ssh/sshd_config"
    0644 root:root

    ``` bash
    AllowAgentForwarding no
    ```


## Reference[^1][^2][^3][^4][^5][^6]

[^1]: https://developers.yubico.com/PGP/SSH_authentication/Windows.html
[^2]: https://www.linode.com/docs/guides/gpg-key-for-ssh-authentication/
[^3]: https://codingnest.com/how-to-use-gpg-with-yubikey-wsl/
[^4]: https://ttmm.io/tech/yubikey/
[^5]: https://occamy.chemistry.jhu.edu/references/pubsoft/YubikeySSH/index.php
[^6]: https://superuser.com/questions/161973/how-can-i-forward-a-gpg-key-via-ssh-agent

[a]: ../setup/import.md#trust-gpg-public-key-locally
[b]: ../setup/backup.md#export-gpg-keys
[c]: ../../../service/ssh/README.md
[d]: https://www.gpg4win.org/package-integrity.html
[e]: https://superuser.com/questions/1075404/how-can-i-restart-gpg-agent
[f]: https://www.putty.org
[g]: ../../../glossary/yubikey.md#yubikey-passwordpin
[h]: https://winscp.net/eng/docs/ui_login_tunnel
[i]: http://www.unixwiz.net/techtips/ssh-agent-forwarding.html
