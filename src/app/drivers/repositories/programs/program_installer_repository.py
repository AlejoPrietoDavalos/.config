import logging

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

logger = logging.getLogger(__name__)


class ProgramInstallerRepository(CoreProgramInstallerRepository):
    def __init__(
        self,
        pkg_manager_factory_repo: CorePkgManagerFactoryRepository | None = None,
        file_repo: CoreFileInstallerRepository | None = None,
    ) -> None:
        self._package_repo = pkg_manager_factory_repo or PkgManagerFactoryRepository()
        self._file_repo = file_repo or LocalFileOperationsRepository()

    def install_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.install(cfg.package_dependencies, program_name=cfg.name)

    def uninstall_requirement(self, cfg: ProgramConfig) -> None:
        self._package_repo.uninstall(cfg.package_dependencies, program_name=cfg.name)

    def install_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.install(
                cfg.files.path_folder_config_files_input,
                cfg.files.path_folder_program_dotfile,
            )
        else:
            logger.info("[%s] [files skip] no files configured", cfg.name)
        for action in cfg.post_install_actions:
            action_name = getattr(action, "__name__", action.__class__.__name__)
            logger.info("[%s] [post install] run action=%s", cfg.name, action_name)
            action()
            logger.info("[%s] [post install] done action=%s", cfg.name, action_name)

    def uninstall_files(self, cfg: ProgramConfig) -> None:
        if cfg.files is not None:
            self._file_repo.uninstall(
                cfg.files.path_folder_config_files_input,
                cfg.files.path_folder_program_dotfile,
            )
        else:
            logger.info("[%s] [files delete skip] no files configured", cfg.name)
        for action in cfg.post_uninstall_actions:
            action_name = getattr(action, "__name__", action.__class__.__name__)
            logger.info("[%s] [post uninstall] run action=%s", cfg.name, action_name)
            action()
            logger.info("[%s] [post uninstall] done action=%s", cfg.name, action_name)
