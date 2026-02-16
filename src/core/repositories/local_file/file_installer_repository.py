from abc import ABC, abstractmethod
from pathlib import Path


class CoreFileInstallerRepository(ABC):
    @abstractmethod
    def install(self, files_dir: Path, target_dir: Path) -> None:
        ...

    @abstractmethod
    def uninstall(self, files_dir: Path, target_dir: Path) -> None:
        ...
