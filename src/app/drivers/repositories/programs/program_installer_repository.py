from src.app.drivers.repositories.local_file.local_file_operations_repository import (
    LocalFileOperationsRepository,
)
from src.app.drivers.repositories.pkg_manager.factory_repository import (
    PkgManagerFactoryRepository,
)
from src.app.drivers.repositories.shell.command_repository import (
    CommandRepository,
)
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.shell import CoreCommandRepository
from src.core.repositories.local_file import CoreFileInstallerRepository
from src.core.repositories.pkg_manager import CorePkgManagerFactoryRepository
from src.core.repositories.programs import CoreProgramInstallerRepository


class ProgramInstallerRepository(CoreProgramInstallerRepository):
    def __init__(
        self,
        pkg_manager_factory_repo: CorePkgManagerFactoryRepository | None = None,
        file_repo: CoreFileInstallerRepository | None = None,
        command_repo: CoreCommandRepository | None = None,
    ) -> None:
        self._package_repo = pkg_manager_factory_repo or PkgManagerFactoryRepository()
        self._file_repo = file_repo or LocalFileOperationsRepository()
        self._command_repo = command_repo or CommandRepository()

    def install_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.install(cfg.packages)

    def uninstall_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.uninstall(cfg.packages)

    def install_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.install(cfg.files.source_dir, cfg.files.target_dir, cfg.files.mode)
        for cmd in cfg.post_install_commands:
            self._command_repo.run(cmd)

    def uninstall_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.uninstall(cfg.files.source_dir, cfg.files.target_dir, cfg.files.mode)
