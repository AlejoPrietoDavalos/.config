from src.app.drivers.repositories.programs._implementations.base_program_repository import BaseProgramRepository
from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles


class PicomRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "picom"
        return ProgramConfig(
            name="picom",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "picom"),
            packages=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["picom"])]),
        )
