from __future__ import annotations

from abc import ABC
from typing import Sequence

from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository
from src.core.repositories.pkg_manager.pkg_repository import CoreBasePkgRepository


class BasePkgRepository(CoreBasePkgRepository, ABC):
    def __init__(
        self,
        manager_name: str,
        install_cmd_prefix: Sequence[str],
        uninstall_cmd_prefix: Sequence[str],
        command_repo: CoreCommandRepository | None = None,
    ) -> None:
        self._manager_name = manager_name
        self._install_cmd_prefix = tuple(install_cmd_prefix)
        self._uninstall_cmd_prefix = tuple(uninstall_cmd_prefix)
        self._command_repo = command_repo or CommandRepository()

    @property
    def manager_name(self) -> str:
        return self._manager_name

    def _exists(self) -> bool:
        return self._command_repo.command_exists(self._manager_name)

    def _is_installed(self, pkg_name: str) -> bool:
        return self._command_repo.run_argv_quiet([self._manager_name, "-Q", pkg_name]) == 0

    def _run_install(self, pkg_names: list[str]) -> None:
        self._command_repo.run_argv([*self._install_cmd_prefix, *pkg_names])

    def _run_uninstall(self, pkg_names: list[str]) -> None:
        self._command_repo.run_argv([*self._uninstall_cmd_prefix, *pkg_names])

    def install(self, pkg_names: list[str]) -> None:
        if not self._exists():
            print(f"Skip deps: {self._manager_name} not found")
            return
        if not pkg_names:
            return

        missing = [pkg for pkg in pkg_names if not self._is_installed(pkg)]
        if not missing:
            return

        print(f"Installing deps: {' '.join(missing)}")
        self._run_install(missing)

    def uninstall(self, pkg_names: list[str]) -> None:
        if not self._exists():
            return
        if not pkg_names:
            return

        installed = [pkg for pkg in pkg_names if self._is_installed(pkg)]
        if not installed:
            return

        print(f"Removing deps: {' '.join(installed)}")
        self._run_uninstall(installed)
