# WebOS
Smart TV Asshattery.

!!! danger
    **Always** hard block WebOS with firewall rules and [Destination NAT][a].

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

[a]: ../networking/edge_os/README.md#add-a-destination-nat-rule
[b]: https://old.reddit.com/r/LGOLED/comments/11m88an/disable_voice_recognition_for_good/?share_id=-JMhWX4cvVxMRoHjl9aN9
