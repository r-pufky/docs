.. _wbase-specific-windows-fixes-background-apps:

Fix Windows Applications Not Appearing in Start Menu Searches
#############################################################
Background Tasks need to be enabled for the application index to be updated when
new programs are installed. By disabling all background tasks (global toggle)
this index is never updated, and therefore apps will stop appearing in start
menu searches. You can still disable all apps in the background, however the
service still needs to be enabled.

:cmdmenu:`⌘ + r --> ms-settings:privacy-backgroundapps`

   * Let apps run in the background: ☑

`Reference <https://superuser.com/questions/947392/windows-10-search-cant-find-any-applications-even-calculator>`__
