from abc import ABC, abstractmethod

from src.core.entities.program_config import Packages, ProgramName


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
