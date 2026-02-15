from abc import ABC, abstractmethod


class CommandRepository(ABC):
    @abstractmethod
    def run(self, cmd: str) -> None:
        ...
