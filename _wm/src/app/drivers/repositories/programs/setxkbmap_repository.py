from src.app.drivers.repositories.programs.command_repository import CommandRepository
from src.core.repositories.command_repository import CoreCommandRepository
from src.core.repositories.setxkbmap_repository import CoreSetxkbmapRepository


class SetxkbmapRepository(CoreSetxkbmapRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def set_layout(self, layout: str) -> None:
        self._command_repo.run(f"setxkbmap -layout {layout}")
