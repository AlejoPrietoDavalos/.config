from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository
from src.core.constants import path_dotfiles, path_wm_programs, path_wm_scripts
from src.core.entities.packages import PackageSpec, Packages
from src.core.entities.program_config import ProgramConfig


class SxhkdConfigRepository(ProgramBuildConfigRepository):
    def build_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "sxhkd"
        return ProgramConfig(
            name="sxhkd",
            files_dir=program_root / "files",
            target_dir=path_dotfiles / "sxhkd",
            packages=Packages(packages=[PackageSpec(manager="pacman", names=["sxhkd", "playerctl", "scrot", "xclip"])]),
            post_install_commands=(str(path_wm_scripts / "generate_sxhkd.sh"),),
        )
