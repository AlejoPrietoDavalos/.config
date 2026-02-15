from __future__ import annotations

import os
import shutil
import subprocess

from src.core.entities.program_config import ProgramName


class YayPackageRepository:
    def _exists(self) -> bool:
        return shutil.which("yay") is not None

    def install(self, program: ProgramName, package_names: list[str]) -> None:
        if not self._exists():
            print(f"Skip deps for '{program}': yay not found")
            return
        if not package_names:
            return

        missing = [
            pkg
            for pkg in package_names
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

    def uninstall(self, program: ProgramName, package_names: list[str]) -> None:
        if os.getenv("WM_REMOVE_PACKAGES") != "1":
            return
        if not self._exists():
            return
        if not package_names:
            return

        installed = [
            pkg
            for pkg in package_names
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
