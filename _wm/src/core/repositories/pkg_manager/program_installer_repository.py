from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramConfig


class ProgramInstallerRepository(ABC):
    @abstractmethod
    def install_requirement(self, cfg: ProgramConfig) -> None:
        ...

    @abstractmethod
    def uninstall_requirement(self, cfg: ProgramConfig) -> None:
        ...

    @abstractmethod
    def install_files(self, cfg: ProgramConfig) -> None:
        ...

    @abstractmethod
    def uninstall_files(self, cfg: ProgramConfig) -> None:
        ...
