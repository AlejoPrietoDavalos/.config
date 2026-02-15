from abc import ABC, abstractmethod


class CommandRepository(ABC):
    @abstractmethod
    def run(self, cmd: str) -> None:
        ...

    @abstractmethod
    def run_capture(self, cmd: str) -> str:
        ...
