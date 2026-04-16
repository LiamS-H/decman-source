import decman
from decman.plugins import aur, pacman, systemd


class AudioModule(decman.Module):
    def __init__(self):
        super().__init__("audio")

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            "pipewire",
            "pipewire-alsa",
            "pipewire-pulse",
            "pipewire-jack",
            "wireplumber",
        }

    @aur.packages
    def aurpkgs(self) -> set[str]:
        return {"decman"}
