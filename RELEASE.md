# [Changelog][3g]

## 2021-02-28.0
Finish sphinx CT directive migration.

Changed:
* gtable, ggui, w* directives migrated.

Removed:
* v1 ct sphinx tables removed.

## 2021-02-20.0
Split 20H2 documentation, update sphinx CT directives.

Added:
* Azure Media Services to youtube-dl scripts.
* proxmox (PVE) hypervisor configuration.
* git worktree/branch documentation.
* EdgeOS script for creating hosts.
* EdgeOS config to modify host file instead of manual edits.
* DNS caching service debugging for windows.
* Self-references for dropdowns.
* Hyper-V kernel extension disable.
* Highlight required sphinx import.

Changed:
* Use multi-core sphinx builds.
* Thoroughly clean builds with 'make clean'.
* timezone configuration for containers.
* Pi-Hole setup should only specify the upstream DNS server.
* radarr configuration to include full-chain cert workaround.
* sphinx style guide admonitions.

Removed:
* non-existant blocklists from pihole.

## 2020-12-18.0
Update sphinx core & enable additional extensions.

Added:
* sphinx-panel, sphinx_rtd_theme, sphinx_copybutton extensions.
* Windows 10 reset password.

Changed:
* Sphinx upgraded to 3.3.1.
* Sphinx dependencies updated.
* RTD theme migrated from 0.4.3.dev0 to pypi 0.5.0.
* Windows 1903 validated, using new templates.

Removed:
* static RTD theme.

## 2020-11-01.0
Separated Windows 1903 settings and fix link rot.

Added:
* Proxy/troubleshooting docs for NGINX.

Changed:
* Separate Windows 1903 settings from core windows 10.
* Ubuntu 18.04 no longer requires PPA for wireguard.
* NGINX start/run with docker backends down.
* Unban all fail2ban documentation.
* Windows defender run URI fixed.

## 2020-09-30.0
Add Wireguard, Pihole 5.x, Yubikey (Windows Hello), and sphinx venv to build.

Added:
* Add sphinx virtual python environment to build file. 
* Add wireguard documentation.
* Add notes about UFW conflicting with Docker.
* Add documentation for removing storage repository.
* Add saltstack job queue management notes.
* Add XCP guest template update from testing repo.

Changed:
* Correct DB typos for MUA setup.
* Update GPG/Yubikey for usage with Windows Hello Devices. 
* Update documentation for PiHole 5.x.
* Update Pi-Hole documentation with IPv6 port information.
* Update XCP documentation for 8.1.
* Update XCP documentation with VM copying / USB storage repository ins.

## 2020-03-29.0
Add MariaDB, DashMachine, DNSRoboCert, Postgres containers.

Added:
* mariadb container.
* dashmachine container.
* postgres container.
* dnsrobocert container.

Changed:
* vimrc updated with better organization, formatting.
* imapsync documentation updated.
* bulk downloader for reddit instructions added.

Removed:
* heimdall container (use dashmachine instead).
* letsencrypt container (superceeded by dnsrobocert).

## 2020-02-02.0
Dockerized Email Services.

Added:
* Add tamper protection disable for registry.
* Add instructions for disabling tamper protection via powershell.
* Add SSHD docker container with chroot and readonly filesystem.
* Add windows update taskbar notification removal.
* Add dockerized email services.
* Add git rebase, tagging instructions.

Changed:
* Update execution policy with additional options.
* Update SSH documentation with some additional troublshooting information.
* Use defaults file instead of systemd service for ssh options.
* Use `internal-sftp` for default SFTP server now, instead of separate binary. This has been the default for a few years. Explicitly make it so.

Documentation no longer in use has been removed.
* Removed: service/dovecot
* Removed: service/postfix

## 2019-01-03.0
Telemetry updates and documentation clarification.

Added:
* Add delivery optimization windows settings.
* Add disable of customer experience improvement program for windows.
* Add registry entries for paging file.
* Add windows spotlight disable.
* Add application telemetry for windows.
* Add disable for microsoft account sync in windows.
* Add windows error reporting disable for windows.
* Add facial recognition disable for Windows.
* Add phone call, voice activation privacy sections for windows 10 1909.
* Add voice activation to privacy settings for windows 1909.
* Add ubiquity telemetry disabled instructions. Fucking idiots. 
* Add GPG encryption documentation and yubikey verification.

Changed:
* Fix documentation formatting.
* Use dyanmic system restore disable script. Add GPO management.
* Update telemetry link.
* Update system restore points with registry and powershell commands.
* Update published documentation.
* Clarify authy TOTP wording.
* Update published documentation.
* Standardize document names and ensure default values are correct.
* Update Phone Calls privacy section for windows 1909.
* Update pihole documentation with blocklist and blacklist locations.

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
