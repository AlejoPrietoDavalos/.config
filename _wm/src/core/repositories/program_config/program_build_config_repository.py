from abc import ABC, abstractmethod

from src.core.entities.program_config import ProgramConfig


class ProgramBuildConfigRepository(ABC):
    @abstractmethod
    def build_config(self) -> ProgramConfig:
        ...
