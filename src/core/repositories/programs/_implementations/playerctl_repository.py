from abc import abstractmethod
from typing import Literal

from src.core.repositories.programs.program_repository import CoreProgramRepository

PlayerctlAction = Literal["previous", "next", "play_pause", "stop"]


class CorePlayerctlRepository(CoreProgramRepository):
    @abstractmethod
    def run(self, action: PlayerctlAction) -> None:
        ...

    @abstractmethod
    def previous(self) -> None:
        ...

    @abstractmethod
    def next(self) -> None:
        ...

    @abstractmethod
    def play_pause(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...
