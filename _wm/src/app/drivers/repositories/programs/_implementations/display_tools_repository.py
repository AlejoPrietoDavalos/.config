from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.app.drivers.repositories.programs._implementations.base_program_repository import BaseProgramRepository


class DisplayToolsRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="display-tools",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["xorg-xrandr", "arandr"])]),
        )
