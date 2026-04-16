import decman
from decman.plugins import pacman, aur, systemd
from hyprland.base import HyprlandModule


class DevModule(decman.Module):
    """
    Developer tooling: neovim, zsh, tmux, uv, rustup, Chrome, etc.
    Used by both 'dev' (with UI) and 'headless' (without UI) profiles.
    """

    user: str
    include_ui: bool

    def __init__(self, user, include_ui: bool = True):
        """
        Args:
            user: string representing user name and home location
            include_ui: Set to False for the headless profile to skip
                        browser, Ghostty, and Hyprland-adjacent packages.
        """
        self.user = user
        self.include_ui = include_ui
        if self.include_ui:
            decman.modules.append(HyprlandModule(self.user))

        name = "dev" if self.include_ui else "dev-headless"
        super().__init__(name)

    @pacman.packages
    def pkgs(self) -> set[str]:
        base = {
            # Shell
            "zsh",
            "zsh-completions",
            "zsh-syntax-highlighting",
            "zsh-autosuggestions",
            # Editor
            "neovim",
            "tree-sitter",
            "ripgrep",  # telescope / grep
            "fd",  # telescope file finder
            "lazygit",
            # Terminal multiplexer
            "tmux",
            # Dev essentials
            "git",
            "github-cli",
            "jq",
            "fzf",
            "bat",
            # "eza",              # modern ls
            # "zoxide",           # smart cd
            "docker",
            "docker-compose",
            # Build tools (rust needs these)
            "base-devel",
            "cmake",
            "clang",
            "llvm",
            # Python (uv manages Python versions, but system python is handy)
            # "python",
            # "python-pip",
            # Node
            # "nodejs",          # Node (many LSPs need it)
            "bun",
            "pnpm",
            # LSP / language support
            "lua-language-server",
            "bash-language-server",
            "shfmt",
            "shellcheck",
            "rustup",  # manages rust toolchain + cargo
        }

        return base

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        base = {
            "uv",  # fast Python package manager
            "oh-my-zsh-git",
            "zsh-theme-powerlevel10k-git",
        }

        return base

    @systemd.units
    def units(self) -> set[str]:
        return {"docker.service"}
