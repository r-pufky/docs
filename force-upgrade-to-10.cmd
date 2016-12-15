REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\UpgradeExperienceIndicators" /v UpgEx | findstr UpgEx
if "%errorlevel%" == "0" GOTO RunGWX
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Appraiser" /v UtcOnetimeSend /t REG_DWORD /d 1 /f
schtasks /run /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"
:CompatCheckRunning
schtasks /query /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"
schtasks /query /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" | findstr Ready
if NOT "%errorlevel%" == "0" ping localhost >nul &goto :CompatCheckRunning
:RunGWX
schtasks /run /TN "\Microsoft\Windows\Setup\gwx\refreshgwxconfig"
