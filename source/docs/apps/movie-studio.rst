.. _apps-movie-studio:

Movie Studio
############
`Steam Movie Studio 13 Platinum Release`_.

Encoding Templates
******************
Custom templates are saved to ``%appdata%\Sony\Render Templates``.

Templates below work well with shadowplay videos and youtube uploads.

.. dropdown:: AVC/135mbps/cuda/60
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Create a new template
    :path:    Project --> Make Movie --> Save it to my Hard Drive --> MP4 -->
              Advanced Options --> MainConcept AVC/AAC --> Customize Template
    :value0:  Template, AVC/135mbps/cuda/60
    :value1:     Notes, 135mbps @ 60fps using CUDA
    :update:  2021-04-03
    :label:   Create a new template
    :generic:
    :open:

  .. gui::    Video
    :path:    Customize Template --> Video
    :value2:                           ☑, Include video
    :value3:                  Frame size, (Custom Frame Size)
    :value4:                       Width, 2560
    :value5:                      Height, 1440
    :value6:                           ☐, Allow source to adjust frame size
    :value7:                     Profile, Main
    :value8:                  Frame rate, 60.000000
    :value9:                           ☑, Allow source to adjust frame rate
    :value10:                Field order, None (progressive scan)
    :value11:         Pixel aspect ratio, 1.0000
    :value12: Number of reference frames, 2
    :value13:                          ☐, Use deblocking filter
    :value14:                          ☑, Constant bit rate
    :value15:                          ›, 135000000
    :value16:           Number of slices, 4
    :value17:                Encode mode, Render using CUDA if available
    :value18:                          ☑, Enable progressive download
    :update:  2021-04-03
    :label:   Video
    :generic:
    :open:

  .. gui::    Audio
    :path:    Customize Template --> Audio
    :value0:                 ☑, Include audio
    :value1:  Sample rate (Hz), 48000
    :value2:    Bit rate (bps), 192000
    :update:  2021-04-03
    :label:   Audio
    :generic:
    :open:

  .. gui::    System
    :path:    Customize Template --> System
    :value0:  Format, MP4 file format (.mp4)
    :update:  2021-04-03
    :label:   System
    :generic:
    :open:

  .. gui::    Project
    :path:    Customize Template --> Project
    :value0:  Video rendering quality, Best
    :value1:      Sterescopic 3D mode, Use Project Settings
    :value2:                        ☐, Swap Left/Right
    :update:  2021-04-03
    :label:   Project
    :generic:
    :open:

.. dropdown:: AVC/135mbps/cuda
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Create a new template
    :path:    Project --> Make Movie --> Save it to my Hard Drive --> MP4 -->
              Advanced Options --> MainConcept AVC/AAC --> Customize Template
    :value0:  Template, AVC/135mbps/cuda
    :value1:     Notes, 135mbps @ 59.683fps using CUDA
    :update:  2021-04-03
    :label:   Create a new template
    :generic:
    :open:

  .. gui::    Video
    :path:    Customize Template --> Video
    :value2:                           ☑, Include video
    :value3:                  Frame size, (Custom Frame Size)
    :value4:                       Width, 2560
    :value5:                      Height, 1440
    :value6:                           ☐, Allow source to adjust frame size
    :value7:                     Profile, Main
    :value8:                  Frame rate, 59.683000
    :value9:                           ☑, Allow source to adjust frame rate
    :value10:                Field order, None (progressive scan)
    :value11:         Pixel aspect ratio, 1.0000
    :value12: Number of reference frames, 2
    :value13:                          ☐, Use deblocking filter
    :value14:                          ☑, Constant bit rate
    :value15:                          ›, 135000000
    :value16:           Number of slices, 4
    :value17:                Encode mode, Render using CUDA if available
    :value18:                          ☑, Enable progressive download
    :update:  2021-04-03
    :label:   Video
    :generic:
    :open:

  .. gui::    Audio
    :path:    Customize Template --> Audio
    :value0:                 ☑, Include audio
    :value1:  Sample rate (Hz), 48000
    :value2:    Bit rate (bps), 192000
    :update:  2021-04-03
    :label:   Audio
    :generic:
    :open:

  .. gui::    System
    :path:    Customize Template --> System
    :value0:  Format, MP4 file format (.mp4)
    :update:  2021-04-03
    :label:   System
    :generic:
    :open:

  .. gui::    Project
    :path:    Customize Template --> Project
    :value0:  Video rendering quality, Best
    :value1:      Sterescopic 3D mode, Use Project Settings
    :value2:                        ☐, Swap Left/Right
    :update:  2021-04-03
    :label:   Project
    :generic:
    :open:

