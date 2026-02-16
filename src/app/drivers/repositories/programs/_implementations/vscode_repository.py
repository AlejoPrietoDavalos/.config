from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.vscode_repository import CoreVscodeRepository


class VscodeRepository(CoreVscodeRepository):
    # TODO: Renombrar a "code"
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="vscode",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "vscode",
                path_folder_program_dotfile=path_config / "Code" / "User",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="yay", names=["code"])]),
        )
