from typing import List
from pathlib import Path
import subprocess
import json

from cmd_bspc import CommandsBSPWM

def detect_monitors() -> List[str]:
    result = subprocess.run(
        ["xrandr | grep ' connected '"],
        stdout = subprocess.PIPE,
        shell = True
    )
    xrandr_grep_monitors = result.stdout.decode("utf-8").strip()
    xrandr_grep_monitors = xrandr_grep_monitors.split("\n")
    monitors = [line.split(" connected ")[0].strip() for line in xrandr_grep_monitors]
    return monitors


def main(
        monitors: List[str],
        positions: str,
        resolution: str = "1920x1080") -> None:
    CommandsBSPWM.set_monitor_primary(monitors[0], positions[0], resolution)
    for i in range(len(monitors) - 1):
        CommandsBSPWM.set_monitor_secondary(monitors[i], monitors[i+1], positions[i+1], resolution)
    
    CommandsBSPWM.set_desktops_from_monitors(monitors)

if __name__ == "__main__":
    # TODO: Que obtenga los monitores encontrados, y que asigne los desktops dependiendo del número.
    # TODO: Luego hacer una herramienta que permita modificarlos en caso que estén mal asignados.
    path_monitors_json = Path.home() / ".config" / "bspwm" / "monitors.json"
    with open(path_monitors_json, "r") as f:
        monitors = json.load(f)["monitors"]
    positions = ["0x0", "1920x0"]
    resolution = "1920x1080"
    main(
        monitors = monitors,
        positions = positions,
        resolution = resolution
    )
    
    from wallpaper import set_wall, get_random_wall
    set_wall(get_random_wall())