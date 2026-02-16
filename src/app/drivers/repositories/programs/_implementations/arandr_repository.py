from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.arandr_repository import CoreArandrRepository


class ArandrRepository(CoreArandrRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="arandr",
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["arandr"])]),
            program_dependencies=("xorg",),
        )
