from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.app.drivers.repositories.programs._implementations.base_program_repository import BaseProgramRepository


class PulseaudioRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="pulseaudio",
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["pulseaudio", "pulseaudio-alsa", "pamixer"])]),
        )
