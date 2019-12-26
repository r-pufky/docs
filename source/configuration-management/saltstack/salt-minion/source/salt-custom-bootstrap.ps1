<#
.SYNOPSIS
    Install a custom bootstrapped salt-minion on windows.

.DESCRIPTION
    Install a specified version of salt-minion with optional pre-seeded config;
    automatically starts the service.

.EXAMPLE
    ./salt-custom-bootstrap.ps1 -domain mydomain.com
    Install using default values. Hostname will be automatically determined from
    the install machine.

.EXAMPLE
    ./salt-custom-bootstrap.ps1 -domain mydomain.com -config salt-config.zip -confirm
    Install using with custom domain and pre-seeded configuration, skip
    confirmation prompt.

.EXAMPLE
    ./bootstrap-salt.ps1 -version 2019.2.2 -master salt -minion myminion -config salt-config.zip -domain example.com
    Install salt minion 2019.2.2 and overlay custom salt configuration, with the
    minion id: myminion.

.PARAMETER version
    Salt-minion version to install. Default: latest.

.PARAMETER master
    Name or IP of the master server. Installer defaults to 'salt'.

.PARAMETER minion
    Name of the minion being installed on this host. Installer defaults to the
    host name.

.PARAMETER repo
    URL to the windows packages. Default is 'https://repo.saltstack.com/windows'

.PARAMETER working
    Working directory for script to hold temporary files. Defaults to Appdata.

