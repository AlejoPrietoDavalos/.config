from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository
from src.core.repositories.programs._implementations.bspwm_repository import CoreBspwmRepository


class BspwmRepository(CoreBspwmRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="bspwm",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "bspwm",
                path_folder_program_dotfile=path_config / "bspwm",
            ),
            package_dependencies=Packages(
                pkg_specs=[PkgSpec(manager="pacman", names=["bspwm", "xorg-setxkbmap", "feh"])]
            ),
            program_dependencies=("arandr",),
        )

    def list_monitors(self) -> list[str]:
        try:
            out = self._command_repo.run_capture("bspc query -M --names")
        except Exception:
            return []
        return [line.strip() for line in out.splitlines() if line.strip()]

    def set_monitor_desktops(self, monitor: str, desktops: list[str]) -> None:
        if not desktops:
            return
        quoted = " ".join(f"'{d}'" for d in desktops)
        self._command_repo.run(f"bspc monitor '{monitor}' -d {quoted}")
