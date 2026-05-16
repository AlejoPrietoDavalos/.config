from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.polybar_repository import CorePolybarRepository


class PolybarRepository(CorePolybarRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="polybar",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "polybar",
                path_folder_program_dotfile=path_config / "polybar",
            ),
            package_dependencies=Packages(
                pkg_specs=[
                    PkgSpec(
                        manager="pacman",
                        names=["polybar", "networkmanager", "libnotify"],
                    )
                ]
            ),
            program_dependencies=("pulseaudio",),
        )
