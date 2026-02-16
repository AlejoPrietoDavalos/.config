from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository
from src.core.repositories.programs._implementations.bspwm_repository import CoreBspwmRepository


class BspwmRepository(CoreBspwmRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

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

    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "bspwm"
        return ProgramConfig(
            name="bspwm",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "bspwm"),
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["bspwm", "xorg-setxkbmap"])]),
            dependencies=("wm-base", "display-tools"),
        )
