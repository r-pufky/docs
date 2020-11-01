REM Move to script dirrectory for working directory and remove edge.
REM Requires install_wim_tweak to be in the path.
@echo off
cd /d "%~dp0"
echo Uninstalling Microsoft Edge ...

install_wim_tweak.exe /o /l
install_wim_tweak.exe /o /c Microsoft-Windows-Internet-Browser-Package /r
install_wim_tweak.exe /h /o /l

echo Reboot to apply changes.
pause