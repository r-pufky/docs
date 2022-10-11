# This is executed on interactive / login shells
# Order: .bash_profile, .bash_login, .profile
#
# This is where all of your interactive prompt stuff should go
#

# If not running interactively, quit
[ -z "$PS1" ] && return

# Resize the terminal columns/rows if window is resized
shopt -s checkwinsize

# Get default route primary adapter IP.
IP=`ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p'`

# use colors/export terminal title if not dumb terminal
if [ "$TERM" != "dumb" ]; then
  # (S)tart and (E)nd blocks required on prompt, so commandline doens't break
  S="\["
  E="\]"
  LIGHTBLUE="\e[0;36;40m"
  PINK="\e[0;35;40m"
  RED="\e[0;31;40m"
  YELLOW="\e[0;33;40m"
  BOLDGREEN="\e[0;32;40m"
  GRAY="\e[0;37;40m"

  PS1="\n$LIGHTBLUE[\! $S$PINK$E\t$S$LIGHTBLUE$E|$S$RED$E\u$S$LIGHTBLUE$E@$S$YELLOW$E$IP$S$LIGHTBLUE$E:$S$BOLDGREEN$E\w$S$LIGHTBLUE$E]$S$GRAY$E\n$ "
fi

# Include all aliases and exports from non-interactive shells
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi