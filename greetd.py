import decman
from decman.plugins import pacman, systemd

class GreetdModule(decman.Module):
    def __init__(self):
        super().__init__("greetd")

    @pacman.packages
    def pkgs(self) -> set[str]:
        return {
            "greetd",
            "greetd-tuigreet",
        }

    @systemd.units
    def units(self) -> set[str]:
        return {"greetd.service"}

    def files(self) -> dict[str, decman.File]:
        return {
            "/etc/greetd/config.toml": decman.File(
                source_file="./files/etc/greetd/config.toml"
            ),
        }
