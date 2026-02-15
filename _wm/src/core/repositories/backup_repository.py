from abc import ABC, abstractmethod
from pathlib import Path


class BackupRepository(ABC):
    @abstractmethod
    def backup_and_remove(self, path: Path) -> None:
        ...
