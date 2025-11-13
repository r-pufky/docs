# Movie Studio
[Steam Movie Studio 13 Platinum Release][a].


## Encoding Templates
Templates below work well with shadowplay videos and youtube uploads.

Custom templates are saved to **%appdata%\Sony\Render Templates**.


### AVC/135mbps/cuda/60
!!! example "Project ➔ Make Movie ➔ Save it to my Hard Drive ➔ MP4 ➔ Advanced Options ➔ MainConcept AVC/AAC ➔ Customize Template"
    * Template: **AVC/135mbps/cuda/60**
    * Notes: **135mbps @ 60fps using CUDA**

!!! example "Customize Template ➔ Video"
    * Frame rate: **60.000000**
    * Allow source to adjust frame rate: ✘
    * Constant bit rate: ✔
        * **135000000**
    * Encode mode: **Render using CUDA if available**

### AVC/135mbps/cuda
!!! example "Project ➔ Make Movie ➔ Save it to my Hard Drive ➔ MP4 ➔ Advanced Options ➔ MainConcept AVC/AAC ➔ Customize Template"
    * Template: **AVC/135mbps/cuda**
    * Notes: **135mbps @ 59.683fps using CUDA**

!!! example "Template ➔ Video"
    * Frame rate: **59.683000**
    * Allow source to adjust frame rate: ✔
    * Constant bit rate: ✔
        * **135000000**
    * Encode mode: **Render using CUDA if available**

### AVC/50mbps/cuda
!!! example "Project ➔ Make Movie ➔ Save it to my Hard Drive ➔ MP4 ➔ Advanced Options ➔ MainConcept AVC/AAC ➔ Customize Template"
    * Template: **AVC/50mbps/cuda**
    * Notes: **50mbps @ 60fps using CUDA**

!!! example "Template ➔ Video"
    * Frame rate: **60.000000**
    * Allow source to adjust frame rate: ✔
    * Constant bit rate: ✔
        * **50000000**
    * Encode mode: **Render using CUDA if available**

### AVC/50mbps
!!! example "Project ➔ Make Movie ➔ Save it to my Hard Drive ➔ MP4 ➔ Advanced Options ➔ MainConcept AVC/AAC ➔ Customize Template"
    * Template: **AVC/50mbps**
    * Notes: **50mbps @ 60fps using CPU**

!!! example "Template ➔ Video"
    * Frame rate: **60.000000**
    * Allow source to adjust frame rate: ✔
    * Constant bit rate: ✔
        * **50000000**
    * Encode mode: **Render using CPU only**

### AVC
!!! example "Project ➔ Make Movie ➔ Save it to my Hard Drive ➔ MP4 ➔ Advanced Options ➔ MainConcept AVC/AAC ➔ Customize Template"
    * Template: **AVC**
    * Notes: **12mbps VBR to 24mbps @ 60fps using CPU**

!!! example "Template ➔ Video"
    * Frame rate: **60.000000**
    * Allow source to adjust frame rate: ✔
    * Variable bit rate: ✔
        * Maximum (bps): **24000000**
        * Average (bps): **12000000**
    * Encode mode: **Render using CPU only**

### All profiles
All profiles use these settings.

!!! example "Customize Template ➔ Video"
    * Include video: ✔
    * Frame size: **Custom Frame Size**
    * Width: **2560**
    * Height: **1440**
    * Allow source to adjust frame size: ✘
    * Profile: **Main**
    * Field order: **None (progressive scan)**
    * Pixel aspect ratio: **1.0000**
    * Number of reference frames: **2**
    * Use deblocking filter: ✘
    * Number of slices: **4**
    * Enable progressive download: ✔

!!! example "Customize Template ➔ Audio"
    * Include audio: ✔
    * Sample rate (Hz): **48000**
    * Bit rate (bps): **192000**

!!! example "Customize Template ➔ System"
    * Format: **MP4 file format (.mp4)**

!!! example "Customize Template ➔ Project"
    * Video rendering quality: **Best**
    * Sterescopic 3D mode: **Use Project Settings**
    * Swap Left/Right: ✘

[a]: https://store.steampowered.com/sub/53361
