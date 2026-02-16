from src.core.entities.program_config import ProgramName
from src.core.repositories.programs import CoreProgramFactoryRepository, CoreProgramInstallerRepository


class ProgramActions:
    # TODO: Revisar esta clase, no me convence del todo como está implementada, pero por ahora funciona.
    def __init__(
        self,
        program_factory_repo: CoreProgramFactoryRepository,
        program_installer_repo: CoreProgramInstallerRepository,
    ) -> None:
        self._program_factory_repo = program_factory_repo
        self._program_installer_repo = program_installer_repo

    def run(self, action: str, program: ProgramName | None = None) -> None:
        if action == "dirty_install_all_packages":
            self._dirty_install_all_packages()
            return

        if program is None:
            raise ValueError(f"Action '{action}' requires --program")

        program_repo = self._program_factory_repo.get_program_repo(program)
        program_cfg = program_repo.default_config()

        if action == "install-requirement":
            for dep in self._resolve_dependency_order(program):
                dep_cfg = self._program_factory_repo.get_program_repo(dep).default_config()
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
                dep_cfg = self._program_factory_repo.get_program_repo(dep).default_config()
                self._program_installer_repo.install_requirement(dep_cfg)
            self._program_installer_repo.install_files(program_cfg)
            return

        if action == "uninstall":
            self._program_installer_repo.uninstall_files(program_cfg)
            self._program_installer_repo.uninstall_requirement(program_cfg)
            return

        raise ValueError(f"Unknown action: {action}")

    def _dirty_install_all_packages(self) -> None:
        for program in self._program_factory_repo.list_programs():
            try:
                program_repo = self._program_factory_repo.get_program_repo(program)
                program_cfg = program_repo.default_config()
                self._program_installer_repo.install_requirement(program_cfg)
                self._program_installer_repo.install_files(program_cfg)
            except Exception:
                continue

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
            cfg = self._program_factory_repo.get_program_repo(name).default_config()
            for dep in cfg.program_dependencies:
                visit(dep)
            in_stack.remove(name)
            visited.add(name)
            ordered.append(name)

        visit(program)
        return ordered
