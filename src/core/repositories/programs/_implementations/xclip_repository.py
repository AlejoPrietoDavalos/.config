from abc import abstractmethod
from pathlib import Path

from src.core.repositories.programs.program_repository import CoreProgramRepository


class CoreXclipRepository(CoreProgramRepository):
    @abstractmethod
    def copy_png_to_clipboard(self, path_png: Path) -> None:
        ...
