from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs.display_tools_repository import CoreDisplayToolsRepository


class DisplayToolsRepository(CoreDisplayToolsRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="display-tools",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["xorg-xrandr", "arandr"])]),
        )
