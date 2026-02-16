from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramConfig


class CoreBaseProgramRepository(ABC):
    @abstractmethod
    def default_config(self) -> ProgramConfig:
        ...

    @abstractmethod
    def install_requirement(self) -> None:
        ...

    @abstractmethod
    def uninstall_requirement(self) -> None:
        ...

    @abstractmethod
    def install_files(self) -> None:
        ...

    @abstractmethod
    def uninstall_files(self) -> None:
        ...
