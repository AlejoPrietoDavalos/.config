from abc import ABC, abstractmethod


class CoreBspcRepository(ABC):
    @abstractmethod
    def list_monitors(self) -> list[str]:
        ...

    @abstractmethod
    def set_monitor_desktops(self, monitor: str, desktops: list[str]) -> None:
        ...
