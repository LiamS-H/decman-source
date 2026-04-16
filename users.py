from decman.extras.users import UserManager, User, Group


def make_user_manager() -> UserManager:
    um = UserManager()

    # ── Shared groups ─────────────────────────────────────────────────────────
    um.add_group(Group("docker"))
    um.add_group(Group("video"))
    um.add_group(Group("input"))
    um.add_group(Group("gamemode"))

    # ── dev ───────────────────────────────────────────────────────────────────
    # Full desktop developer: Hyprland + neovim + zsh + uv + rustup + Chrome
    um.add_user(
        User(
            username="dev",
            uid=1000,
            home="/home/dev",
            shell="/bin/zsh",
            groups=(
                "wheel",
                "docker",
                "video",
                "input",
                "audio",
                "storage",
                "optical",
            ),
        )
    )

    # ── gaming ────────────────────────────────────────────────────────────────
    # Hyprland + Steam + emulation; no dev tooling
    um.add_user(
        User(
            username="gaming",
            uid=1001,
            home="/home/gaming",
            shell="/bin/bash",
            groups=(
                "wheel",
                "docker",
                "video",
                "input",
                "audio",
                "storage",
                "gamemode",
                "optical",
            ),
        )
    )

    # ── headless ──────────────────────────────────────────────────────────────
    # SSH / server dev: same tooling as dev but no Hyprland, no browser
    um.add_user(
        User(
            username="headless",
            uid=1002,
            home="/home/headless",
            shell="/bin/zsh",
            groups=(
                "wheel",
                "docker",
                "video",
                "input",
                "audio",
                "storage",
            ),
        )
    )

    return um
