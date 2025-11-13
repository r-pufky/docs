# [Release Changelog](https://keepachangelog.com/en/1.0.0/)

## 2.1.0:
Restructure organization.

Changed:
* Enforce 80 character limits where possible for markdown source.
* Use reference links for any links that interrupt markdown reading flow.
* Use Footnote references for general page links.

## 2.0.3:

Added:
* Add BlueBubbles server configuration.
* PiKVM: Added configuration.
* Debian: CryptFS remote rescue over dropbear and wireguard.
* Shield TV: Disable Ads, alternative launcher,
* GIT: Reduce Repository Size (Prune).
* Windows 11: EA Updater (or other apps) showing in search results
* Windows 11: Disable USB Selective Suspend
* Windows 11: Prevent Disk Check on Every Boot
* Windows 11: Astro A40's Not Consistently Working
* Windows 11 requires DAC to be directly connected.
* Hard Reset Locked Yubikey Devices.
* Fixing readonly IronKey devices.
* Recover from a Bad Upgrade with Encrypted Root Disk.
* List of User Installed Packages.
* List of Package by Install Date.

Changed:
* Break GIT into multiple sections.
* Update ykman commands with modern CLI argument.

## 2.0.2
Update and add additional configuration notes.

Added:
* ZFS SVOL configuration, de-duplicate saving check.
* VSCodium configuration and preferences.
* VSCodium troubleshooting section.
* Add VSCodium customization and GIT signed commits.
* Add Kindle Adbreak jailbreak notes.
* KDE windows opening on wrong monitor fix.
* Manjaro updates failing after 6+ months of no updates.
* Manjaro settings notifier mutes.
* Bash last CLI argument use.
* GPG pinentry not redirecting to correct terminal
* Switch to a User with no login shell

## 2.0.1
Modern manjaro settings.

Added:
* Games section (Elden Ring, Escape from Tarkov).

Changed:
* Manjaro settings updated to current release.

## 2.0.0
A large number of outdated documentations has been removed. See 2022-10-19.0
release to find it.

Added:
* mkdoc-material support with minimal plugins and extensions.

Changed:
* Updated documentation to markdown.
* Switch to Schematic versioning.

Removed:
* Sphinx and all related sphinx code.
* Windows documentation removed in lieu of utilities that provide
  similar benefits with much less maintenance work.

Added:
* mkdocs-material implementation.

## 2022-10-19.0
Changed:
* Migrate sphinx/documentation to sphinx-design.
* Config Table updated to use sphinx-design (sphinx-panels deprecated).
* Updated documentation to use new sphinx-design base directives.
* Makefile updated with additional purge_cache command.

## 2022-10-06.0
Added:
* Nahimic service disable.
* Deletion of system volume information.
* Linux captive portal login configuration.
* Deletion of windows system volume information for foreign disks.
* Corrected link for realtek service disable.
* Privacy fix for vscodium setttings-sync extension.
* nodejs non-root installation in manjaro
* VSCodium new terminal preferences configuration
* Windows youtube-dl libav tool installation
* Multiple edition configuration for radarr.
* Multiple edition plex support in radarr configuration.
* Firefox certificate authenticaiton to NGINX.

Changed:
* Convert refs archives to zip for easy windows use.
* Update manjaro/youtube documentation.
* KDE reduced focus steal prevention to none
* VSCodium settings sync added new ignore directory ('node_modules')
* Standardize mouse click instructions to use badges.
* Converted all LMB/MMB/RMB in RST to badges ({LMB}, etc).
* Rendered icons are now unicode runes.
* Radarr/Sonarr quality options updated.
* Radarr/Sonarr indexer hard limits set.
* Add attention header for manjaro KDE theme settings.

Fixed:
* Use empty list for ct._sanitize_data on no data passed.
* Fix broken refsi-mirror.zip link.
* Fix header length issue for firefox client certificate.

## 2022-01-21.0
Add Windows 10 21H2 documentation.

Added:
* Used 20H2 as base and revalidated for 21H2.
* Added RTC/UTC clock for Windows dual boot.
* Added git commands for rebasing historical commits.

Changed:
* Dropped regedits when possible.
* Updated settings to be reflective of out-of-box usage; versus strict
  lockdown (e.g. camera, microphone are enabled but enough info is there
  for a user to disable if wanted).
* Moved 10 base to Windows base install.
* Separated base advanced settings into separate files.
* Updated SNMP requirements for Brother printer.

Removed:
* Removed 1903 documentation.

## 2022-01-09.0
Add Printing Setup.

Added:
* Manjaro setup instructions.
* Add empty ReFS mirrored virtual disk.
* Clean up Manjaro documention, Add 'ADD' badge.
* Add multi-screen, arc-dark SDDM login setup for KDE Plasma.
* Add force pull for git.
* Add network printing configuration.
* Linux settings for Chrome cert auto-select.

Fixed:
* Remove pkg-resources==0.0.0 from requirements.txt
* Updated sphinx badges with HTTPS and HTTP support.
* Corrected 'received' spelling error.

## 2021-12-15.0
Add Manjaro Setup.

Added:
* Manjaro setup instructions.

Fixed:
* Remove pkg-resources==0.0.0 from requirements.txt

## 2021-09-22.0
Remove Saltstack; add Ansible.

Added:
* Add Movie Studio encoding templates.
* Add fix for failed to run vncproxy on pve.
* Add note about fc-cache now generating .uuid files.
* Add GPG agent forwarding for WSL2 and Linux machines.
* Add CLI static DHCP configuration.
* Add apt auto selection to docs.
* Add 7 days to die administrative commands link.
* Add git commands for creating repository tracked hooks.
* Add disable for Asus Armoury Crate.
* Add additional git merge instructions for backing out and generating log.
* Add firefly baremetal setup instructions.
* Add git stash notes.
* Add crashplan LXC/KVM/Baremetal instructions.
* Add Instructions for GPU passthru to LXC containers.
* Add pve subscription removal service.
* Add gitea troubleshooting information for timeouts and duplicate keys.
* Add dropbear service.
* Add ZFS sync send/recv commands with automation.
* Add installing older game versions on Steam.
* Add SSH blocked through wireguard network resolution.
* Add wireguard-initramfs instructions.
* Add PFX RSA public/private, certificate extraction instructions.
* Add wireguard kernel debugging configuration.
* Add ansible notes.
* Add ansible auto-decrypt vault with security key scripts.
* Add Movie Studio encoding templates.
* Add fix for failed to run vncproxy on pve.
* Add note about fc-cache now generating .uuid files.
* Add GPG agent forwarding for WSL2 and Linux machines.
* Add CLI static DHCP configuration.
* Add apt auto selection to docs.

Changed:
* Correct links and formatting for gpg/ansible docs as well.
* Update ZFS manaul disk replacement instructions.
* Update for automatic partitioning, manual swap, locating devices/ZFS GUID.
* Update PFX RSA cert extraction to single commands.
* Update ZFS instructions with Encryption and dataset usage.
* Update proxmox instructions for version 7.
* Update PVE with GPU passthru instructions.

Removed:
* Remove saltstack configuration notes, add ansible configuration notes.

Fixed:
* Update pygments to 2.7.4 addressing CVE-2021-27291
* Update jinja, urllibs based on security advisories.

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
