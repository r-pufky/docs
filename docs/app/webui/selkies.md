# [Selkies][a]
Open-Source Low-Latency Accelerated Linux WebRTC HTML5 Remote Desktop Streaming
Platform for Self-Hosting, Containers, Kubernetes, or Cloud/HPC. Google Stadia,
GeForce NOW, Moonlight, and other platforms use this to stream 60fps+ FullHD
over HTML5.

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
    apt install x11-utils x11-xkb-utils x11-xserver-utils ssl-cert

    # If using full KDE Desktop.
    apt install kde-plasma-desktop

    # If using snakeoil certs.
    usermod -a -G ssl-cert $(whoami)
    ```

``` bash
export SELKIES_VERSION=$(curl -fsSL "https://api.github.com/repos/selkies-project/selkies-gstreamer/releases/latest" | jq -r '.tag_name' | sed 's/[^0-9.\-]*//g')
# Create a directory and download
mkdir -p /opt/selkies && cd /opt/selkies
curl -fsSL "https://github.com/selkies-project/selkies-gstreamer/releases/download/v${SELKIES_VERSION}/selkies-gstreamer-portable-v${SELKIES_VERSION}_amd64.tar.gz" | tar -xz
```

## Streaming
Start **UDP** stream from an unprivileged user on unprivileged containers.
There are many configuration options not included here, including [hardware
encoder support for GPU's and Audio][b].

!!! warning "Use Encryption & Authentication"
    Most features such as clipboard and microphones are disabled if encrypted
    transports are not used. **Only** directly expose to Internet when both
    encryption and authentication are enabled. It does [not incur][e]
    additional overhead.

    Use **Chrome** if clipboard is required. Firefox has not implemented the
    permissions API and [enabling async clipboard][d] is a massive security
    risk.

!!! tip "Basic Auth Defaults"
    Default basic auth options are **{USER}**:**mypasswd**.

### Headless KDE Desktop Stream with Audio
Use a user systemd unit to manage private DBUS for KDE and Audio devices during
the process lifecycle. A shared DBUS is required for the processes to
communicate. See [PVE Audio Passthrough](../../os/pve/audio.md).

!!! tip "Audio Should Appear Un-muted"
    Audio will be un-muted and audio settings will display **Virtual-Speaker**.

    Audio device in KDE will report no audio devices found as these are not
    mapped. Audio will still work through streaming.

#### User Configuration
User must be configured for [Systemd User Environments][c].

``` bash
# Enable service lingering for user.
sudo loginctl enable-linger {USER}

# Export required user systemd unit environment for configuration.
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"

# Disable auto-start of user services, manage in systemd unit.
systemctl --user stop pulseaudio.socket pulseaudio.service pipewire-pulse.socket pipewire-pulse.service
systemctl --user disable pulseaudio.socket pulseaudio.service pipewire-pulse.socket pipewire-pulse.service
systemctl --user mask pulseaudio.socket pulseaudio.service pipewire-pulse.socket pipewire-pulse.service
```

#### Service
Service is isolated per-user enabling a KDE session for each user configured.

!!! abstract "~/.local/bin/stream_kde"
    0755 {USER}:{USER}

    ``` bash
    #!/bin/bash
    #
    # Create a streaming KDE desktop instance with a private DBUS.
    #
    # Additional Selkies options:
    # * https://github.com/selkies-project/selkies/tree/main/src

    export DISPLAY=':99'
    export RESOLUTION='2560x1440x24'
    export SELKIES_ADDR='0.0.0.0'
    export SELKIES_PORT=5555
    export SELKIES_ENCODER='x264enc'
    export SELKIES_ENABLE_HTTPS='true'
    export SELKIES_HTTPS_CERT='/etc/ssl/certs/ssl-cert-snakeoil.pem'
    export SELKIES_HTTPS_KEY='/etc/ssl/private/ssl-cert-snakeoil.key'
    export SELKIES_BASIC_AUTH='false'
    export SELKIES_CLIPBOARD='true'
    export SELKIES_RESIZE='true'
    export SELKIES_PATH='/opt/selkies/selkies-gstreamer'

    export XDG_RUNTIME_DIR="/run/user/$(id -u)"
    export PULSE_SERVER="unix:${XDG_RUNTIME_DIR}/pulse/native"

    SESSION_PROCS='pipewire|pipewire-pulse|wireplumber|Xvfb|startplasma-x11'

    pkill -u $(whoami) -x "${SESSION_PROCS}"
    rm -f ${XDG_RUNTIME_DIR}/pipewire-0*
    rm -rf ${XDG_RUNTIME_DIR}/pulse
    rm -f /tmp/.X${DISPLAY#*:}-lock

    mkdir -p ${XDG_RUNTIME_DIR}/pulse
    Xvfb ${DISPLAY} -screen 0 ${RESOLUTION} \
        +extension RANDR \
        +extension GLX \
        +extension MIT-SHM &
    sleep 2

    # Create background private DBUS and use systemd control group to stop.
    dbus-run-session bash -c "
        pipewire & sleep 1;
        wireplumber & sleep 1;
        pipewire-pulse & sleep 2;
        pactl load-module module-null-sink sink_name=remote \
            sink_properties=device.description='Virtual-Speaker';
        pactl set-default-sink remote;
        startplasma-x11
    " &

    sleep 5

    if [ -d "${SELKIES_PATH}" ]; then
        ${SELKIES_PATH}/selkies-gstreamer-run \
            --addr=${SELKIES_ADDR} \
            --port=${SELKIES_PORT} \
            --encoder=${SELKIES_ENCODER} \
	        --enable_https=${SELKIES_ENABLE_HTTPS} \
	        --https_cert=${SELKIES_HTTPS_CERT} \
 	        --https_key=${SELKIES_HTTPS_KEY} \
            --enable_basic_auth=${SELKIES_BASIC_AUTH} \
            --enable_clipboard=${SELKIES_CLIPBOARD} \
            --enable_resize=${SELKIES_RESIZE}
    else
        echo "Selkies not found!"
        exit 1
    fi
    ```

!!! abstract "~/.config/systemd/user/stream_kde.service"
    0644 {USER}:{USER}

    ``` bash
    [Unit]
    Description=KDE Headless Streaming Session.
    After=network.target

    [Service]
    Type=simple
    ExecStart=%h/.local/bin/stream_kde
    Restart=always
    RestartSec=5

    # Kill everything in the control group when stopping.
    KillMode=mixed

    [Install]
    WantedBy=default.target
    ```

``` bash
systemctl --user daemon-reload
systemctl --user enable stream_kde
systemctl --user start stream_kde
```

### Stream Specific Application
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
        --encoder=x264enc  #  Nvidia should use nvh264enc.
    ```

## Troubleshooting

### Window appears with scrollbar or two pages
Canvas size is not properly detected. Typically this occurs when the bookmarks
bar is visible and the canvas size is not adjusted (common for chrome).

Hide bookmarks bar and refresh.

[a]: https://github.com/selkies-project/selkies
[b]: https://github.com/selkies-project/selkies/blob/main/docs/component.md#encoders
[c]: ../../service/systemd/README.md
[d]: ../gui/firefox.md#enable-async-clipboard
[e]: https://www.imperialviolet.org/2010/06/25/overclocking-ssl.html
