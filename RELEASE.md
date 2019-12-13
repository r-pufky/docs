# [Changelog][3g]

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
