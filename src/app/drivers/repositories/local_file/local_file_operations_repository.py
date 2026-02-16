from __future__ import annotations

from pathlib import Path

from src.app.drivers.repositories.local_file.local_filesystem_repository import LocalFilesystemRepository
from src.core.entities.program_config import FileMode
from src.core.repositories.local_file import CoreFileInstallerRepository, CoreLocalFilesystemRepository


class LocalFileOperationsRepository(CoreFileInstallerRepository):
    def __init__(self, fs_repo: CoreLocalFilesystemRepository | None = None) -> None:
        self._fs_repo = fs_repo or LocalFilesystemRepository()

    def _prepare_destination(self, dst: Path) -> None:
        if self._fs_repo.exists_or_is_symlink(dst):
            self._fs_repo.remove_path(dst)

    def install(self, files_dir: Path, target_dir: Path, mode: FileMode) -> None:
        self._fs_repo.ensure_dir(target_dir)

        for src in self._fs_repo.list_dir(files_dir):
            self._fs_repo.ensure_cmd_exec(src)
            dst = target_dir / src.name

            if mode == "link":
                src_real = self._fs_repo.resolve(src)
                if self._fs_repo.same_target(dst, src_real):
                    continue
                self._prepare_destination(dst)
                self._fs_repo.symlink_to(dst, src_real)
                print(f"Linked: {dst} -> {src_real}")
                continue

            if mode == "copy":
                self._prepare_destination(dst)
                self._fs_repo.copy_path(src, dst)
                print(f"Copied: {src} -> {dst}")
                continue

            raise ValueError(f"Unsupported files mode: {mode}")

    def uninstall(self, files_dir: Path, target_dir: Path, mode: FileMode) -> None:
        for src in self._fs_repo.list_dir(files_dir):
            dst = target_dir / src.name

            if mode == "link":
                if self._fs_repo.same_target(dst, src):
                    self._fs_repo.remove_path(dst)
                    print(f"Unlinked: {dst}")
                continue

            if mode == "copy":
                if not self._fs_repo.exists_or_is_symlink(dst):
                    continue
                self._prepare_destination(dst)
                print(f"Removed copied file: {dst}")
                continue

            raise ValueError(f"Unsupported files mode: {mode}")
