Putty Configuration

Generic notes until more finalized.

### putty timeouts
putty > connection > enable tcp keepalives
putty > connection > seconds between keepalives 0 -> 5

Export putty settings (or go through full registry dump)
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham

Create a putty shortcut that launches a profile:
http://superuser.com/questions/248099/a-putty-shortcut-that-automatically-launches-a-profile
