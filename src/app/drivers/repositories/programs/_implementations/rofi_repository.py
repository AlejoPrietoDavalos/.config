from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.rofi_repository import CoreRofiRepository


class RofiRepository(CoreRofiRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "rofi"
        return ProgramConfig(
            name="rofi",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "rofi"),
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["rofi"])]),
        )
