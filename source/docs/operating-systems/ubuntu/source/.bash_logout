# ~/.bash_logout: executed by bash(1) when login shell exits.
# Clear history, and screen on logout.
if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi

cat /dev/null > ~/.bash_history && history -c && exit
