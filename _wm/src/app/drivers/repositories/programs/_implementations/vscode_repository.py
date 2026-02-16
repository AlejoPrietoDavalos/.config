from src.core.constants import path_dotfiles, path_wm_programs
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs.vscode_repository import CoreVscodeRepository


class VscodeRepository(CoreVscodeRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "vscode"
        return ProgramConfig(
            name="vscode",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "Code" / "User"),
            packages=Packages(pkg_specs=[PkgSpec(manager="yay", names=["code"])]),
        )
