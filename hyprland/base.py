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
            # Terminal (Ghostty - see AUR below)
            # Fonts & theming
            # "noto-fonts",
            # "noto-fonts-emoji",
            # "ttf-jetbrains-mono-nerd",
            # "ttf-font-awesome",
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
        return {
            # "ghostty-git",  # GPU-accelerated terminal
        }

    @systemd.units
    def units(self) -> set[str]:
        return {"greetd.service"}
