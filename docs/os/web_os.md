# WebOS
Smart TV Asshattery.

!!! danger
    **Always** hard block WebOS with firewall rules and Destination NAT (DNAT).

    Track MAC addresses and block on all network devices even if not configured
    for use (e.g. Wifi and Ethernet).

    TV **will** upload viewing habits and display Ads regardless of settings.

!!! tip
    TV's are displays and should be dumb. Use another device that is upgradable
    and not motivated to harvest user data for playing media.

## [Disable Always On Voice Recording][b]
!!! warning
    Internet is required to disable 'Always Ready'. Disable **immediately**
    after setting this option to prevent Updates.

!!! example "⚙ ➔ AI Settings"
    * Voice: **Disable ALL voice settings**
    * Always Ready: ✘

!!! example "⚙ ➔ General ➔ Terms ➔ User Agreements"
    Disable all.

!!! warning
    Disable Internet connection.

!!! example "⚙ ➔ General ➔ Terms ➔ User Agreements"
    Disable all. Option sometimes re-enables during network state changes.

## [Disable LG shutdown logo][c]
!!! example "🔇 ➔ 🔇 ➔ 🔇 ➔ 🔇 ➔ 🔇"
    * Show LG logo when turning off: ✘

## Brighter HDR Videos
Enabling full uncompressed HDR video typically resolves the issue.

!!! example "⚙ ➔ Picture ➔ Filmmaker mode (user settings)"
    * Brightness:
        * OLED Pixel Brightness: Energy saving
        * Adjust Contrast: **85**
        * Black Level: **50**
        * Auto Dynamic Contrast: **off**
        * Peak Brightness: **off**
        * Gamma: **2.2**
        * Video Range: **full**
        * Motion Eye Care: **off**
    * Color:
        * All: **Defaults**
    * Clarity:
        * Adjust Sharpness: **10**
        * Super Resolution: **off**
        * Noise Reduction: **off**
        * MPEG Noise Reduction: **off**
        * Smooth Gradation: **off**
        * Real Cinema: **off**
        * TruMotion: **off**

Both **Auto Dynamic Contrast** and **Peak Brightness** can be enabled for very
dark videos. These may lead to flickering between scenes as they auto-adjust
but may make a video watchable. Default to off and enable when needed.

Gamma: Keep on **2.2** which will pull out much more detail in shadows.
**BT.1886** will drastically increase brightness but
[wash out background detail][d].  **1.9** is brighter and only recommended when
2.2 does not look good.

[b]: https://old.reddit.com/r/LGOLED/comments/11m88an/disable_voice_recognition_for_good/?share_id=-JMhWX4cvVxMRoHjl9aN9
[c]: https://youtu.be/kA3_X1Zl2FI?si=hkFPX2q6hjfY6AbX&t=240
[d]: https://old.reddit.com/r/OLED/comments/u1qfeu/gamma_setting_22_vs_24_vs_bt_1886
