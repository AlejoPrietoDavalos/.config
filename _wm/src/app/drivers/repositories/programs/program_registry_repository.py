from typing import Dict

from src.core.entities.program_config import ProgramName
from src.core.repositories.program_registry_repository import CoreProgramRegistryRepository
from src.core.repositories.program_repository import CoreBaseProgramRepository
from src.app.drivers.repositories.programs import (
    BspwmRepository,
    DisplayToolsRepository,
    KittyRepository,
    NvidiaRepository,
    PicomRepository,
    PolybarRepository,
    PulseaudioRepository,
    RangerRepository,
    RofiRepository,
    SxhkdRepository,
    ThunarRepository,
    VscodeRepository,
    WmBaseRepository,
)

def _get_program_repos() -> Dict[ProgramName, CoreBaseProgramRepository]:
    # FIXME: Ponerle un name a cada repo y usar eso en vez de hardcodear el name acá.
    return {
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


class ProgramRegistryRepository(CoreProgramRegistryRepository):
    def __init__(self) -> None:
        self._repos: Dict[ProgramName, CoreBaseProgramRepository] = _get_program_repos()

    def get_program_repo(self, program: ProgramName) -> CoreBaseProgramRepository:
        repo = self._repos[program]

        cfg = repo.default_config()
        if cfg.files is not None and not cfg.files.source_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files.source_dir}")
        return repo
