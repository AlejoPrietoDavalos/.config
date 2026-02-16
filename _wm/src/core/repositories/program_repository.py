from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramConfig


class CoreProgramRepository(ABC):
    @abstractmethod
    def default_config(self) -> ProgramConfig:
        ...

    @abstractmethod
    def install_requirement(self) -> None:
        ...

    @abstractmethod
    def uninstall_requirement(self) -> None:
        ...

    def install_files(self) -> None:
        raise NotImplementedError("install_files is not implemented for this program")

    def uninstall_files(self) -> None:
        raise NotImplementedError("uninstall_files is not implemented for this program")
