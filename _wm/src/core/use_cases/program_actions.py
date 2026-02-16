from src.core.entities.program_config import ProgramName
from src.core.repositories.pkg_manager.program_installer_repository import (
    ProgramInstallerRepository,
)
from src.core.repositories.programs.program_factory_repository import CoreProgramFactoryRepository


class ProgramActions:
    def __init__(
        self,
        program_registry_repo: CoreProgramFactoryRepository,
        program_installer_repo: ProgramInstallerRepository,
    ) -> None:
        self._program_registry_repo = program_registry_repo
        self._program_installer_repo = program_installer_repo

    def run(self, action: str, program: ProgramName) -> None:
        program_repo = self._program_registry_repo.get_program_repo(program)
        program_cfg = program_repo.default_config()

        if action == "install-requirement":
            for dep in self._resolve_dependency_order(program):
                dep_cfg = self._program_registry_repo.get_program_repo(dep).default_config()
                self._program_installer_repo.install_requirement(dep_cfg)
            return

        if action == "uninstall-requirement":
            self._program_installer_repo.uninstall_requirement(program_cfg)
            return

        if action == "install-files":
            self._program_installer_repo.install_files(program_cfg)
            return

        if action == "uninstall-files":
            self._program_installer_repo.uninstall_files(program_cfg)
            return

        if action == "install":
            for dep in self._resolve_dependency_order(program):
                dep_cfg = self._program_registry_repo.get_program_repo(dep).default_config()
                self._program_installer_repo.install_requirement(dep_cfg)
            self._program_installer_repo.install_files(program_cfg)
            return

        if action == "uninstall":
            self._program_installer_repo.uninstall_files(program_cfg)
            self._program_installer_repo.uninstall_requirement(program_cfg)
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
            cfg = self._program_registry_repo.get_program_repo(name).default_config()
            for dep in cfg.dependencies:
                visit(dep)
            in_stack.remove(name)
            visited.add(name)
            ordered.append(name)

        visit(program)
        return ordered
