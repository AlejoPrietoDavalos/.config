from src.app.drivers.repositories.packages.pacman_package_repository import PacmanPackageRepository
from src.app.drivers.repositories.packages.yay_package_repository import YayPackageRepository
from src.core.entities.program_config import PackageManager, Packages, ProgramName
from src.core.repositories.package_manager_repository import PackageManagerRepository


class ProgramPackageManagerRepository(PackageManagerRepository):
    def __init__(self) -> None:
        self._package_repos: dict[PackageManager, object] = {
            "pacman": PacmanPackageRepository(),
            "yay": YayPackageRepository(),
        }

    def _repo_for_manager(self, manager: PackageManager) -> object:
        return self._package_repos[manager]

    def install(self, program: ProgramName, packages: Packages) -> None:
        for spec in packages.packages:
            repo = self._repo_for_manager(spec.manager)
            repo.install(program, spec.names)

    def uninstall(self, program: ProgramName, packages: Packages) -> None:
        for spec in packages.packages:
            repo = self._repo_for_manager(spec.manager)
            repo.uninstall(program, spec.names)