.. dropdown:: AVC/50mbps/cuda
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Create a new template
    :path:    Project --> Make Movie --> Save it to my Hard Drive --> MP4 -->
              Advanced Options --> MainConcept AVC/AAC --> Customize Template
    :value0:  Template, AVC/50mbps/cuda
    :value1:     Notes, 50mbps @ 60fps using CUDA
    :update:  2021-04-03
    :label:   Create a new template
    :generic:
    :open:

  .. gui::    Video
    :path:    Customize Template --> Video
    :value2:                           ☑, Include video
    :value3:                  Frame size, (Custom Frame Size)
    :value4:                       Width, 2560
    :value5:                      Height, 1440
    :value6:                           ☐, Allow source to adjust frame size
    :value7:                     Profile, Main
    :value8:                  Frame rate, 60.000000
    :value9:                           ☑, Allow source to adjust frame rate
    :value10:                Field order, None (progressive scan)
    :value11:         Pixel aspect ratio, 1.0000
    :value12: Number of reference frames, 2
    :value13:                          ☐, Use deblocking filter
    :value14:                          ☑, Constant bit rate
    :value15:                          ›, 50000000
    :value16:           Number of slices, 4
    :value17:                Encode mode, Render using CUDA if available
    :value18:                          ☑, Enable progressive download
    :update:  2021-04-03
    :label:   Video
    :generic:
    :open:

  .. gui::    Audio
    :path:    Customize Template --> Audio
    :value0:                 ☑, Include audio
    :value1:  Sample rate (Hz), 48000
    :value2:    Bit rate (bps), 192000
    :update:  2021-04-03
    :label:   Audio
    :generic:
    :open:

  .. gui::    System
    :path:    Customize Template --> System
    :value0:  Format, MP4 file format (.mp4)
    :update:  2021-04-03
    :label:   System
    :generic:
    :open:

  .. gui::    Project
    :path:    Customize Template --> Project
    :value0:  Video rendering quality, Best
    :value1:      Sterescopic 3D mode, Use Project Settings
    :value2:                        ☐, Swap Left/Right
    :update:  2021-04-03
    :label:   Project
    :generic:
    :open:

.. dropdown:: AVC/50mbps
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Create a new template
    :path:    Project --> Make Movie --> Save it to my Hard Drive --> MP4 -->
              Advanced Options --> MainConcept AVC/AAC --> Customize Template
    :value0:  Template, AVC/50mbps
    :value1:     Notes, 50mbps @ 60fps using CPU
    :update:  2021-04-03
    :label:   Create a new template
    :generic:
    :open:

  .. gui::    Video
    :path:    Customize Template --> Video
    :value2:                           ☑, Include video
    :value3:                  Frame size, (Custom Frame Size)
    :value4:                       Width, 2560
    :value5:                      Height, 1440
    :value6:                           ☐, Allow source to adjust frame size
    :value7:                     Profile, Main
    :value8:                  Frame rate, 60.000000
    :value9:                           ☑, Allow source to adjust frame rate
    :value10:                Field order, None (progressive scan)
    :value11:         Pixel aspect ratio, 1.0000
    :value12: Number of reference frames, 2
    :value13:                          ☐, Use deblocking filter
    :value14:                          ☑, Constant bit rate
    :value15:                          ›, 50000000
    :value16:           Number of slices, 4
    :value17:                Encode mode, Render using CPU only
    :value18:                          ☑, Enable progressive download
    :update:  2021-04-03
    :label:   Video
    :generic:
    :open:

  .. gui::    Audio
    :path:    Customize Template --> Audio
    :value0:                 ☑, Include audio
    :value1:  Sample rate (Hz), 48000
    :value2:    Bit rate (bps), 192000
    :update:  2021-04-03
    :label:   Audio
    :generic:
    :open:

  .. gui::    System
    :path:    Customize Template --> System
    :value0:  Format, MP4 file format (.mp4)
    :update:  2021-04-03
    :label:   System
    :generic:
    :open:

  .. gui::    Project
    :path:    Customize Template --> Project
    :value0:  Video rendering quality, Best
    :value1:      Sterescopic 3D mode, Use Project Settings
    :value2:                        ☐, Swap Left/Right
    :update:  2021-04-03
    :label:   Project
    :generic:
    :open:

.. dropdown:: AVC
  :color: primary
  :icon: browser
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gui::    Create a new template
    :path:    Project --> Make Movie --> Save it to my Hard Drive --> MP4 -->
              Advanced Options --> MainConcept AVC/AAC --> Customize Template
    :value0:  Template, AVC
    :value1:     Notes, 12mbps VBR to 24mbps @ 60fps using CPU
    :update:  2021-04-03
    :label:   Create a new template
    :generic:
    :open:

  .. gui::    Video
    :path:    Customize Template --> Video
    :value2:                           ☑, Include video
    :value3:                  Frame size, (Custom Frame Size)
    :value4:                       Width, 2560
    :value5:                      Height, 1440
    :value6:                           ☐, Allow source to adjust frame size
    :value7:                     Profile, Main
    :value8:                  Frame rate, 60.000000
    :value9:                           ☑, Allow source to adjust frame rate
    :value10:                Field order, None (progressive scan)
    :value11:         Pixel aspect ratio, 1.0000
    :value12: Number of reference frames, 2
    :value13:                          ☐, Use deblocking filter
    :value14:                          ☑, Variable bit rate
    :value15:            › Maximum (bps), 24000000
    :value16:            › Average (bps), 12000000
    :value17:           Number of slices, 4
    :value18:                Encode mode, Render using CPU only
    :value19:                          ☑, Enable progressive download
    :update:  2021-04-03
    :label:   Video
    :generic:
    :open:

  .. gui::    Audio
    :path:    Customize Template --> Audio
    :value0:                 ☑, Include audio
    :value1:  Sample rate (Hz), 48000
    :value2:    Bit rate (bps), 192000
    :update:  2021-04-03
    :label:   Audio
    :generic:
    :open:

  .. gui::    System
    :path:    Customize Template --> System
    :value0:  Format, MP4 file format (.mp4)
    :update:  2021-04-03
    :label:   System
    :generic:
    :open:

  .. gui::    Project
    :path:    Customize Template --> Project
    :value0:  Video rendering quality, Best
    :value1:      Sterescopic 3D mode, Use Project Settings
    :value2:                        ☐, Swap Left/Right
    :update:  2021-04-03
    :label:   Project
    :generic:
    :open:

.. _Steam Movie Studio 13 Platinum Release: https://store.steampowered.com/sub/53361/
