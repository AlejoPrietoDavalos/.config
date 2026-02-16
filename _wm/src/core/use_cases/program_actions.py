from src.core.entities.program_config import ProgramName
from src.core.repositories.program_registry_repository import CoreProgramRegistryRepository


class ProgramActions:
    def __init__(self, program_registry_repo: CoreProgramRegistryRepository) -> None:
        self._program_registry_repo = program_registry_repo

    def run(self, action: str, program: ProgramName) -> None:
        program_repo = self._program_registry_repo.get_program_repo(program)

        if action == "install-requirement":
            for dep in self._resolve_dependency_order(program):
                self._program_registry_repo.get_program_repo(dep).install_requirement()
            return

        if action == "uninstall-requirement":
            program_repo.uninstall_requirement()
            return

        if action == "install-files":
            program_repo.install_files()
            return

        if action == "uninstall-files":
            program_repo.uninstall_files()
            return

        if action == "install":
            for dep in self._resolve_dependency_order(program):
                self._program_registry_repo.get_program_repo(dep).install_requirement()
            program_repo.install_files()
            return

        if action == "uninstall":
            program_repo.uninstall_files()
            program_repo.uninstall_requirement()
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
