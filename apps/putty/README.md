Putty Configuration

Generic notes until more finalized.

### putty timeouts
putty > connection > enable tcp keepalives
putty > connection > seconds between keepalives 0 -> 5

Export putty settings (or go through full registry dump)
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham

Create a putty shortcut that launches a profile:
http://superuser.com/questions/248099/a-putty-shortcut-that-automatically-launches-a-profile

### Changing escape characters
Sometimes the terminal escape sequences that are sent are changed if you are running through multiple screen sessions into docker, etc.

Determine the current escape sequences
```bash
stty -a
```
 * Find the escape sequence you are looking for (e.g. erase is for delete)

Determine the actual control sequence sent
```bash
ctrl + v, [desire key press]
```
 * This will print the escape sequence to the terminal

Set the correct sequence.
```bash
stty erase ^H
```
 * Sets the correct escape sequence
 * Generally should press the key instead of manually typing it


References
----------
[1]: https://unix.stackexchange.com/questions/43103/backspace-tab-not-working-in-terminal-using-ssh
