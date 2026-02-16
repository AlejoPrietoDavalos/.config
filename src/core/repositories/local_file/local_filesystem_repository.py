from abc import ABC, abstractmethod
from pathlib import Path


class CoreLocalFilesystemRepository(ABC):
    @abstractmethod
    def ensure_dir(self, path: Path) -> None:
        ...

    @abstractmethod
    def list_dir(self, path: Path) -> list[Path]:
        ...

    @abstractmethod
    def ensure_cmd_exec(self, path: Path) -> None:
        ...

    @abstractmethod
    def exists_or_is_symlink(self, path: Path) -> bool:
        ...

    @abstractmethod
    def is_symlink(self, path: Path) -> bool:
        ...

    @abstractmethod
    def resolve(self, path: Path) -> Path:
        ...

    @abstractmethod
    def same_target(self, path: Path, target: Path) -> bool:
        ...

    @abstractmethod
    def symlink_to(self, dst: Path, src: Path) -> None:
        ...

    @abstractmethod
    def copy_path(self, src: Path, dst: Path) -> None:
        ...

    @abstractmethod
    def remove_path(self, path: Path) -> None:
        ...
