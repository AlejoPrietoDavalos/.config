from abc import ABC, abstractmethod

from core.entities.program_config import ProgramConfig


class ProgramConfigRepository(ABC):
    @abstractmethod
    def get(self, program: str) -> ProgramConfig:
        ...
