import time

from src.core.repositories.programs.bspc_repository import CoreBspcRepository
from src.core.repositories.programs.xrandr_repository import CoreXrandrRepository


DESKTOPS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def split_even(items: list[str], parts: int) -> list[list[str]]:
    if parts <= 0:
        return []
    base, extra = divmod(len(items), parts)
    chunks: list[list[str]] = []
    index = 0
    for part in range(parts):
        size = base + (1 if part >= (parts - extra) and extra > 0 else 0)
        chunks.append(items[index : index + size])
        index += size
    return chunks


class ApplyMonitorLayout:
    def __init__(self, xrandr_repo: CoreXrandrRepository, bspc_repo: CoreBspcRepository) -> None:
        self._xrandr_repo = xrandr_repo
        self._bspc_repo = bspc_repo

    def run(self) -> None:
        self._ensure_connected_outputs_enabled()
        monitors = self._resolve_active_monitors()
        if not monitors:
            return

        target_monitors = monitors[: len(DESKTOPS)]
        chunks = split_even(DESKTOPS, len(target_monitors))
        for monitor, desktops in zip(target_monitors, chunks):
            self._bspc_repo.set_monitor_desktops(monitor, desktops)

    def _ensure_connected_outputs_enabled(self) -> None:
        connected = self._xrandr_repo.list_connected_outputs()
        if not connected:
            return
        active = set(self._xrandr_repo.list_active_outputs())
        if any(output not in active for output in connected):
            self._xrandr_repo.enable_outputs_auto(connected)
            time.sleep(0.2)

    def _resolve_active_monitors(self) -> list[str]:
        bspwm_monitors = self._bspc_repo.list_monitors()
        if not bspwm_monitors:
            return []
        xrandr_active = self._xrandr_repo.list_active_outputs()
        if not xrandr_active:
            return bspwm_monitors
        ordered = [m for m in xrandr_active if m in bspwm_monitors]
        return ordered or bspwm_monitors
