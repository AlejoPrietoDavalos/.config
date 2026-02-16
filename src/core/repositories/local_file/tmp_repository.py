from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from pathlib import Path


class CoreTmpRepository(ABC):
    @abstractmethod
    def temporary_path(
        self,
        suffix: str = "",
        filename: str = "tmp",
        directory_prefix: str = "tmp_",
    ) -> AbstractContextManager[Path]:
        ...

    @abstractmethod
    def temporary_png_path(self) -> AbstractContextManager[Path]:
        ...
