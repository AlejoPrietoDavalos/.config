from typing import List
import subprocess

def desktops_from_ints(desktops: List[int]) -> List[str]:
    return [str(d) for d in desktops]

def get_12345() -> List[int]:
    return list(range(1, 5+1))

def get_67890() -> List[int]:
    return list(range(6, 9+1)) + [0]

def get_1234567890() -> List[int]:
    return get_12345() + get_67890()

class CmdBSPWM:
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
            CmdBSPWM.set_desktops(monitors[0], get_1234567890())
        if len(monitors) == 2:
            CmdBSPWM.set_desktops(monitors[0], get_12345())
            CmdBSPWM.set_desktops(monitors[1], get_67890())
