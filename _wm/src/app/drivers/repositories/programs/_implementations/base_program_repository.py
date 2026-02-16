from src.app.drivers.repositories.files.local_file_operations_repository import LocalFileOperationsRepository
from src.app.drivers.repositories.pkg_manager.factory_repository import PkgManagerFactoryRepository
from src.app.drivers.repositories.programs._implementations.command_repository import CommandRepository
from src.core.repositories.command_repository import CoreCommandRepository
from src.core.repositories.file_operations_repository import FileOperationsRepository
from src.core.repositories.pkg_manager.factory_repository import (
    CorePkgManagerFactoryRepository,
)
from src.core.repositories.program_repository import CoreBaseProgramRepository


class BaseProgramRepository(CoreBaseProgramRepository):
    def __init__(
        self,
        package_repo: CorePkgManagerFactoryRepository | None = None,
        file_repo: FileOperationsRepository | None = None,
        command_repo: CoreCommandRepository | None = None,
    ) -> None:
        self._package_repo = package_repo or PkgManagerFactoryRepository()
        self._file_repo = file_repo or LocalFileOperationsRepository()
        self._command_repo = command_repo or CommandRepository()

    def install_requirement(self) -> None:
        cfg = self.default_config()
        self._package_repo.install(cfg.packages)

    def uninstall_requirement(self) -> None:
        cfg = self.default_config()
        self._package_repo.uninstall(cfg.packages)

    def install_files(self) -> None:
        cfg = self.default_config()
        if cfg.files is not None:
            self._file_repo.install(cfg.files.source_dir, cfg.files.target_dir, cfg.files.mode)
        for cmd in cfg.post_install_commands:
            self._command_repo.run(cmd)

    def uninstall_files(self) -> None:
        cfg = self.default_config()
        if cfg.files is not None:
            self._file_repo.uninstall(cfg.files.source_dir, cfg.files.target_dir, cfg.files.mode)
