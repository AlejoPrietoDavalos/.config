from src.core.entities.program import ProgramName
from src.core.repositories.command_repository import CommandRepository
from src.core.repositories.file_operations_repository import FileOperationsRepository
from src.core.repositories.package_manager_repository import PackageManagerRepository
from src.core.repositories.program_config.program_config_repository import ProgramConfigRepository


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

    def run(self, action: str, program: ProgramName, backup: bool = False) -> None:
        cfg = self._config_repo.get_config(program)
        use_backup = backup or cfg.backup_files

        if action == "install-requirement":
            for dep in self._resolve_dependency_order(program):
                dep_cfg = self._config_repo.get_config(dep)
                self._package_repo.install(dep, dep_cfg.packages)
            return

        if action == "uninstall-requirement":
            self._package_repo.uninstall(program, cfg.packages)
            return

        if action == "install-files":
            if cfg.files_dir is not None and cfg.target_dir is not None:
                self._file_repo.install(
                    cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup
                )
            for cmd in cfg.post_install_commands:
                self._command_repo.run(cmd)
            return

        if action == "uninstall-files":
            if cfg.files_dir is not None and cfg.target_dir is not None:
                self._file_repo.uninstall(
                    cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup
                )
            return

        if action == "install":
            for dep in self._resolve_dependency_order(program):
                dep_cfg = self._config_repo.get_config(dep)
                self._package_repo.install(dep, dep_cfg.packages)
            if cfg.files_dir is not None and cfg.target_dir is not None:
                self._file_repo.install(
                    cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup
                )
            for cmd in cfg.post_install_commands:
                self._command_repo.run(cmd)
            return

        if action == "uninstall":
            if cfg.files_dir is not None and cfg.target_dir is not None:
                self._file_repo.uninstall(
                    cfg.files_dir, cfg.target_dir, cfg.files_mode, backup=use_backup
                )
            self._package_repo.uninstall(program, cfg.packages)
            return

        raise ValueError(f"Unknown action: {action}")

    def _resolve_dependency_order(self, program: ProgramName) -> list[ProgramName]:
        ordered: list[ProgramName] = []
        visited: set[ProgramName] = set()
        in_stack: set[ProgramName] = set()

        def visit(name: ProgramName) -> None:
            if name in visited:
                return
            if name in in_stack:
                raise ValueError(f"Cyclic dependency detected at program: {name}")
            in_stack.add(name)
            cfg = self._config_repo.get_config(name)
            for dep in cfg.dependencies:
                visit(dep)
            in_stack.remove(name)
            visited.add(name)
            ordered.append(name)

        visit(program)
        return ordered
