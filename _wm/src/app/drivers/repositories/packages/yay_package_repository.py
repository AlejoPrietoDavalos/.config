from __future__ import annotations

import os
import shutil
import subprocess

from src.core.entities.packages import Packages
from src.core.entities.program import ProgramName
from src.core.entities.program_config import PackageManager
from src.core.repositories.package_manager_repository import PackageManagerRepository


class YayPackageRepository(PackageManagerRepository):
    def _exists(self) -> bool:
        return shutil.which("yay") is not None

    def install(
        self, program: ProgramName, packages: Packages, manager: PackageManager = "yay"
    ) -> None:
        if not self._exists():
            print(f"Skip deps for '{program}': yay not found")
            return
        if not packages.packages:
            return

        missing = [
            pkg
            for pkg in packages.packages
            if subprocess.run(
                ["yay", "-Q", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            != 0
        ]
        if not missing:
            return

        print(f"Installing deps for '{program}' (yay): {' '.join(missing)}")
        subprocess.run(["yay", "-S", "--needed", "--noconfirm", *missing], check=True)

    def uninstall(
        self, program: ProgramName, packages: Packages, manager: PackageManager = "yay"
    ) -> None:
        if os.getenv("WM_REMOVE_PACKAGES") != "1":
            return
        if not self._exists():
            return
        if not packages.packages:
            return

        installed = [
            pkg
            for pkg in packages.packages
            if subprocess.run(
                ["yay", "-Q", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        ]
        if not installed:
            return

        print(f"Removing deps for '{program}' (yay): {' '.join(installed)}")
        subprocess.run(["yay", "-Rns", "--noconfirm", *installed], check=True)
