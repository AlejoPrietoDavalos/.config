from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.xorg_repository import CoreXorgRepository


class XorgRepository(CoreXorgRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="xorg",
            package_dependencies=Packages(
                pkg_specs=[PkgSpec(manager="pacman", names=["xorg-server", "xorg-xinit", "xorg-xrandr"])]
            ),
        )
