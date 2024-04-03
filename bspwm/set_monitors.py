#!/usr/bin/python3
from typing import List, Optional
from pathlib import Path
import subprocess
import json


def get_12345() -> List[str]:
    return list(str(d) for d in range(1, 5+1))

def get_67890() -> List[str]:
    return list(str(d) for d in range(6, 9+1)) + ["0"]

def get_1234567890() -> List[str]:
    return get_12345() + get_67890()


class CmdBSPWM:
    @classmethod
    def cmd_set_monitor(
            cls,
            monitor: str,
            pos: str,
            resolution: str,
            is_primary: bool = False,
            monitor_left: Optional[str] = None
        ) -> List[str]:
        cmd = [
            "xrandr",
            "--output", monitor,
            "--mode", resolution,
            "--rotate", "normal",
            "--pos", pos
        ]
        if is_primary:
            cmd.extend(["--primary"])
        if monitor_left is not None:     # Se debe pasar el monitor que esté a la izquierda de este.
            cmd.extend(["--right-of", monitor_left])
        return cmd
    
    @classmethod
    def cmd_set_desktops(cls, monitor: str, desktops: List[str]) -> List[str]:
        cmd = ["bspc", "monitor", monitor, "-d"]
        cmd.extend(desktops)
        return cmd

    @classmethod
    def set_monitor_primary(cls, monitor: str, pos: str, resolution: str) -> None:
        cmd = cls.cmd_set_monitor(monitor=monitor, pos=pos, resolution=resolution, is_primary=True)
        subprocess.run(cmd)

    @classmethod
    def set_monitor_secondary(cls, monitor_left: str, monitor_right: str, pos: str, resolution: str) -> None:
        cmd = cls.cmd_set_monitor(monitor=monitor_right, pos=pos, resolution=resolution, monitor_left=monitor_left)
        subprocess.run(cmd)

    @classmethod
    def set_desktops(cls, monitor: str, desktops: List[str]) -> None:
        cmd = cls.cmd_set_desktops(monitor=monitor, desktops=desktops)
        subprocess.run(cmd)

    @classmethod
    def set_desktops_from_monitors(cls, monitors: List[str]) -> None:
        if len(monitors) == 1:
            CmdBSPWM.set_desktops(monitors[0], get_1234567890())
        if len(monitors) == 2:
            CmdBSPWM.set_desktops(monitors[0], get_12345())
            CmdBSPWM.set_desktops(monitors[1], get_67890())


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