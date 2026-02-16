from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs.thunar_repository import CoreThunarRepository


class ThunarRepository(CoreThunarRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "thunar"
        return ProgramConfig(
            name="thunar",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "Thunar"),
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["thunar"])]),
        )
