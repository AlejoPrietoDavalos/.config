from typing import List
from pathlib import Path
import subprocess
import json

from cmd_bspc import CmdBSPWM

def detect_monitors() -> List[str]:
    """ FIXME: Detecta un None-1-1, ver como solucionarlo, se fixea con un `if`."""
    result = subprocess.run(["xrandr | grep ' connected '"], stdout = subprocess.PIPE, shell = True)
    xrandr_grep_monitors = result.stdout.decode("utf-8").strip()
    xrandr_grep_monitors = xrandr_grep_monitors.split("\n")
    monitors = []
    for line in xrandr_grep_monitors:
        m = line.split(" connected ")[0].strip()
        if "none" not in m.lower():                 # ----> BUG
            monitors.append(m)
    return monitors


def main(monitors: List[str], positions: str, resolution: str = "1920x1080") -> None:
    CmdBSPWM.set_monitor_primary(monitors[0], positions[0], resolution)
    for i in range(len(monitors) - 1):
        CmdBSPWM.set_monitor_secondary(monitors[i], monitors[i+1], positions[i+1], resolution)
    
    CmdBSPWM.set_desktops_from_monitors(monitors)

if __name__ == "__main__":
    # TODO: Que obtenga los monitores encontrados, y que asigne los desktops dependiendo del número.
    # TODO: Luego hacer una herramienta que permita modificarlos en caso que estén mal asignados.
    path_monitors_json = Path.home() / ".config" / "bspwm" / "monitors.json"
    with open(path_monitors_json, "r") as f:
        monitors = json.load(f)["monitors"]
    monitors_detected = detect_monitors()
    monitors = [m for m in monitors if m in monitors_detected]
    
    positions = ["0x0", "1920x0"]
    resolution = "1920x1080"
    main(
        monitors = monitors,
        positions = positions,
        resolution = resolution
    )
    
    from wallpaper import set_wall, get_random_wall
    set_wall(get_random_wall())