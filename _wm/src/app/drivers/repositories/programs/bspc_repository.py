from src.app.drivers.repositories.programs.command_repository import CommandRepository
from src.core.repositories.bspc_repository import CoreBspcRepository
from src.core.repositories.command_repository import CoreCommandRepository


class BspcRepository(CoreBspcRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def list_monitors(self) -> list[str]:
        try:
            out = self._command_repo.run_capture("bspc query -M --names")
        except Exception:
            return []
        return [line.strip() for line in out.splitlines() if line.strip()]

    def set_monitor_desktops(self, monitor: str, desktops: list[str]) -> None:
        if not desktops:
            return
        quoted = " ".join(f"'{d}'" for d in desktops)
        self._command_repo.run(f"bspc monitor '{monitor}' -d {quoted}")
