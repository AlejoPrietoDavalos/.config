from pathlib import Path
import subprocess

path_home = Path.home()
path_config = path_home / ".config"
branchs = ["bspwm", "polybar", "sxhkd", "picom", "kitty", "ranger", "rofi"]

for branch in branchs:
    cmd = [
        "git", "clone",
        "--branch", branch,
        "https://github.com/AlejoPrietoDavalos/.dotfiles.git",
        f"{path_config / branch}"
    ]
    subprocess.run(cmd)
