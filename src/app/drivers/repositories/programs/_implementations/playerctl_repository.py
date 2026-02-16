from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.playerctl_repository import (
    CorePlayerctlRepository,
    PlayerctlAction,
)
from src.core.repositories.shell.command_repository import CoreCommandRepository


class PlayerctlRepository(CorePlayerctlRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="playerctl",
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="pacman", names=["playerctl"])]),
        )

    def run(self, action: PlayerctlAction) -> None:
        if action == "previous":
            self.previous()
        elif action == "next":
            self.next()
        elif action == "play_pause":
            self.play_pause()
        elif action == "stop":
            self.stop()
        else:
            raise ValueError(f"Unsupported action: {action}")

    def previous(self) -> None:
        self._command_repo.run_argv_quiet(["playerctl", "previous"])

    def next(self) -> None:
        self._command_repo.run_argv_quiet(["playerctl", "next"])

    def play_pause(self) -> None:
        self._command_repo.run_argv_quiet(["playerctl", "play-pause"])

    def stop(self) -> None:
        self._command_repo.run_argv_quiet(["playerctl", "stop"])
