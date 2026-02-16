from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramConfig


class CoreProgramRepository(ABC):
    @abstractmethod
    def default_config(self) -> ProgramConfig:
        ...
