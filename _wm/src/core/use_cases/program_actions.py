from core.repositories.command_repository import CommandRepository
from core.repositories.file_operations_repository import FileOperationsRepository
from core.repositories.package_manager_repository import PackageManagerRepository
from core.repositories.program_config_repository import ProgramConfigRepository


class ProgramActions:
    def __init__(
        self,
        config_repo: ProgramConfigRepository,
        package_repo: PackageManagerRepository,
        file_repo: FileOperationsRepository,
        command_repo: CommandRepository,
    ) -> None:
        self._config_repo = config_repo
        self._package_repo = package_repo
        self._file_repo = file_repo
        self._command_repo = command_repo

    def run(self, action: str, program: str, backup: bool = False) -> None:
        cfg = self._config_repo.get(program)
        use_backup = backup or cfg.backup_files

        if action == "install-requirement":
            self._package_repo.install(program, cfg.packages_file)
            return

        if action == "uninstall-requirement":
            self._package_repo.uninstall(program, cfg.packages_file)
            return

        if action == "install-files":
            self._file_repo.install(cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup)
            for cmd in cfg.post_install_commands:
                self._command_repo.run(cmd)
            return

        if action == "uninstall-files":
            self._file_repo.uninstall(cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup)
            return

        if action == "install":
            self._package_repo.install(program, cfg.packages_file)
            self._file_repo.install(cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup)
            for cmd in cfg.post_install_commands:
                self._command_repo.run(cmd)
            return

        if action == "uninstall":
            self._file_repo.uninstall(cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup)
            self._package_repo.uninstall(program, cfg.packages_file)
            return

        raise ValueError(f"Unknown action: {action}")
