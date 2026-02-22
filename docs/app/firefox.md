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

## [Disable Speech Dispatcher][c]
Only use for accessibility screen readers. Will produce an error if enabled and
not setup. Create as needed.

!!! example "about:config"
    * media.webspeech.synth.dont_notify_on_error: **true**
    * media.webspeech.recognition.enable: **false**
    * media.webspeech.synth.enabled: **false**

[a]: https://www.firefox.com/en-US/browsers/desktop/windows/
[b]: https://connect.mozilla.org/t5/discussions/remove-ai-garbage/m-p/96009
[c]: https://discuss.cachyos.org/t/speech-dispatcher-error-in-firefox/21131