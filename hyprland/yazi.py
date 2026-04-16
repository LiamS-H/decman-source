import decman
from decman.plugins import aur, pacman, systemd


class YaziModule(decman.Module):
    def __init__(self):
        super().__init__("yazi")

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            "yazi",
            "ffmpeg",
            "7zip",
            "jq",
            "poppler",
            "fd",
            "ripgrep",
            "fzf",
            "zoxide",
            "resvg",
            "imagemagick",
        }

    @aur.packages
    def aurpkgs(self) -> set[str]:
        return {"decman"}
