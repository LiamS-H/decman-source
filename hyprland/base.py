import decman
from decman import File, Directory
from decman.plugins import pacman, aur, systemd
from hyprland.yazi import YaziModule


class HyprlandModule(decman.Module):
    """
    Hyprland Wayland compositor stack.
    Shared between 'dev' and 'gaming' users.
    """

    user: str

    def __init__(self, user):
        self.user = user
        super().__init__("hyprland")
        decman.modules.append(YaziModule())
        decman.directories[f"/home/{self.user}/.config/hypr"] = Directory (
            source_directory="./hyprland/hypr",
            bin_files=False,
            encoding="utf-8",
            owner=self.user,
            permissions=0o600,
        )

        decman.directories[f"/home/{self.user}/.config/waybar"] = Directory (
            source_directory="./hyprland/waybar",
            bin_files=False,
            encoding="utf-8",
            owner=self.user,
            permissions=0o600,
        )

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            # Wayland / Hyprland
            "hyprland",
            "hyprpaper",  # wallpaper
            "hypridle",  # idle daemon
            "hyprlock",  # lock screen
            "xdg-desktop-portal-hyprland",
            "xdg-user-dirs",
            # Display / GPU
            "wayland",
            "wayland-protocols",
            "qt5-wayland",
            "qt6-wayland",
            # Status bar
            "waybar",

            # App launcher
            "wofi",
            # Notifications
            "mako",
            # Clipboard
            "wl-clipboard",
            "cliphist",
            # Screenshots
            "grim",
            "slurp",
            "swappy",
            # File manager
            "thunar",
            "tumbler",
            # Polkit
            "polkit-gnome",
            # GTK theming
            "nwg-look",
            # Display manager
            "greetd",
            # Screenshot helper
            "hyprshot",
            "greetd-tuigreet",  # TUI greeter for greetd
            # Terminal
            "yazi",
            "ghostty",
            # File System
        }

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        return set()

    @systemd.units
    def units(self) -> set[str]:
        return set()

    def files(self) -> dict[str, decman.File]:
        return {
            "/usr/share/wayland-sessions/hyprland.desktop": decman.File(
                source_file="./files/usr/share/wayland-sessions/hyprland.desktop"
            ),
        }

