from abc import abstractmethod

from src.core.repositories.programs.program_repository import CoreProgramRepository


class CoreSxhkdRepository(CoreProgramRepository):
    @abstractmethod
    def reload_sxhkd(self) -> None:
        ...
