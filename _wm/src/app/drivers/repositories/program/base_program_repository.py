from abc import ABC, abstractmethod
from pathlib import Path

from core.entities.program_config import ProgramConfig


class BaseProgramRepository(ABC):
    @abstractmethod
    def build(self, config_root: Path) -> ProgramConfig:
        ...
