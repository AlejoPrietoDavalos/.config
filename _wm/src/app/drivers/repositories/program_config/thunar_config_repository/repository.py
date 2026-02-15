from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository
from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PackageSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles


class ThunarConfigRepository(ProgramBuildConfigRepository):
    def build_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "thunar"
        return ProgramConfig(
            name="thunar",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "Thunar"),
            packages=Packages(packages=[PackageSpec(manager="pacman", names=["thunar"])]),
        )
