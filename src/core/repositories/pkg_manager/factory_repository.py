from abc import ABC, abstractmethod

from src.core.entities.program_config import Packages


class CorePkgManagerFactoryRepository(ABC):
    @abstractmethod
    def install(self, pkgs: Packages, program_name: str | None = None) -> None:
        ...

    @abstractmethod
    def uninstall(self, pkgs: Packages, program_name: str | None = None) -> None:
        ...
