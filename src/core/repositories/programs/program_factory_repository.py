from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramName
from src.core.repositories.programs.program_repository import CoreProgramRepository


class CoreProgramFactoryRepository(ABC):
    @abstractmethod
    def get_program_repo(self, program: ProgramName) -> CoreProgramRepository:
        ...

    @abstractmethod
    def list_programs(self) -> list[str]:
        ...
