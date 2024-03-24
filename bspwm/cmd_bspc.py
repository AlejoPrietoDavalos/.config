from typing import List
import subprocess

def desktops_from_ints(desktops: List[int]) -> List[str]:
    return [str(d) for d in desktops]


class CommandsBSPWM:
    @staticmethod
    def set_monitor_primary(monitor: str, pos: str, resolution: str) -> None:
        subprocess.run([
            "xrandr",
            "--output", monitor,
            "--primary",
            "--mode", resolution,
            "--rotate", "normal",
            "--pos", pos
        ])

    @staticmethod
    def set_monitor_secondary(monitor_left: str, monitor_right: str, pos: str, resolution: str) -> None:
        subprocess.run([
            "xrandr",
            "--output", monitor_right,
            "--mode", resolution,
            "--rotate", "normal",
            "--pos", pos,
            "--right-of", monitor_left
        ])

    @staticmethod
    def set_desktops(monitor: str, desktops: List[int]) -> None:
        _command = ["bspc", "monitor", monitor, "-d"]
        _command.extend(desktops_from_ints(desktops))
        subprocess.run(_command)

    @staticmethod
    def set_desktops_from_monitors(monitors: List[str]) -> None:
        if len(monitors) == 1:
            CommandsBSPWM.set_desktops(monitors[0], list(range(1, 10)) + [0])
        if len(monitors) == 2:
            CommandsBSPWM.set_desktops(monitors[0], list(range(1, 5+1)))
            CommandsBSPWM.set_desktops(monitors[1], list(range(6, 9+1)) + [0])
