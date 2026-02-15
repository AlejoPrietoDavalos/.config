from pathlib import Path

from app.drivers.repositories.program.base_program_repository import BaseProgramRepository
from app.drivers.repositories.program.bspwm_repository import BspwmRepository
from app.drivers.repositories.program.picom_repository import PicomRepository
from app.drivers.repositories.program.polybar_repository import PolybarRepository
from app.drivers.repositories.program.ranger_repository import RangerRepository
from app.drivers.repositories.program.rofi_repository import RofiRepository
from app.drivers.repositories.program.sxhkd_repository import SxhkdRepository
from app.drivers.repositories.program.thunar_repository import ThunarRepository
from app.drivers.repositories.program.vscode_repository import VscodeRepository
from core.entities.program_config import ProgramConfig
from core.repositories.program_config_repository import ProgramConfigRepository


class ProgramRegistryRepository(ProgramConfigRepository):
    def __init__(self, config_root: Path) -> None:
        self._config_root = config_root
        self._repos: dict[str, BaseProgramRepository] = {
            "bspwm": BspwmRepository(),
            "sxhkd": SxhkdRepository(),
            "polybar": PolybarRepository(),
            "ranger": RangerRepository(),
            "picom": PicomRepository(),
            "rofi": RofiRepository(),
            "thunar": ThunarRepository(),
            "vscode": VscodeRepository(),
        }

    def get(self, program: str) -> ProgramConfig:
        repo = self._repos.get(program)
        if repo is None:
            raise ValueError(f"Program not found: {program}")
        cfg = repo.build(self._config_root)
        if not cfg.files_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files_dir}")
        return cfg
