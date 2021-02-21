.. _w10-20h2-settings-gaming-game-mode:

Game Mode
#########
.. dropdown:: Enable Game Mode  
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disables Windows updates while playing games. Game "performance" optimizes are
  minimal.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Removing ⌘ + g Prompt on Game Launch
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\GameBar
      :names:     AllowAutoGameMode,
                  AutoGameModeEnabled
      :types:     DWORD,
                  DWORD
      :data:      1,
                  1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/75936-turn-off-game-mode-windows-10-a.html>`__
