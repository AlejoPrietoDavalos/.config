from abc import ABC, abstractmethod

from src.core.entities.packages import Packages
from src.core.entities.program import ProgramName


class PackageManagerRepository(ABC):
    @abstractmethod
    def install(
        self,
        program: ProgramName,
        packages: Packages,
    ) -> None:
        ...

    @abstractmethod
    def uninstall(
        self,
        program: ProgramName,
        packages: Packages,
    ) -> None:
        ...
