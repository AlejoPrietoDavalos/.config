from __future__ import annotations

from pathlib import Path

from src.app.drivers.repositories.files.local_backup_repository import LocalBackupRepository
from src.app.drivers.repositories.files.local_filesystem_repository import LocalFilesystemRepository
from src.core.entities.program_config import FileMode
from src.core.repositories.backup_repository import BackupRepository
from src.core.repositories.file_operations_repository import FileOperationsRepository
from src.core.repositories.filesystem_repository import FilesystemRepository


class LocalFileOperationsRepository(FileOperationsRepository):
    def __init__(
        self,
        fs_repo: FilesystemRepository | None = None,
        backup_repo: BackupRepository | None = None,
    ) -> None:
        self._fs_repo = fs_repo or LocalFilesystemRepository()
        self._backup_repo = backup_repo or LocalBackupRepository()

    def _prepare_destination(self, dst: Path, backup: bool) -> None:
        if not self._fs_repo.exists_or_is_symlink(dst):
            return
        if backup:
            self._backup_repo.backup_and_remove(dst)
            return
        self._fs_repo.remove_path(dst)

    def install(self, files_dir: Path, target_dir: Path, mode: FileMode, backup: bool = False) -> None:
        self._fs_repo.ensure_dir(target_dir)

        for src in self._fs_repo.list_dir(files_dir):
            self._fs_repo.ensure_cmd_exec(src)
            dst = target_dir / src.name

            if mode == "link":
                src_real = self._fs_repo.resolve(src)
                if self._fs_repo.same_target(dst, src_real):
                    continue
                self._prepare_destination(dst, backup=backup)
                self._fs_repo.symlink_to(dst, src_real)
                print(f"Linked: {dst} -> {src_real}")
                continue

            if mode == "copy":
                self._prepare_destination(dst, backup=backup)
                self._fs_repo.copy_path(src, dst)
                print(f"Copied: {src} -> {dst}")
                continue

            raise ValueError(f"Unsupported files mode: {mode}")

    def uninstall(self, files_dir: Path, target_dir: Path, mode: FileMode, backup: bool = False) -> None:
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
                self._prepare_destination(dst, backup=backup)
                action = "backup" if backup else "remove"
                print(f"Removed copied file ({action}): {dst}")
                continue

            raise ValueError(f"Unsupported files mode: {mode}")
