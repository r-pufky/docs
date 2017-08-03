# This is loaded on all non-interactive login shells
#
# This should contain all of your aliases and exports, so all shells have the
# same commands available (i.e. remote shells, etc)
#

export PATH=$PATH:/root/bin
export HISCONTROL=ignoreboth
export EDITOR='vim'

alias wipe='shred --iterations=35 --verbose --zero --remove'
alias grep='grep --color=auto'
