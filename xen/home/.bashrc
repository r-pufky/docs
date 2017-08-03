# This is loaded on all non-interactive login shells
#
# This should contain all of your aliases and exports, so all shells have the
# same commands available (i.e. remote shells, etc)
#
case $- in
    *i*) ;;
      *) return;;
esac

export PATH=$PATH:~/bin
export HISTCONTROL=ignoredups
export EDITOR='vim'

# Allow groups to read/execute, no permissions to others
umask 027

alias wipe='shred --iterations=35 --verbose --zero --remove'
alias src='screen -D -R'
alias grep='grep --color=auto'
