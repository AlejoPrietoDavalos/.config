from typing import Literal, get_args

ProgramName = Literal[
    "bspwm",
    "sxhkd",
    "polybar",
    "ranger",
    "picom",
    "rofi",
    "thunar",
    "vscode",
]

PROGRAM_NAMES: tuple[ProgramName, ...] = get_args(ProgramName)
