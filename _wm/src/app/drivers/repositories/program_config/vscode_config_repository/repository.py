from src.app.drivers.repositories.program_config.base_program_repository import BaseProgramRepository
from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles


class VscodeRepository(BaseProgramRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "vscode"
        return ProgramConfig(
            name="vscode",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "Code" / "User"),
            packages=Packages(pkg_specs=[PkgSpec(manager="yay", names=["code"])]),
            backup_files=False,
        )
