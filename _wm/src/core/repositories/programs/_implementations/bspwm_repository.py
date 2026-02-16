from abc import ABC, abstractmethod

from src.core.repositories.programs.program_repository import CoreProgramRepository


class CoreBspwmRepository(CoreProgramRepository, ABC):
    @abstractmethod
    def list_monitors(self) -> list[str]:
        ...

    @abstractmethod
    def set_monitor_desktops(self, monitor: str, desktops: list[str]) -> None:
        ...
