from abc import ABC, abstractmethod


class CoreSetxkbmapRepository(ABC):
    @abstractmethod
    def set_layout(self, layout: str) -> None:
        ...
