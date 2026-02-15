from typing import Literal, get_args

ProgramName = Literal[
    "bspwm",
    "sxhkd",
    "polybar",
    "kitty",
    "ranger",
    "picom",
    "rofi",
    "thunar",
    "vscode",
    "wm-base",
    "pulseaudio",
    "display-tools",
    "nvidia",
]

PROGRAM_NAMES: tuple[ProgramName, ...] = get_args(ProgramName)
