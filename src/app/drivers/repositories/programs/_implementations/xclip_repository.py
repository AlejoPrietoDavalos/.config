from pathlib import Path

from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.xclip_repository import CoreXclipRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository


class XclipRepository(CoreXclipRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="xclip",
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["xclip"])]),
        )

    def copy_png_to_clipboard(self, path_png: Path) -> None:
        self._command_repo.run_argv(
            ["xclip", "-selection", "clipboard", "-t", "image/png", "-i", str(path_png)]
        )
