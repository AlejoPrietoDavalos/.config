from src.core.constants import path_dotfiles, path_wm_programs, path_wm_scripts
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.sxhkd_repository import CoreSxhkdRepository


class SxhkdRepository(CoreSxhkdRepository):
    def default_config(self) -> ProgramConfig:
        program_root = path_wm_programs / "sxhkd"
        return ProgramConfig(
            name="sxhkd",
            files=ProgramFiles(source_dir=program_root / "files", target_dir=path_dotfiles / "sxhkd"),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["sxhkd", "playerctl", "scrot", "xclip"])]),
            post_install_commands=(str(path_wm_scripts / "generate_sxhkd.sh"),),
        )
