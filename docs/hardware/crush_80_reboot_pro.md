# [Crush 80 Reboot Pro][a]

## Update Firmware

1. Download and extract [firmware][b]
2. Unplug.
3. Hold **Fn+Esc** for **3** seconds to put in factory default state.
4. Unplug.
5. Remove caps lock key and toggle switch **off**.
4. Plugin (should immediately go into wired mode).
5. Run firmware update wait until **success** message.
6. Unplug keyboard, wait a few seconds, then plug it in. Ready for usevia.app.

## Keymapping
Use Chrome (browser must support WebHID) and download the specific keymap
definitions for the crush 80; this is required so usevia knows how to map
firmware functions in the webapp.

1. Download and extract [VIA keymap JSON configs][b].
2. Open [usevia.app](https://usevia.app).
3. Authorize device **RDR Crush 80** (it will not show up right away).
4. Design (paintbrush) ➔ Load Draft Definition ➔ Load all JSON definitions
   (the correct definition will autoload).
6. Keymapper (Device should now appear).
7. Change settings and apply.

## [Specific Keymaps][c]
After remapping remove the duplicate shortcuts.

Layer1

  Key    | Map                  | Purpose
 --------|----------------------|---------
  {KEY}  | **RGB_M_P**          | Solid RGB Toggle.
  print  | **LED system power** | Power LED Toggle.
  scroll | **LED logo power**   | Logo LED Toggle.
  pause  | **LED side power**   | Side LED Toggle.
  insert | **saturation+**      | Increase saturation.
  delete | **saturation-**      | Decrease saturation.
  home   | **hue+**             | Increase hue
  end    | **hue-**             | Decrease hue
  pgup   | **brightness+**      | Increase brightness.
  pgdn   | **brightness-**      | Decrease brightness.

[a]: https://www.wobkey.com/collections/all/products/crush-80-reboot
[b]: https://www.wobkey.com/pages/support-for-crush-80
[c]: https://old.reddit.com/r/keyboards/comments/1m2had9/rgb_issue_with_crush_80/
