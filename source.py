"""
decman source — entry point
Run with:  sudo decman ~/source/source.py
"""

import decman
from decman.plugins import pacman

from base import BaseModule
from hyprland import HyprlandModule
from dev import DevModule
from gaming import GamingModule
from users import make_user_manager

# ── modules ───────────────────────────────────────────────────────────────────
decman.modules += [
    # Core system (always present)
    BaseModule(),
    # Display stack (dev + gaming profiles share this)
    HyprlandModule(),
    # Developer tooling — with UI (browser + ghostty)
    DevModule(include_ui=True),
    # Gaming suite
    GamingModule(),
    # Headless dev tooling — no UI packages
    # DevModule(include_ui=False) is merged below via shared packages;
    # the headless user simply doesn't launch Hyprland.
    # If you want headless to be a completely separate, minimal install,
    # comment out HyprlandModule and GamingModule above and uncomment:
    # DevModule(include_ui=False),
    # Users
    make_user_manager(),
]

# ── system-wide services ──────────────────────────────────────────────────────
# (per-module services are declared in each Module; add extras here)
decman.systemd.enabled_units |= {
    "bluetooth.service",
}

# ── system files ──────────────────────────────────────────────────────────────
# Uncomment and point to your dotfiles repo as needed, e.g.:
# from decman import File, Directory
# decman.files["/etc/pacman.conf"] = File(source_file="./dotfiles/pacman.conf")
