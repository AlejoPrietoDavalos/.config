import logging
from pathlib import Path

from src.app.drivers.repositories.text import KeyValueReplaceTextRepository
from src.core.repositories.local_file.file_template_renderer_repository import CoreFileTemplateRendererRepository
from src.core.repositories.text import CoreKeyValueReplaceTextRepository

logger = logging.getLogger(__name__)


class FileTemplateRendererRepository(CoreFileTemplateRendererRepository):
    """Recorre archivos y directorios aplicando el reemplazo de tokens. Falla con log si un archivo no es texto válido."""

    def __init__(self, text_replacer: CoreKeyValueReplaceTextRepository | None = None) -> None:
        self._text_replacer = text_replacer or KeyValueReplaceTextRepository()

    def render(self, path: Path, tokens: dict[str, str]) -> None:
        if path.is_symlink():
            return
        if path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and not child.is_symlink():
                    self._render_one(child, tokens)
            return
        if path.is_file():
            self._render_one(path, tokens)

    def _render_one(self, path: Path, tokens: dict[str, str]) -> None:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as e:
            logger.error("[template renderer] cannot read file as text: %s — %s", path, e)
            raise
        if not any(key in text for key in tokens):
            return
        path.write_text(self._text_replacer.replace_text(text, tokens), encoding="utf-8")
