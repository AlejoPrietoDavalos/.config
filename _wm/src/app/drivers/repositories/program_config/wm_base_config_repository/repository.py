from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.app.drivers.repositories.program_config.base_program_repository import BaseProgramRepository


class WmBaseRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="wm-base",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["feh"])]),
        )
