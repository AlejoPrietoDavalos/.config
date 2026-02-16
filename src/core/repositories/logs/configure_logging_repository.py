import logging
from abc import ABC, abstractmethod


class CoreConfigureLoggingRepository(ABC):
    @abstractmethod
    def configure(
        self,
        level: int = logging.INFO,
        log_filename: str | None = None,
    ) -> None:
        ...
