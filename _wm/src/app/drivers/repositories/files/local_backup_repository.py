from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from src.core.repositories.backup_repository import BackupRepository


class LocalBackupRepository(BackupRepository):
    def __init__(self, config_root: Path) -> None:
        self._config_root = config_root
        self._backup_root = config_root / "_wm" / "backups"

    def _backup_path(self) -> Path:
        return self._backup_root / datetime.now().strftime("%Y%m%d-%H%M%S")

    def backup_and_remove(self, path: Path) -> None:
        backup = self._backup_path() / path.relative_to(self._config_root)
        backup.parent.mkdir(parents=True, exist_ok=True)

        if path.is_symlink():
            target = path.resolve()
            if target.is_dir():
                shutil.copytree(target, backup, dirs_exist_ok=True)
            else:
                shutil.copy2(target, backup)
            path.unlink()
            return

        if path.is_dir():
            shutil.copytree(path, backup, dirs_exist_ok=True)
            shutil.rmtree(path)
            return

        shutil.copy2(path, backup)
        path.unlink()
