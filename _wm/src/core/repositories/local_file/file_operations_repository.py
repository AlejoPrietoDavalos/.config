from abc import ABC, abstractmethod
from pathlib import Path

from src.core.entities.program_config import FileMode


class FileOperationsRepository(ABC):
    @abstractmethod
    def install(self, files_dir: Path, target_dir: Path, mode: FileMode) -> None:
        ...

    @abstractmethod
    def uninstall(self, files_dir: Path, target_dir: Path, mode: FileMode) -> None:
        ...
