import decman
from decman.plugins import aur, pacman, systemd


class BaseModule(decman.Module):
    def __init__(self):
        super().__init__("base")

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            # Base system
            "base",
            "base-devel",
            "linux",
            "linux-firmware",
            "linux-headers",
            "intel-ucode",  # for intel processors
            # Location
            "geoclue",
            # Filesystem tools
            "btrfs-progs",
            "dosfstools",
            "e2fsprogs",
            # Network
            "networkmanager",
            "network-manager-applet",
            "openssh",
            "bluez",
            "bluez-utils",
            # Brightness
            "brightnessctl",
            # System utilities
            "sudo",
            "git",
            "curl",
            "wget",
            "htop",
            "man-db",
            "man-pages",
            "unzip",
            "zip",
            "tar",
            "rsync",
            "which",
            "ufw",
        }

    @aur.packages
    def aurpkgs(self) -> set[str]:
        return {
            "decman",
            "automatic-timezoned",
        }

    @systemd.units
    def units(self) -> set[str]:
        return {
            "NetworkManager.service",
            "sshd.service",
            "ufw.service",
            "automatic-timezoned.service",
        }

    def files(self) -> dict[str, decman.File]:
        return {
            "/etc/mkinitcpio.conf": decman.File(
                source_file="./files/etc/mkinitcpio.conf"
            ),
            "/etc/pacman.conf": decman.File(source_file="./files/etc/pacman.conf"),
        }

    def on_change(self, store):
        decman.prg(["mkinitcpio", "-P"])
        decman.prg(["pacman", "-Sy"])

    def after_update(self):
        pass
        # subprocess.run("timedatectl set-timezone $(curl -sf https://ipapi.co/timezone)".split())
