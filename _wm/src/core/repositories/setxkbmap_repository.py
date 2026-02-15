from abc import ABC, abstractmethod


class SetxkbmapRepository(ABC):
    @abstractmethod
    def set_layout(self, layout: str) -> None:
        ...
