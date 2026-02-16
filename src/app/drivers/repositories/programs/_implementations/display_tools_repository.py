from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.display_tools_repository import CoreDisplayToolsRepository


class DisplayToolsRepository(CoreDisplayToolsRepository):
    # FIXME: Mismo que wm_base, hace falta? o como ponerlo?
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="display-tools",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["xorg-xrandr", "arandr"])]),
        )
