from src.app.drivers.repositories.pkg_manager import PacmanPkgRepository, YayPkgRepository
from src.core.entities.program_config import PkgManager, Packages
from src.core.repositories.pkg_repository import CorePkgRepository
from src.core.repositories.pkg_manager.factory_repository import CorePkgManagerFactoryRepository


def _get_available_pkg_managers() -> tuple[CorePkgRepository, ...]:
    return (
        PacmanPkgRepository(),
        YayPkgRepository(),
    )


class PkgManagerFactoryRepository(CorePkgManagerFactoryRepository):
    def __init__(self) -> None:
        self._pkg_repos: dict[str, CorePkgRepository] = {
            repo.manager_name: repo for repo in _get_available_pkg_managers()
        }

    def _manager2repo(self, manager: PkgManager) -> CorePkgRepository:
        return self._pkg_repos[manager]

    def install(self, pkgs: Packages) -> None:
        for pkg_spec in pkgs.pkg_specs:
            repo = self._manager2repo(pkg_spec.manager)
            repo.install(pkg_spec.names)

    def uninstall(self, pkgs: Packages) -> None:
        for pkg_spec in pkgs.pkg_specs:
            repo = self._manager2repo(pkg_spec.manager)
            repo.uninstall(pkg_spec.names)
