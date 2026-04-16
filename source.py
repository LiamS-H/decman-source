"""
decman source — entry point
Run with:  sudo decman ~/source/source.py
"""

import decman
from decman.plugins import pacman

from audio import AudioModule
from base import BaseModule
from dev import DevModule
from gaming import GamingModule
from users import make_user_manager

# ── modules ───────────────────────────────────────────────────────────────────
decman.modules += [
    # Core system (always present)
    BaseModule(),
    AudioModule(),
    # Developer tooling — with UI (browser + ghostty)
    DevModule("dev", include_ui=True),
    DevModule("headless", include_ui=False),
    GamingModule("gaming"),
    make_user_manager(),
]

# ── system-wide services ──────────────────────────────────────────────────────
# (per-module services are declared in each Module; add extras here)
decman.systemd.enabled_units |= {
    "bluetooth.service",
}
