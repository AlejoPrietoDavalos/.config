from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.picom_repository import CorePicomRepository


class PicomRepository(CorePicomRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="picom",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "picom",
                path_folder_program_dotfile=path_config / "picom",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["picom"])]),
        )
