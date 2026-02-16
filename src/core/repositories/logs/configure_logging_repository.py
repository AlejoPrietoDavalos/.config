import logging
from abc import ABC, abstractmethod
from pathlib import Path


class CoreConfigureLoggingRepository(ABC):
    @abstractmethod
    def configure(self, level: int = logging.INFO, path_logs: Path | None = None) -> None:
        ...
