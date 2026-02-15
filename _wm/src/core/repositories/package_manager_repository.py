from abc import ABC, abstractmethod

from src.core.entities.packages import Packages
from src.core.entities.program import ProgramName
from src.core.entities.program_config import PackageManager


class PackageManagerRepository(ABC):
    @abstractmethod
    def install(
        self,
        program: ProgramName,
        packages: Packages,
        manager: PackageManager = "pacman",
    ) -> None:
        ...

    @abstractmethod
    def uninstall(
        self,
        program: ProgramName,
        packages: Packages,
        manager: PackageManager = "pacman",
    ) -> None:
        ...
