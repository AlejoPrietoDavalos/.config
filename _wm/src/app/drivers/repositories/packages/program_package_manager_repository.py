from src.app.drivers.repositories.packages.pacman_package_repository import PacmanPackageRepository
from src.app.drivers.repositories.packages.yay_package_repository import YayPackageRepository
from src.core.entities.packages import Packages
from src.core.entities.program import ProgramName
from src.core.entities.program_config import PackageManager
from src.core.repositories.package_manager_repository import PackageManagerRepository


class ProgramPackageManagerRepository(PackageManagerRepository):
    def __init__(self) -> None:
        self._package_repos: dict[PackageManager, PackageManagerRepository] = {
            "pacman": PacmanPackageRepository(),
            "yay": YayPackageRepository(),
        }

    def _repo_for_manager(self, manager: PackageManager) -> PackageManagerRepository:
        return self._package_repos[manager]

    def install(
        self, program: ProgramName, packages: Packages, manager: PackageManager = "pacman"
    ) -> None:
        self._repo_for_manager(manager).install(program, packages, manager=manager)

    def uninstall(
        self, program: ProgramName, packages: Packages, manager: PackageManager = "pacman"
    ) -> None:
        self._repo_for_manager(manager).uninstall(program, packages, manager=manager)
