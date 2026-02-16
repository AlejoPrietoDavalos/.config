from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.pulseaudio_repository import CorePulseaudioRepository


class PulseaudioRepository(CorePulseaudioRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="pulseaudio",
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["pulseaudio", "pulseaudio-alsa", "pamixer"])]),
        )
