from src.core.entities.program_config import PackageSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository


class WmBaseConfigRepository(ProgramBuildConfigRepository):
    def build_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="wm-base",
            packages=Packages(packages=[PackageSpec(manager="pacman", names=["feh"])]),
        )
