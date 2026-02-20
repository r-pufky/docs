# Firefox

=== "CachyOS"
    Install via AUR helper.

    ``` bash
    pacman -S firefox
    ```

=== "Manjaro"
    Install via AUR helper.

    ``` bash
    pacman -S firefox
    ```

    !!! example "chrome://settings/appearance"
        * Use system title bar and borders: ✔

=== "Windows"
    [Download][a] and install.


## [Disable AI][b]

!!! example "about:config"
    * browser.ml.chat.enabled: **false**
    * sidebar.revamp: **false**
    * browser.ml.enable: **false**
    * browser.ml.chat.enabled: **false**
    * extensions.ml.enabled: **false**
    * browser.ml.linkPreview.enabled: **false**
    * browser.tabs.groups.smart.enabled: **false**
    * browser.tabs.groups.smart.userEnabled: **false**

[a]: https://www.firefox.com/en-US/browsers/desktop/windows/
[b]: https://connect.mozilla.org/t5/discussions/remove-ai-garbage/m-p/96009
