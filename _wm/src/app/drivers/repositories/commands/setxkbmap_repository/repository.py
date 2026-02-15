from src.core.repositories.command_repository import CommandRepository
from src.core.repositories.setxkbmap_repository import SetxkbmapRepository


class ShellSetxkbmapRepository(SetxkbmapRepository):
    def __init__(self, command_repo: CommandRepository) -> None:
        self._command_repo = command_repo

    def set_layout(self, layout: str) -> None:
        self._command_repo.run(f"setxkbmap -layout {layout}")
