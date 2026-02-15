from src.core.entities.packages import PackageSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository


class DisplayToolsConfigRepository(ProgramBuildConfigRepository):
    def build_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="display-tools",
            packages=Packages(packages=[PackageSpec(manager="pacman", names=["xorg-xrandr", "arandr"])]),
        )
