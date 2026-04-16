import decman
from decman.plugins import pacman, aur, systemd

from hyprland.base import HyprlandModule


class GamingModule(decman.Module):
    """
    Gaming: Steam, Proton, emulation suite, and gaming utilities.
    Requires HyprlandModule for the display stack.
    """

    user: str

    def __init__(self, user):
        super().__init__("gaming")
        self.user = user
        decman.modules.append(HyprlandModule(self.user))

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            # Steam (enable multilib in pacman.conf first)
            "steam",
            # Proton / Wine dependencies
            "wine",
            "wine-mono",
            "wine-gecko",
            "winetricks",
            "lib32-mesa",
            "lib32-vulkan-icd-loader",
            "vulkan-tools",
            # Gaming utilities
            "gamemode",
            "lib32-gamemode",
            # "mangohud",  # in-game overlay
            # "lib32-mangohud",
            # Emulation - cores
            "retroarch",
            "retroarch-assets-xmb",
            # "libretro-beetle-psx-hw",  # PS1
            # "libretro-dolphin",  # GC / Wii
            # "libretro-mgba",  # GBA
            # "libretro-snes9x",  # SNES
            # Browser
            "chromium",
            "xdg-utils",
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return {
            "google-chrome",  # comment out if you prefer chromium above
            "protonup-qt",  # Proton-GE manager
            # "heroic-games-launcher-bin",  # Epic / GOG launcher
            "bottles",  # Wine prefix manager
            # "ryujinx",  # Nintendo Switch emulator
            # "rpcs3-git",  # PS3 emulator
            # "lutris",  # unified game launcher
            # Controller support
            "game-devices-udev",
            "xboxdrv",
        }

    @systemd.units
    def units(self) -> set[str]:
        return {"bluetooth.service"}
