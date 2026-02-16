from src.app.drivers.repositories.pkg_manager._implementations.base_pkg_repository import BasePkgRepository

class PacmanPkgRepository(BasePkgRepository):
    def __init__(self) -> None:
        super().__init__(
            manager_name="pacman",
            install_cmd_prefix=["sudo", "pacman", "-S", "--needed", "--noconfirm"],
            uninstall_cmd_prefix=["sudo", "pacman", "-Rns", "--noconfirm"],
        )
