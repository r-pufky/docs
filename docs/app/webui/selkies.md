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

    # If using full KDE Desktop.
    sudo pacman -S plasma
    ```

=== "Debian"

    ``` bash
    # Base dependencies.
    apt install jq tar gzip ca-certificates curl libpulse0 wayland-protocols
    apt install xserver-xorg-core libwayland-dev libwayland-egl1 xvfb
    apt install x11-utils x11-xkb-utils x11-xserver-utils

    # If using full KDE Desktop.
    apt install kde-plasma-desktop
    ```

``` bash
export SELKIES_VERSION=$(curl -fsSL "https://api.github.com/repos/selkies-project/selkies-gstreamer/releases/latest" | jq -r '.tag_name' | sed 's/[^0-9.\-]*//g')
# Create a directory and download
mkdir -p /opt/selkies && cd /opt/selkies
curl -fsSL "https://github.com/selkies-project/selkies-gstreamer/releases/download/v${SELKIES_VERSION}/selkies-gstreamer-portable-v${SELKIES_VERSION}_amd64.tar.gz" | tar -xz
```

## Streaming
Start UDP stream from an unprivileged user on unprivileged containers.

!!! warning "Setup assumes encrypted tunnels"
    Scripts below assume encrypted tunnels. If Directly exposing to the
    Internet (not recommended) both authentication and encryption should be
    enabled by default.

!!! tip "Encrypted Connections Preferred"
    Most features such as clipboard and microphones will be disabled
    automatically if encrypted transports are not used. Basic auth default
    values are the running **user** and **mypasswd**. Selkies uses **UDP**.

## Stream KDE Desktop
KDE with Audio desktop session requires a shared DBUS so the process can
communicate. See [PVE Audio Passthrough](../../os/pve/audio.md).

!!! tip "Audio Should Appear Un-muted"
    Audio will be un-muted, and audio settings will display 'Virtual-Speaker'.

    Audio device in KDE will report no audio devices found as these are not
    mapped. Audio will still work through streaming.

!!! abstract "~/.local/bin/start_plasma_session"
    0755 {USER}:{USER}

    ``` bash
    #!/bin/bash
    #
    # Launch KDE, pipewire, wireplumber using the same DBUS, and create an virtual
    # audio device.

    pipewire & sleep 1
    wireplumber & sleep 1
    pipewire-pulse & sleep 2

    pactl load-module module-null-sink \
        sink_name=remote \
        sink_properties=device.description="Virtual-Speaker"
    pactl set-default-sink remote

    startplasma-x11
    ```

!!! abstract "~/.local/bin/stream_kde"
    0755 {USER}:{USER}

    ```
    #!/bin/bash
    #
    # Launch KDE and stream the desktop session.

    export DISPLAY_ID=":99"
    export RESOLUTION="2560x1440x24"
    export SELKIES_ADDR='0.0.0.0'
    export SELKIES_PORT=5555
    export SELKIES_ENCODER="x264enc" # Nvidia: nvh264enc, AMD/Intel: vhap264enc
    export SELKIES_PATH="/opt/selkies/selkies-gstreamer"

    unset DBUS_SESSION_BUS_ADDRESS
    unset DBUS_SESSION_BUS_PID
    export XDG_RUNTIME_DIR="/tmp/runtime-$(whoami)"
    mkdir -p $XDG_RUNTIME_DIR
    chmod 700 $XDG_RUNTIME_DIR

    pkill -x "Xvfb"
    pkill -u $(whoami) pipewire
    pkill -u $(whoami) wireplumber
    pkill -u $(whoami) dbus-daemon
    rm -f /tmp/.X${DISPLAY_ID#*:}-lock

    Xvfb ${DISPLAY_ID} -screen 0 ${RESOLUTION} +extension RANDR +extension GLX +extension MIT-SHM &
    sleep 2
    export DISPLAY=${DISPLAY_ID}

    echo "Starting Plasma & DBUS session..."
    dbus-run-session $(dirname $(realpath -s $0))/start_plasma_session > /dev/null 2>&1 &
    sleep 10

    if pgrep -f "selkies-gstreamer-run" > /dev/null; then
        echo "Selkies is already running. Skipping launch."
    else
        if [ -d "${SELKIES_PATH}" ]; then
            echo "Launching Selkies on port ${SELKIES_PORT}..."
    	    export PULSE_SERVER="unix:${XDG_RUNTIME_DIR}/pulse/native"
            ${SELKIES_PATH}/selkies-gstreamer-run \
                --addr=${SELKIES_ADDR} \
                --port=${SELKIES_PORT} \
                --encoder=${SELKIES_ENCODER} \
    	    --enable_basic_auth=false \
    	    --enable_clipboard=true \
                --enable_resize=true
        else
            echo "Error: Selkies directory not found at ${SELKIES_PATH}"
            exit 1
        fi
    fi
    ```

## Stream Specific Application
Quick and dirty for just streaming a specific application. Prefer
[Stream KDE Desktop](#stream-kde-desktop).

!!! abstract "~/.local/bin/stream_digikam"
    0755 {USER}:{USER}

    ``` bash
    #!/bin/bash
    #
    # Stream Digikam on port 8080.
    export DISPLAY=:99
    Xvfb :99 -screen 0 1920x1080x24 & sleep 2

    digikam &

    # Stream the exported display over selkies.
    /opt/selkies/selkies-gstreamer-run \
        --addr=0.0.0.0 \
        --port=8080 \
        --enable_https=false \
        --enable_basic_auth=false \
        --enable_clipboard=true \
        --encoder=x264enc  #  Nvidia shoud use nvh264enc.
    ```

[a]: https://github.com/selkies-project/selkies
