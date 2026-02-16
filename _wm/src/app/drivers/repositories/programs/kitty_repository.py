from src.app.drivers.repositories.programs.base_program_repository import BaseProgramRepository
from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles


class KittyRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "kitty"
        return ProgramConfig(
            name="kitty",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "kitty"),
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["kitty"])]),
        )
