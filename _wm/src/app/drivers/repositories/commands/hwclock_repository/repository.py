from src.core.repositories.command_repository import CommandRepository
from src.core.repositories.hwclock_repository import HwclockRepository


class ShellHwclockRepository(HwclockRepository):
    def __init__(self, command_repo: CommandRepository) -> None:
        self._command_repo = command_repo

    def set_timezone(self, timezone: str) -> None:
        self._command_repo.run(f"sudo ln -sf /usr/share/zoneinfo/{timezone} /etc/localtime")

    def sync_system_to_hardware(self) -> None:
        self._command_repo.run("sudo hwclock --systohc")
