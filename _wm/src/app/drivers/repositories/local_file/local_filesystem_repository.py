from __future__ import annotations

import shutil
import stat
from pathlib import Path

from src.core.repositories.local_file.local_filesystem_repository import CoreLocalFilesystemRepository


class LocalFilesystemRepository(CoreLocalFilesystemRepository):
    def ensure_dir(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)

    def list_dir(self, path: Path) -> list[Path]:
        return sorted(path.iterdir())

    def ensure_cmd_exec(self, path: Path) -> None:
        if not path.is_dir() or path.name != "cmd":
            return
        for child in path.iterdir():
            if child.is_file():
                mode = child.stat().st_mode
                child.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    def exists_or_is_symlink(self, path: Path) -> bool:
        return path.exists() or path.is_symlink()

    def is_symlink(self, path: Path) -> bool:
        return path.is_symlink()

    def resolve(self, path: Path) -> Path:
        return path.resolve()

    def same_target(self, path: Path, target: Path) -> bool:
        if not path.is_symlink():
            return False
        return path.resolve() == target.resolve()

    def symlink_to(self, dst: Path, src: Path) -> None:
        dst.symlink_to(src.resolve())

    def copy_path(self, src: Path, dst: Path) -> None:
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
            return
        shutil.copy2(src, dst)

    def remove_path(self, path: Path) -> None:
        if path.is_symlink():
            path.unlink()
            return
        if path.is_dir():
            shutil.rmtree(path)
            return
        path.unlink()
