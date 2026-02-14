import subprocess

from pathlib import Path
from typing import List

def cmd_set_wall(*, path_wall: Path) -> List[str]:
    """Return feh command to set a wallpaper."""
    return ["feh", "--bg-fill", str(path_wall)]


def set_wall(*, path_wall: Path) -> None:
    """Set the wallpaper with feh."""
    subprocess.run(cmd_set_wall(path_wall=path_wall))
