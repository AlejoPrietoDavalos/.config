from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from src.core.repositories.package_manager_repository import PackageManagerRepository


class PacmanPackageRepository(PackageManagerRepository):
    def _read_packages(self, packages_file: Path) -> list[str]:
        if not packages_file.exists():
            return []
        items: list[str] = []
        for raw in packages_file.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            items.append(line.split()[0])
        return items

    def _exists(self) -> bool:
        return shutil.which("pacman") is not None

    def install(self, program: str, packages_file: Path) -> None:
        if not self._exists():
            print(f"Skip deps for '{program}': pacman not found")
            return

        packages = self._read_packages(packages_file)
        if not packages:
            return

        missing = [
            pkg
            for pkg in packages
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

    def uninstall(self, program: str, packages_file: Path) -> None:
        if os.getenv("WM_REMOVE_PACKAGES") != "1":
            return
        if not self._exists():
            return

        packages = self._read_packages(packages_file)
        if not packages:
            return

        installed = [
            pkg
            for pkg in packages
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
