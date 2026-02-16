from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.wm_base_repository import CoreWmBaseRepository


class WmBaseRepository(CoreWmBaseRepository):
    # FIXME: No es un programa, es como un empaquetado, ver donde meterlo.
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="wm-base",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["feh"])]),
        )
