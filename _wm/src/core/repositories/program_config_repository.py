from abc import ABC, abstractmethod

from src.core.entities.program import ProgramName
from src.core.entities.program_config import ProgramConfig


class ProgramConfigRepository(ABC):
    @abstractmethod
    def get(self, program: ProgramName) -> ProgramConfig:
        ...
