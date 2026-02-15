from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository
from src.app.drivers.repositories.program_config.bspwm_config_repository.repository import BspwmConfigRepository
from src.app.drivers.repositories.program_config.picom_config_repository.repository import PicomConfigRepository
from src.app.drivers.repositories.program_config.polybar_config_repository.repository import PolybarConfigRepository
from src.app.drivers.repositories.program_config.ranger_config_repository.repository import RangerConfigRepository
from src.app.drivers.repositories.program_config.rofi_config_repository.repository import RofiConfigRepository
from src.app.drivers.repositories.program_config.sxhkd_config_repository.repository import SxhkdConfigRepository
from src.app.drivers.repositories.program_config.thunar_config_repository.repository import ThunarConfigRepository
from src.app.drivers.repositories.program_config.vscode_config_repository.repository import VscodeConfigRepository
from src.core.entities.program import ProgramName
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_config_repository import ProgramConfigRepository


class ProgramConfigRegistryRepository(ProgramConfigRepository):
    def __init__(self) -> None:
        self._repos: dict[ProgramName, ProgramBuildConfigRepository] = {
            "bspwm": BspwmConfigRepository(),
            "sxhkd": SxhkdConfigRepository(),
            "polybar": PolybarConfigRepository(),
            "ranger": RangerConfigRepository(),
            "picom": PicomConfigRepository(),
            "rofi": RofiConfigRepository(),
            "thunar": ThunarConfigRepository(),
            "vscode": VscodeConfigRepository(),
        }

    def get_config(self, program: ProgramName) -> ProgramConfig:
        repo = self._repos.get(program)
        if repo is None:
            raise ValueError(f"Program not found: {program}")
        cfg = repo.build_config()
        if not cfg.files_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files_dir}")
        return cfg
