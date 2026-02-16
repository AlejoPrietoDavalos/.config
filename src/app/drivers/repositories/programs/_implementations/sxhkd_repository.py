import subprocess

from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.sxhkd_repository import CoreSxhkdRepository


class SxhkdRepository(CoreSxhkdRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="sxhkd",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "sxhkd",
                path_folder_program_dotfile=path_config / "sxhkd",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["sxhkd", "playerctl", "scrot", "xclip"])]),
            post_install_actions=(self.reload_sxhkd,),
        )

    def reload_sxhkd(self) -> None:
        subprocess.run(["pkill", "-USR1", "-x", "sxhkd"], check=False)