.PARAMETER config
    Optional Zip file containing configuration overlay. This should be created
    with folder structures in place for salt/conf. A sha256 checksum must also
    exist in the same location of the zip file to validate it.

    Example salt-config.zip:
     pki/minion/master_sign.pub
     minion.d/*.conf

.PARAMETER saltdir
    Salt installation directory. Do not change.

.PARAMETER domain
    Domain that the salt-master and salt-minion are on.

    e.g.: example.com

.PARAMETER confirm
    Flag to auto-accept confirmation on script run.

.PARAMETER ports
    Flag to enable incoming connections on TCP 4505-4506 in windows firewall.

    This is NOT NEEDED for salt-minions to work. Dangerous.
#>

[CmdletBinding()]
Param (
    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    # Doesn't support versions prior to "YYYY.M.R-B"
    [ValidatePattern('^201\d\.\d{1,2}\.\d{1,2}(\-\d{1})?|(rc\d)$')]
    [string]$VERSION = 'Latest',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$MASTER = 'salt',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$MINION = "$(hostname)",

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$REPO = 'https://repo.saltstack.com/windows',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$WORKING = "$env:temp\salt-minion-installer",

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$CONFIG = '',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$SALTDIR = 'c:\salt\conf',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [string]$DOMAIN = 'example.com',

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [switch]$CONFIRM,

    [Parameter(Mandatory=$false,ValueFromPipeline=$true)]
    [switch]$PORTS
)

Import-Module BitsTransfer
$ARCH = if ([IntPtr]::Size -eq 4) {'x86'} else {'AMD64'}
$BINARY = "Salt-Minion-$VERSION-Py3-$arch-Setup.exe"
$MASTER = "$MASTER.$DOMAIN"
$MINION = "$MINION.$DOMAIN"

Write-Output "Version:       $VERSION"
Write-Output "Master:        $MASTER"
Write-Output "Minion:        $MINION"
Write-Output "Repository:    $REPO"
Write-Output "Working Dir:   $WORKING"
Write-Output "Custom Config: $CONFIG"
Write-Output "Salt Dir:      $SALTDIR"
Write-Output "Platform:      $ARCH"
Write-Output "Binary:        $BINARY"
Write-Output "Expose Ports:  $PORTS"
if (-Not $CONFIRM) {
  Read-Host -Prompt 'Confirm install options (press any key) or CTRL+C to quit.'
}

function Get-IsAdministrator {
    $Identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $Principal = New-Object System.Security.Principal.WindowsPrincipal($Identity)
    $Principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Run-AsAdmin {
  If (!(Get-IsAdministrator)) {
    Write-Host 'You must run this script as an Administrator.' -BackgroundColor red
    Write-Host 'Ensure unrestricted execution policy: ' -NoNewLine
    Write-Host 'Set-ExecutionPolicy Unrestricted' -ForegroundColor yellow
    exit 3
  }
}

function Validate-File {
  param (
    [string] $File,
    [string] $ChecksumFile
  )
  $Checksum = Get-Content $ChecksumFile -First 1
  $Fields = $Checksum -split '\s+'
  $Hash = $Fields[0].Trim().ToUpper()

  $BinaryHash = (Get-FileHash -Algorithm sha256 $File).Hash.ToUpper()

  if ($Hash.Equals($BinaryHash)) {
      Write-Host $File,' ' -NoNewLine
      Write-Host "Passed" -BackgroundColor green -ForegroundColor black
  } else {
      Write-Host $File,' ' -NoNewLine
      Write-Host "Not Passed" -BackgroundColor red
      Write-Host "File:     ", $Hash
      Write-Host "Computed: ", $BinaryHash
      exit 2
  }
}

function Setup-Prerequistes {
  New-Item $WORKING -ItemType Directory -Force | Out-Null
}

function Install-Config {
  if ($CONFIG -eq '') {
    Write-Host 'No custom config defined. ' -NoNewline
    Write-Host 'Not installing' -BackgroundColor green -ForegroundColor black
    return
  }
  Validate-File "$PSScriptRoot/$CONFIG" "$PSScriptRoot/$CONFIG.sha256"
  Write-Host 'Installing custom config ... ' -NoNewline
  Expand-Archive "$PSScriptRoot/$CONFIG" -DestinationPath $SALTDIR -Force | Out-Null
  Write-Host 'Done' -BackgroundColor green -ForegroundColor black
}

function Download-Minion {
  Start-BitsTransfer -Source "$REPO/$BINARY" -Destination $WORKING -DisplayName 'Salt-Minion' -Description 'Downloading salt-minion binary ...'
  Start-BitsTransfer -Source "$REPO/$BINARY.sha256" -Destination $WORKING -DisplayName 'Salt-Minion Integrity Check' -Description 'Downloading salt-minion binary Integrity hash ...'
  Validate-File "$WORKING/$BINARY" "$WORKING/$BINARY.sha256"
}

function Install-Minion {
  Write-Host 'Installing salt-minion ... ' -NoNewLine
  Start-Process "$WORKING/$BINARY" -ArgumentList "/master=$MASTER","/minion-name=$MINION",'/start-minion=0','/S' -Wait -NoNewWindow -PassThru | Out-Null
  Write-Host 'Done' -BackgroundColor green -ForegroundColor black
}

function Start-MinionService {
  $service = Get-Service salt-minion -ErrorAction SilentlyContinue
  While (!$service) {
    Start-Sleep -s 2
    $service = Get-Service salt-minion -ErrorAction SilentlyContinue
  }

  $try = 0
  While (($service.Status -ne "Running") -and ($try -ne 5)) {
    Start-Service -Name 'salt-minion' -ErrorAction SilentlyContinue
    $service = Get-Service salt-minion -ErrorAction SilentlyContinue
    Start-Sleep -s 2
    $try += 1
  }
  If ($service.Status -eq "Stopped") {
    Write-Host 'Failed to start salt minion' -NoNewline -BackgroundColor red
    exit 1
  }
  Set-Service -Name salt-minion -StartupType Automatic
  Write-Host 'salt-minion service started.' -NoNewline -BackgroundColor green -ForegroundColor black
}

function Enable-Connections {
  if ($PORTS) {
    Write-Host 'Enabling minion connections ... ' -NoNewLine
    Start-Process netsh -ArgumentList 'advfirewall','firewall','add','rule','name=Salt-Minion','dir=in','action=allow','protocol=TCP','localport=4505-4506' -Wait -NoNewWindow -PassThru | Out-Null
    Write-Host 'Done' -BackgroundColor green -ForegroundColor black
  }
}

Run-AsAdmin
Setup-Prerequistes
Install-Config
Download-Minion
Install-Minion
Start-MinionService
Enable-Connections