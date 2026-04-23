# App Bundles
Platform agnostic application distribution.

!!! info "Always use OS package manager"
    All app bundles include static libraries which are not updated with the OS.
    Typically this results in very large installs when the application itself
    is very small, and may introduce security vulnerabilities with included
    dependencies that are not updated with the OS.

    **Only** install app bundles when the OS cannot install the version that is
    required to be used.

## [AppImage][b]
AppImage is highly preferred over all other bundles. These tend to be the
smallest, and allow extraction to run directly in limited environments.

``` bash
# AppImages just need to be downloaded and set executable.
chmod +x Image.AppImage
Image.AppImage

# FUSE is required. LXC containers may need to extract the package first.
Image.AppImage --appimage-extract
./squashfs-root/AppRun
```

## [Flatpak][a]
Originally created by RedHat developers to simplify application deployment
across multiple distributions.

!!! warning "Only for Desktops"
    Heavy space bloat and most apps are heavily restricted, resulting in many
    issues in virtualized environments. Most will require **flatseal** to relax
    permissions for actual use.

=== "[Debian][d]"

    ``` bash
    sudo apt install flatpak

    # KDE Support
    sudo apt install plasma-discover-backend-flatpak

    # GNOME Support
    sudo apt install gnome-software-plugin-flatpak

    # Add repository
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    reboot
    ```

=== "CachyOS"

    ``` bash
    sudo pacman -S flatpak
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    reboot
    ```

``` bash
# Flatseal is used to modify sandbox permissions for flatpaks. Most flatpaks
# require additional access to function correctly.
flatpak install flathub flatseal

# Packages are install via flatpak
flatpak install flathub org.kde.digikam
flatpak install flathub org.musicbrainz.Picard
flatpak run org.kde.digikam
```

## [Snap (Snapcraft)][c]
Create by canonical and manages packages via snapd.

!!! warning "Not Recommended"
    Snap packages require a daemon to run and can randomly restart underlying
    services when installing/using apps. Use AppImage or Flatpak instead.

[a]: https://appimage.org
[b]: https://docs.flatpak.org/en/latest
[c]: https://snapcraft.io
[d]: https://flathub.org/en/setup/Debian
