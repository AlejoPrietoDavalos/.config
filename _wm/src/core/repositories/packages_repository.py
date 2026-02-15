from abc import ABC, abstractmethod

from src.core.entities.packages import Packages
from src.core.entities.program_config import ProgramConfig


class PackagesRepository(ABC):
    @abstractmethod
    def get(self, cfg: ProgramConfig) -> Packages:
        ...
