from src.app.drivers.repositories.programs.bspwm_repository import BspwmRepository
from src.app.drivers.repositories.programs.display_tools_repository import DisplayToolsRepository
from src.app.drivers.repositories.programs.kitty_repository import KittyRepository
from src.app.drivers.repositories.programs.nvidia_repository import NvidiaRepository
from src.app.drivers.repositories.programs.picom_repository import PicomRepository
from src.app.drivers.repositories.programs.polybar_repository import PolybarRepository
from src.app.drivers.repositories.programs.pulseaudio_repository import PulseaudioRepository
from src.app.drivers.repositories.programs.ranger_repository import RangerRepository
from src.app.drivers.repositories.programs.rofi_repository import RofiRepository
from src.app.drivers.repositories.programs.sxhkd_repository import SxhkdRepository
from src.app.drivers.repositories.programs.thunar_repository import ThunarRepository
from src.app.drivers.repositories.programs.vscode_repository import VscodeRepository
from src.app.drivers.repositories.programs.wm_base_repository import WmBaseRepository
from src.core.entities.program_config import ProgramName
from src.core.repositories.program_registry_repository import ProgramRegistryRepository as CoreProgramRegistryRepository
from src.core.repositories.program_repository import ProgramRepository


class ProgramRegistryRepository(CoreProgramRegistryRepository):
    def __init__(self) -> None:
        self._repos: dict[ProgramName, ProgramRepository] = {
            "bspwm": BspwmRepository(),
            "sxhkd": SxhkdRepository(),
            "polybar": PolybarRepository(),
            "kitty": KittyRepository(),
            "ranger": RangerRepository(),
            "picom": PicomRepository(),
            "rofi": RofiRepository(),
            "thunar": ThunarRepository(),
            "vscode": VscodeRepository(),
            "wm-base": WmBaseRepository(),
            "pulseaudio": PulseaudioRepository(),
            "display-tools": DisplayToolsRepository(),
            "nvidia": NvidiaRepository(),
        }

    def get_program(self, program: ProgramName) -> ProgramRepository:
        repo = self._repos.get(program)
        if repo is None:
            raise ValueError(f"Program not found: {program}")

        cfg = repo.default_config()
        if cfg.files is not None and not cfg.files.source_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files.source_dir}")
        return repo
