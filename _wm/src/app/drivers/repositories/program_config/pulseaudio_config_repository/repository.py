from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.packages import Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository


class PulseaudioConfigRepository(ProgramBuildConfigRepository):
    def build_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "pulseaudio"
        return ProgramConfig(
            name="pulseaudio",
            files_dir=program_root / "files",
            target_dir=path_dotfiles / "pulseaudio",
            packages=Packages(packages=["pulseaudio", "pulseaudio-alsa", "pamixer"]),
        )
