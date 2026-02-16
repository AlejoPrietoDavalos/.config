from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramName
from src.core.repositories.program_repository import CoreProgramRepository


class ProgramRegistryRepository(ABC):
    @abstractmethod
    def get_program_repo(self, program: ProgramName) -> CoreProgramRepository:
        ...
