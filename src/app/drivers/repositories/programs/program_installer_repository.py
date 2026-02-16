from src.app.drivers.repositories.local_file.local_file_operations_repository import (
    LocalFileOperationsRepository,
)
from src.app.drivers.repositories.pkg_manager.factory_repository import (
    PkgManagerFactoryRepository,
)
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.local_file import CoreFileInstallerRepository
from src.core.repositories.pkg_manager import CorePkgManagerFactoryRepository
from src.core.repositories.programs import CoreProgramInstallerRepository


class ProgramInstallerRepository(CoreProgramInstallerRepository):
    def __init__(
        self,
        pkg_manager_factory_repo: CorePkgManagerFactoryRepository | None = None,
        file_repo: CoreFileInstallerRepository | None = None,
    ) -> None:
        self._package_repo = pkg_manager_factory_repo or PkgManagerFactoryRepository()
        self._file_repo = file_repo or LocalFileOperationsRepository()

    def install_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.install(cfg.package_dependencies)

    def uninstall_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.uninstall(cfg.package_dependencies)

    def install_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.install(
                cfg.files.path_folder_config_files_input,
                cfg.files.path_folder_program_dotfile,
            )
        for action in cfg.post_install_actions:
            action()

    def uninstall_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.uninstall(
                cfg.files.path_folder_config_files_input,
                cfg.files.path_folder_program_dotfile,
            )
        for action in cfg.post_uninstall_actions:
            action()
