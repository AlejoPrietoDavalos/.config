from abc import ABC, abstractmethod
from pathlib import Path


class CoreFileTemplateRendererRepository(ABC):
    """Reemplaza tokens en archivos de texto dado un diccionario clave-valor."""

    @abstractmethod
    def render(self, path: Path, tokens: dict[str, str]) -> None: ...
