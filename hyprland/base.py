import decman
from decman.plugins import pacman, aur, systemd


class HyprlandModule(decman.Module):
    """
    Hyprland Wayland compositor stack.
    Shared between 'dev' and 'gaming' users.
    """

    user: str

    def __init__(self, user):
        self.user = user
        super().__init__("hyprland")

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
            "ghostty",
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
