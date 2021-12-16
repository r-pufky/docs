.. _manajaro-kde-plasma-fonts:

Fonts
#####
Use custom fonts; set font tweaks if font display is not clean. KDE requires a
logout for the fonts to become active in the session or just import the fonts
manually in 'font management' after setup.

.. code-block:: bash
  :caption: Copy custom fonts to system

  cp fonts /usr/share/fonts

.. code-block:: bash
  :caption: **0644 root root** ``/etc/fonts/local.conf``

  <?xml version="1.0"?>
  <!DOCTYPE fontconfig SYSTEM "fonts.dtd">
  <fontconfig>
    <match target="font">
      <edit name="autohint" mode="assign">
        <bool>false</bool>
      </edit>
      <edit name="hinting" mode="assign">
        <bool>true</bool>
      </edit>
      <edit name="antialias" mode="assign">
        <bool>true</bool>
      </edit>
      <edit mode="assign" name="hintstyle">
        <const>hintslight</const>
      </edit>
      <edit mode="assign" name="rgba">
        <const>rgb</const>
      </edit>
      <edit mode="assign" name="lcdfilter">
        <const>lcddefault</const>
      </edit>
    </match>
  </fontconfig>

.. code-block:: bash
  :caption: **0644 user user** ``~/.Xresources``

  Xft.antialias: 1
  Xft.hinting: 1
  Xft.autohint: 0
  Xft.rgba: rgb
  Xft.hintstyle: hintslight
  Xft.lcdfilter: lcddefault

.. code-block:: bash
  :caption: Merge settings, link additional profiles, and update cache

  xrdb -merge ~/.Xresources
  ln -s /usr/share/fontconfig/conf.avail/10-sub-pixel-rgb.conf /etc/fonts/conf.d/
  ln -s /usr/share/fontconfig/conf.avail/11-lcdfilter-default.conf /etc/fonts/conf.d/
  fc-cache -f -v

`Reference <https://wiki.manjaro.org/index.php/Improve_Font_Rendering>`__
