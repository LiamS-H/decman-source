import decman
from decman.plugins import aur, pacman, systemd


class AudioModule(decman.Module):
    def __init__(self):
        super().__init__("audio")

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            "sof-firmware",
            "playerctl",
            "pipewire",
            "pipewire-alsa",
            "pipewire-pulse",
            "pipewire-jack",
            "wireplumber",
            "pavucontrol",
        }

    @aur.packages
    def aurpkgs(self) -> set[str]:
        return {"decman"}

    @systemd.units
    def units(self) -> set[str]:
        return {
            "pipewire.socket",
            "pipewire-pulse.socket",
            "wireplumber.service"
        }
