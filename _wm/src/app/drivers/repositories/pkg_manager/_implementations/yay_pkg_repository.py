from src.app.drivers.repositories.pkg_manager._implementations.base_pkg_repository import BasePkgRepository


class YayPkgRepository(BasePkgRepository):
    def __init__(self) -> None:
        super().__init__(
            manager_name="yay",
            install_cmd_prefix=["yay", "-S", "--needed", "--noconfirm"],
            uninstall_cmd_prefix=["yay", "-Rns", "--noconfirm"],
        )
