from __future__ import annotations

import logging
from pathlib import Path

from src.app.drivers.repositories.local_file.local_filesystem_repository import LocalFilesystemRepository
from src.core.repositories.local_file import CoreFileInstallerRepository, CoreLocalFilesystemRepository

logger = logging.getLogger(__name__)


class LocalFileOperationsRepository(CoreFileInstallerRepository):
    def __init__(self, fs_repo: CoreLocalFilesystemRepository | None = None) -> None:
        self._fs_repo = fs_repo or LocalFilesystemRepository()

    def _prepare_destination(self, dst: Path) -> None:
        if self._fs_repo.exists_or_is_symlink(dst):
            self._fs_repo.remove_path(dst)

    def _should_skip(self, src: Path) -> bool:
        return src.name == "__pycache__" or src.suffix == ".pyc"

    def install(self, files_dir: Path, target_dir: Path) -> None:
        self._fs_repo.ensure_dir(target_dir)
        program_tag = files_dir.name

        for src in self._fs_repo.list_dir(files_dir):
            if self._should_skip(src):
                logger.info("[%s] [files skip] ignored internal file: %s", program_tag, src)
                continue
            self._fs_repo.ensure_cmd_exec(src)
            dst = target_dir / src.name
            self._prepare_destination(dst)
            self._fs_repo.copy_path(src, dst)
            logger.info("[%s] [files copy] %s -> %s", program_tag, src, dst)

    def uninstall(self, files_dir: Path, target_dir: Path) -> None:
        program_tag = files_dir.name
        for src in self._fs_repo.list_dir(files_dir):
            dst = target_dir / src.name
            if self._should_skip(src):
                if self._fs_repo.exists_or_is_symlink(dst):
                    self._prepare_destination(dst)
                    logger.info("[%s] [files delete] removed internal file: %s", program_tag, dst)
                continue

            if not self._fs_repo.exists_or_is_symlink(dst):
                logger.info("[%s] [files delete skip] not found: %s", program_tag, dst)
                continue
            self._prepare_destination(dst)
            logger.info("[%s] [files delete] removed: %s", program_tag, dst)
