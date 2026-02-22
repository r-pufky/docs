# Shield TV


## Fix Black Screen & Launcher Crashes
The default launcher crashes, black screens consistently, and injects Ads to
the home screen. Use an alternative launcher to resolve these issues.

### Install [Projectivity Launcher][a]
If you like this launcher please support the author.

!!! example "Projectivity ➔ Accessibility ➔ Settings ➔ [Override Launcher][b]: ✔"

Change [category orders][c] by moving all the way left in the desired row and
using ↑ ↓ arrows.

### Enable Developer Mode
!!! example "⚙ ➔ Device Preferences ➔ About ➔ Build"
    Click **7** times to enable developer mode.

!!! example "⚙ ➔ Developer Options ➔ Remote Debugging: ✔"
    This may also be called 'wireless debugging'.

### [Disable Built-in Launcher][d]

``` bash
# Alternatively configure package from reference.
pamac install android-tools

adb connect {SHIELD_IP}  # Accept connection on shield.

# Disable launcher.
adb shell pm disable-user --user 0 com.google.android.tvlauncher

# Re-enable launcher.
# adb shell pm enable com.google.android.tvlauncher
```

!!! example "⚙ ➔ Developer Options ➔ Remote Debugging: ✘"
    This may also be called 'wireless debugging'.


## [Disable Google Voice Button][e]
!!! example "⚙ ➔ Settings ➔ Apps ➔ App Permissions ➔ Microphone ➔ Show System Apps"
    * Google: **Don't Allow**

    Press the Voice Assistant button and **Deny**, **Never ask again** when
    prompted. Remap

Button may be remapped to other functions with [Button Mapper][f].


## Reference[^1][^2]

[^1]: https://www.reddit.com/r/ShieldAndroidTV/comments/ssbtmi/a_short_guide_on_how_to_get_rid_of_ads_while
[^2]: https://www.nvidia.com/en-us/geforce/forums/legacy-products/12/173396/rooting-your-shield-the-why-and-how

[a]: https://play.google.com/store/apps/details?id=com.spocky.projengmenu
[b]: https://old.reddit.com/r/ShieldAndroidTV/comments/17sfi7w/projectivity_launcher_question
[c]: https://old.reddit.com/r/AndroidTV/comments/159sapb/projectivy_launcher_change_catagory_order
[d]: https://developer.android.com/tools/releases/platform-tools
[e]: https://old.reddit.com/r/nvidiashield/comments/1hy8ali/solution_disabling_google_voice_assistant_button
[f]: https://play.google.com/store/apps/details?id=flar2.homebutton&hl=en_US