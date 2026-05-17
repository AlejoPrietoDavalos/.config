from src.core.constants import path_config_files, path_dotfiles
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.rofi_repository import CoreRofiRepository


class RofiRepository(CoreRofiRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="rofi",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "rofi",
                path_folder_program_dotfile=path_dotfiles / "rofi",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["rofi"])]),
        )
