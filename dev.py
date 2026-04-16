import decman
from decman.plugins import pacman, aur, systemd


class DevModule(decman.Module):
    """
    Developer tooling: neovim, zsh, tmux, uv, rustup, Chrome, etc.
    Used by both 'dev' (with UI) and 'headless' (without UI) profiles.
    """

    def __init__(self, include_ui: bool = True):
        """
        Args:
            include_ui: Set to False for the headless profile to skip
                        browser, Ghostty, and Hyprland-adjacent packages.
        """
        name = "dev" if include_ui else "dev-headless"
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
            # "starship",         # shell prompt (alternative to oh-my-zsh themes)
            "docker",
            "docker-compose",
            # Build tools (rust needs these)
            "base-devel",
            "cmake",
            "clang",
            "llvm",
            # Python (uv manages Python versions, but system python is handy)
            "python",
            "python-pip",
            # "nodejs",          # Node (many LSPs need it)
            "bun",
            "pnpm",
            # LSP / language support
            "lua-language-server",
            "bash-language-server",
            "shfmt",
            "shellcheck",
        }

        return base

    @aur.packages
    def aur_pkgs(self) -> set[str]:
        base = {
            "rustup",  # manages rust toolchain + cargo
            "uv",  # fast Python package manager
            "oh-my-zsh-git",
            "zsh-theme-powerlevel10k-git",
        }

        return base

    @systemd.units
    def units(self) -> set[str]:
        return {"docker.service"}
