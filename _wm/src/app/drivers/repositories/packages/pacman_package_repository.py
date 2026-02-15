from __future__ import annotations

import os
import shutil
import subprocess

from src.core.entities.program import ProgramName


class PacmanPackageRepository:
    def _exists(self) -> bool:
        return shutil.which("pacman") is not None

    def install(self, program: ProgramName, package_names: list[str]) -> None:
        if not self._exists():
            print(f"Skip deps for '{program}': pacman not found")
            return

        if not package_names:
            return

        missing = [
            pkg
            for pkg in package_names
            if subprocess.run(
                ["pacman", "-Q", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            != 0
        ]
        if not missing:
            return

        print(f"Installing deps for '{program}': {' '.join(missing)}")
        subprocess.run(
            ["sudo", "pacman", "-S", "--needed", "--noconfirm", *missing], check=True
        )

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
                ["pacman", "-Q", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        ]
        if not installed:
            return

        print(f"Removing deps for '{program}': {' '.join(installed)}")
        subprocess.run(
            ["sudo", "pacman", "-Rns", "--noconfirm", *installed], check=True
        )
