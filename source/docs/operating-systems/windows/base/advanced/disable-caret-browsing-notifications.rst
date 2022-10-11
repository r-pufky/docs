.. _wbase-specific-windows-fixes-disable-caret-browsing-notifications:

Disable Caret Browsing Notifications
####################################
Remove notification on F7 press for caret browsing. This is a holdover from
Internet Explorer.

.. gpo::   Disable Caret Browsing Notifications
  :path:   User Configuration -->
           Administrative Templates -->
           Windows Components -->
           Internet Explorer -->
           Internet Control Panel -->
           Advanced Page -->
           Turn on Caret Browsing support
  :value0: ☑, {DISABLED}
  :ref:    https://www.thewindowsclub.com/enable-caret-browsing-internet-explorer
  :update: 2021-02-19
