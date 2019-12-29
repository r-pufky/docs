# [Changelog][3g]

## 2019-12-28.0
Windows Telemetry, NGINX authz, Signal Notifications.

Added:
* Separate and Add detailed documentation for Windows Telemetry and Securing.
* Add GPO for disabling windows defender systray notification.
* Add service for disabling windows diagnostic policy service.
* Add group policy reference and windows salt-call clarification.
* Add initial salt-minion custom installer with config pre-seeding.
* Add saltstack documentation for regenerating master.pem, master.pub.
* Add saltstack minion authentication of master servers.
* Add authz setup for NGINX.
* Add expanded nginx header debugging.
* Add vim flow control commands.
* Add bash snippets and move git snippets to apps.
* Add vim documentation and clarify makefile.
* Add GIT scripts and snippets to documentation.
* Add salt documentation for running a specific state.
* Add Signal CLI documentation.
* Add disable windows backup to additional fixes.
* Add make head option to only upload source changes.
* Add windows 10 usb device speed fix documentation.
* Add Edge browser removal documentation.
* Add windows registry data types, move command reference to reference section.
* Add WSL documentation and standardize windows drive formatting.
* Add windows epfwwfp.sys bluescreen fix.
* Add WIFI password dump for windows.
* Add docker login and push instructions.
* Add docker image tagging.

Changes:
* Update video conversion docs.
* Update youtube-dl syntax with recent update.
* Adjust highlighting based on conf.py changes.
* Add help section for Makefile.
* Remove version tag from sphinx conf.py.

Fixes:
* linkcheck updated to ignore latest github repos, as they will always redirect
  to the latest tagged version.

## 2019-12-12.0
Consolidate sphinx documentation.

Changes:
* Use {CAPS WITH SPACES} for user variables.
* Update windows landing page with subpage links.
* Update style-guide with variable and link guidance.
* Update build documentation with how to check links.
* Updated ConfigTable version.
* Update sphinx build and style guide docs.
* Remove unused variables from Makefile.
* Migrate Conan Exiles / 7 Days to Die docker service.
* Removed unifi-controller VM template. Use service/unifi.
* Move Play-On to services, and remove VM templates.
* Convert Play-On requirements to ConfigTable table.
* SSH documentation moved into SSH service; references updated as needed.
* Variables standardized (e.g. USER/USERNAME).
* Consolidate glossaries to a single location.

Fixes:
* aafig does not support the CheckExternalLinksBuilder (returns
  format = ''); override with an explicit no output for aafig if
  the builder format cannot be determined. This does not change the
  code otherwise.
* Add explicit linkcheck option for Makefile, as specifying a custom
  configuration location breaks the option interpretation.
* Update link checker configuration and fix links.

## 2019-12-08.1
Published sphinx documentation.

Breaking Changes:
* All markdown converted to RST(sphinx) for better presentation, linking,
  and cross references.
* Documentation migrated as-is, exceptions:
  * Containerized services had non-containerized documentation dropped.
  * Pi-Hole docker documentation removed.
  * Duplicate documentation removed due to sphinx reference ability.
* Only remaining markdown is for simple documentation, e.g. README and RELEASE.

## 2019-12-08.0
RST conversion complete.

* MD to RST conversion complete. Cutting release before changing repository around.

## 2019-07-06.0
Documentation no longer in use has been removed.

* Removed: configuration-management/puppet
* Removed: apps/tomahawk
* Removed: services/autosshd
* Removed: servies/ombi
* Removed: services/pxe
* Removed: virtualization/vm-templates/unifi-controller.md

[3g]: https://keepachangelog.com/en/1.0.0/
