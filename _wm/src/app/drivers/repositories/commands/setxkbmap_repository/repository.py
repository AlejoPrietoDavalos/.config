from src.core.repositories.command_repository import CommandRepository
from src.core.repositories.setxkbmap_repository import SetxkbmapRepository
from src.app.drivers.repositories.commands.shell_command_repository import ShellCommandRepository


class ShellSetxkbmapRepository(SetxkbmapRepository):
    def __init__(self, command_repo: CommandRepository | None = None) -> None:
        self._command_repo = command_repo or ShellCommandRepository()

    def set_layout(self, layout: str) -> None:
        self._command_repo.run(f"setxkbmap -layout {layout}")
