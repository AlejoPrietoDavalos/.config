from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.pulseaudio_repository import CorePulseaudioRepository


class PulseaudioRepository(CorePulseaudioRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="pulseaudio",
            # Keep only user-facing volume tooling; avoid pulseaudio<->pipewire-pulse conflicts.
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["pamixer"])]),
        )
