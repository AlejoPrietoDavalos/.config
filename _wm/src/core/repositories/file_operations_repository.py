from abc import ABC, abstractmethod
from pathlib import Path

from core.entities.program_config import FileMode


class FileOperationsRepository(ABC):
    @abstractmethod
    def install(self, files_dir: Path, target_dir: Path, mode: FileMode, backup: bool = False) -> None:
        ...

    @abstractmethod
    def uninstall(self, files_dir: Path, target_dir: Path, mode: FileMode, backup: bool = False) -> None:
        ...
