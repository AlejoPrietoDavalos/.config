from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.packages import Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository


class NvidiaConfigRepository(ProgramBuildConfigRepository):
    """NVIDIA policy for this repo.

    We always prefer NVIDIA's proprietary stack installed from distro repos
    (never the manual .run installer from NVIDIA website). In this environment
    the packaged kernel module available in repos is `nvidia-open`.
    """

    def build_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "nvidia"
        return ProgramConfig(
            name="nvidia",
            files_dir=program_root / "files",
            target_dir=path_dotfiles / "nvidia",
            packages=Packages(
                packages=["nvidia-open", "nvidia-utils", "nvidia-settings", "nvidia-prime"]
            ),
        )
