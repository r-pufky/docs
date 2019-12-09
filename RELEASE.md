# [Changelog][3g]

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