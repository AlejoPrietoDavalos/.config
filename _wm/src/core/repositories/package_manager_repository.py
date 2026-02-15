from abc import ABC, abstractmethod
from pathlib import Path


class PackageManagerRepository(ABC):
    @abstractmethod
    def install(self, program: str, packages_file: Path) -> None:
        ...

    @abstractmethod
    def uninstall(self, program: str, packages_file: Path) -> None:
        ...
