# [Selkies][a]
Open-Source Low-Latency Accelerated Linux WebRTC HTML5 Remote Desktop Streaming
Platform for Self-Hosting, Containers, Kubernetes, or Cloud/HPC.

Google Stadia, GeForce NOW, Moonlight, and other platforms use this to stream
60fps+ FullHD over HTML5.

## Install
=== "CachyOS"

    ``` bash
    # Base dependencies.
    pacman -S --needed jq curl tar gzip libpulse wayland-protocols
    pacman -S --needed libwayland libx11 xorg-server-xvfb xorg-xinit
    pacman -S --needed xorg-xkb-utils xorg-xserver-utils xorg-xwd
    pacman -S --needed libxcb xkblibcommon libxdamage libxfixes libxv
    pacman -S --needed libxtst libxext mesa-utils gstreamer
    pacman -S --needed gst-plugins-base gst-plugins-good gst-plugins-bad
    pacman -S --needed gst-libav python-pip python-gobject gst-plugins-ugly

    # Nvidia Hardware.
    pacman -S --needed nvidia-utils
    # AMD/Intel Hardware.
    pacman -S --needed libva-mesa-driver intel-media-driver
    ```

=== "Debian"

    ``` bash
    # Base depedencies.
    apt install jq tar gzip ca-certificates curl libpulse0 wayland-protocols
    apt install xserver-xorg-core libwayland-dev libwayland-egl1 xvfb
    apt install  x11-utils x11-xkb-utils x11-xserver-utils
    ```


``` bash
export SELKIES_VERSION=$(curl -fsSL "https://api.github.com/repos/selkies-project/selkies-gstreamer/releases/latest" | jq -r '.tag_name' | sed 's/[^0-9.\-]*//g')
# Create a directory and download
mkdir -p /opt/selkies && cd /opt/selkies
curl -fsSL "https://github.com/selkies-project/selkies-gstreamer/releases/download/v${SELKIES_VERSION}/selkies-gstreamer-portable-v${SELKIES_VERSION}_amd64.tar.gz" | tar -xz
```

## Streaming
Stream can be started from an unprivileged user on unprivileged containers (and
can include GPU acceleration if GPU/iGPU devices have been passthrough).

Stream should be encrypted with HTTPS or tunneled through SSH; most features
such as clipboard and microphones require encrypted connections.

## Stream Specific Application

!!! abstract "~/.local/bin/stream_digikam"
    0755 {USER}:{USER}

    ``` bash
    #!/bin/bash
    #
    # Stream Digikam on port 8080.
    export DISPLAY=:99
    xvfb :99 -screen 0 1920x1080x24 & sleep 2

    digikam &

    # Stream the exported display over selkies.
    /opt/selkies/selkies-gstreamer-run \
        --addr=0.0.0.0 \
        --port=8080 \
        --enable_https=false \
        --basic_auth_user={USER} \
        --basic_auth_password={PASSWORD} \
        --encoder=x264enc  #  Nvidia shoud use nvh264enc.
    ```

## Stream KDE Desktop

!!! abstract "~/.local/bin/stream_kde"
    0755 {USER}:{USER}

    ```
    #!/bin/bash
    #
    # Launch KDE and stream the desktop session over port 8080.

    export DISPLAY_ID=":99"
    export RESOLUTION="1920x1080x24"
    export SELKIES_PORT=8080
    export SELKIES_ENCODER="nvh264enc" # Use vhap264enc for AMD/Intel or x264enc for CPU
    export SELKIES_PATH="/opt/selkies"

    echo "Cleaning up display locks..." && rm -f /tmp/.X${DISPLAY_ID#*:}-lock

    echo "Starting Virtual Display on $DISPLAY_ID..."
    Xvfb ${DISPLAY_ID} -screen 0 ${RESOLUTION} +extension RANDR +extension GLX +extension MIT-SHM & sleep 2

    export DISPLAY=${DISPLAY_ID}

    # Start dbus-run-session to ensure KDE has its own message bus.
    echo "Starting KDE Plasma..."
    dbus-run-session startplasma-x11 > /dev/null 2>&1 &
    sleep 5

    # Stream the exported display over selkies
    if [ -d "${SELKIES_PATH}" ]; then
        echo "Launching Selkies on port ${SELKIES_PORT}..."
        ${SELKIES_PATH}/selkies-gstreamer-run \
            --addr=0.0.0.0 \
            --port=${SELKIES_PORT} \
            --encoder=${SELKIES_ENCODER} \
            --enable_resize=true \
            --uinput_mouse=true \
            --uinput_keyboard=true
    else
        echo "Error: Selkies directory not found at ${SELKIES_PATH}"
        exit 1
    fi
    ```

[a]: https://github.com/selkies-project/selkies
