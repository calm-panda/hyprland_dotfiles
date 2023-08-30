#! /bin/bash

eww daemon &
eww open-many bar greet &
eww update is-mute=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -d ' ' -f3) &
eww update volume=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -d ' ' -f2) &
eww update brightness=$(brillo -G) &
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP &
swaybg -i ~/Pictures/Wallp/image.png &
udiskie &
