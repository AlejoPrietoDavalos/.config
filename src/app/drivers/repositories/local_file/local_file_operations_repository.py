from __future__ import annotations

import logging
from pathlib import Path

from src.app.drivers.repositories.local_file.file_template_renderer_repository import FileTemplateRendererRepository
from src.app.drivers.repositories.local_file.local_filesystem_repository import LocalFilesystemRepository
from src.core.constants import path_repo
from src.core.repositories.local_file import CoreFileInstallerRepository, CoreFileTemplateRendererRepository, CoreLocalFilesystemRepository

logger = logging.getLogger(__name__)

_SYSTEM_TOKENS = {"{{DOTFILES_REPO}}": str(path_repo)}


class LocalFileOperationsRepository(CoreFileInstallerRepository):
    def __init__(
        self,
        fs_repo: CoreLocalFilesystemRepository | None = None,
        template_renderer: CoreFileTemplateRendererRepository | None = None,
    ) -> None:
        self._fs_repo = fs_repo or LocalFilesystemRepository()
        self._template_renderer = template_renderer or FileTemplateRendererRepository()

    def _prepare_destination(self, path_target: Path) -> None:
        if self._fs_repo.exists_or_is_symlink(path_target):
            self._fs_repo.remove_path(path_target)

    def _should_skip(self, path_source: Path) -> bool:
        return path_source.name.startswith("_") or path_source.name == "__pycache__" or path_source.suffix == ".pyc"

    def _render(self, path_target: Path, extra_tokens: dict[str, str] | None) -> None:
        """Construye el dict de tokens (sistema + programa) y aplica el reemplazo sobre el archivo o directorio."""
        tokens = {**_SYSTEM_TOKENS.copy(), **(extra_tokens or {})}
        self._template_renderer.render(path_target, tokens)

    def install(self, files_dir: Path, target_dir: Path, extra_tokens: dict[str, str] | None = None) -> None:
        """Copia los archivos de files_dir a target_dir y reemplaza los tokens en cada archivo copiado."""
        self._fs_repo.ensure_dir(target_dir)
        program_tag = files_dir.name

        for path_source in self._fs_repo.list_dir(files_dir):
            if self._should_skip(path_source):
                logger.info("[%s] [files skip] ignored internal file: %s", program_tag, path_source)
                continue
            self._fs_repo.ensure_cmd_exec(path_source)
            path_target = target_dir / path_source.name
            self._prepare_destination(path_target)
            self._fs_repo.copy_path(path_source, path_target)
            self._render(path_target, extra_tokens)
            logger.info("[%s] [files copy] %s -> %s", program_tag, path_source, path_target)

    def uninstall(self, files_dir: Path, target_dir: Path) -> None:
        """Elimina de target_dir los archivos que corresponden a los de files_dir."""
        program_tag = files_dir.name
        for path_source in self._fs_repo.list_dir(files_dir):
            path_target = target_dir / path_source.name
            if self._should_skip(path_source):
                if self._fs_repo.exists_or_is_symlink(path_target):
                    self._prepare_destination(path_target)
                    logger.info("[%s] [files delete] removed internal file: %s", program_tag, path_target)
                continue

            if not self._fs_repo.exists_or_is_symlink(path_target):
                logger.info("[%s] [files delete skip] not found: %s", program_tag, path_target)
                continue
            self._prepare_destination(path_target)
            logger.info("[%s] [files delete] removed: %s", program_tag, path_target)
