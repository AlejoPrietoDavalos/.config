from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.ranger_repository import CoreRangerRepository


class RangerRepository(CoreRangerRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="ranger",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "ranger",
                path_folder_program_dotfile=path_config / "ranger",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["ranger"])]),
        )
