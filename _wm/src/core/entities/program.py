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
]

PROGRAM_NAMES: tuple[ProgramName, ...] = get_args(ProgramName)
