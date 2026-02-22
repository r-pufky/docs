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

1. Download and extract [VIA keymap JSON configs][b].
2. Open VIA:
    * Windows: [usevia.app](https://usevia.app) with Chrome.
    * Linux: `paru -S via-bin`
3. Authorize device **RDR Crush 80** (it will not show up right away).
4. Design (paintbrush) ➔ Load Draft Definition ➔ Load all JSON definitions
   (the correct definition will autoload).
5. Keymapper (Device should now appear).
6. Change settings and apply.


## [Specific Keymaps][c]
After remapping remove the duplicate shortcuts.

### Layer 0

  Key       | Map         | Name      | Purpose
 -----------|-------------|-----------|---------
  Caps Lock | **KC_LCTL** | Left Ctrl | Capslock as control.
  *         | **F24**     | F24       | User key with no window manager interaction.

### Layer 1
Momentary toggle with **Fn** key.

  Key           | Map            | Name             | Purpose
 ---------------|----------------|------------------|---------
  *             | **F24**        | F24              | User key with no window manager interaction.
  /             | **RGB_M_P**    | RGB MODE P       | Solid RGB Toggle.
  Backspace     | **RGB_TOG**    | RGB TOGGLE       | Turn on/off RGB.
  Left Bracket  | **CUSTOM(7)**  | LED LOGO MODE    | Cycle logo RGB effect.
  Right Bracket | **CUSTOM(7)**  | LED LOGO COLOR   | Cycle logo color.
  \             | **RGB_MOD**    | RGB MODE +       | Cycle through RGB modes.
  ;             | **CUSTOM(10)** | LED SIDE MODE    | Cycle side LED mode.
  '             | **CUSTOM(11)** | LED SIDE COLOR   | Cycle side LED color.
  Caps Lock     | **KC_CAPS**    | Caps Lock        | Caps lock toggle on function layer.
  print         | **CUSTOM(14)** | LED SYSTEM POWER | Power LED Toggle.
  scroll        | **CUSTOM(9)**  | LED LOGO POWER   | Logo LED Toggle.
  pause         | **CUSTOM(12)** | LED SIDE POWER   | Side LED Toggle.
  insert        | **RGB_VAI**    | BRIGHT +         | Increase brightness.
  delete        | **RGB_VAD**    | BRIGHT -         | Decrease brightness.
  home          | **RGB_SAI**    | SAT +            | Increase saturation.
  end           | **RGB_SAD**    | SAT -            | Decrease saturation.
  pgup          | **RGB_HUI**    | HUE +            | Increase hue.
  pgdn          | **RGB_HUD**    | HUE -            | Decrease hue.
  ↑             | **RGB_VAI**    | BRIGHT +         | Increase brightness.
  ↓             | **RGB_VAD**    | BRIGHT -         | Decrease brightness.
  →             | **RGB_SPI**    | EFFECT SPEED +   | Increase RGB effect speed.
  ←             | **RGB_SPD**    | EFFECT SPEED -   | Decrease RGB effect speed.

### Layer 3

  Key       | Map         | Name      | Purpose
 -----------|-------------|-----------|---------
  *         | **F24**     | F24       | User key with no window manager interaction.

### Layer 4

  Key       | Map         | Name      | Purpose
 -----------|-------------|-----------|---------
  *         | **F24**     | F24       | User key with no window manager interaction.

[a]: https://www.wobkey.com/collections/all/products/crush-80-reboot
[b]: https://www.wobkey.com/pages/support-for-crush-80
[c]: https://old.reddit.com/r/keyboards/comments/1m2had9/rgb_issue_with_crush_80/
