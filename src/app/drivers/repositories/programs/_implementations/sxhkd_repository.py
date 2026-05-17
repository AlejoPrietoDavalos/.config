from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.constants import path_config_files, path_dotfiles
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.sxhkd_repository import CoreSxhkdRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository

_BROWSER = "firefox"


class SxhkdRepository(CoreSxhkdRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="sxhkd",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "sxhkd",
                path_folder_program_dotfile=path_dotfiles / "sxhkd",
                extra_tokens={
                    "{{COMMAND_OPEN_BROWSER}}": _BROWSER,
                    "{{COMMAND_OPEN_INCOGNITO}}": f"{_BROWSER} --private-window",
                },
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["sxhkd"])]),
            program_dependencies=("playerctl", "scrot", "xclip"),
            post_install_actions=(self.reload_sxhkd,),
        )

    def reload_sxhkd(self) -> None:
        self._command_repo.run_argv_quiet(["pkill", "-USR1", "-x", "sxhkd"])
