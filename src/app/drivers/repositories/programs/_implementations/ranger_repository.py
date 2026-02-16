from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.ranger_repository import CoreRangerRepository


class RangerRepository(CoreRangerRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "ranger"
        return ProgramConfig(
            name="ranger",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "ranger"),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["ranger"])]),
        )
