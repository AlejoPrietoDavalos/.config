from src.core.constants import path_config_files, path_dotfiles
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.thunar_repository import CoreThunarRepository


class ThunarRepository(CoreThunarRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="thunar",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "thunar",
                path_folder_program_dotfile=path_dotfiles / "Thunar",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["thunar"])]),
        )
