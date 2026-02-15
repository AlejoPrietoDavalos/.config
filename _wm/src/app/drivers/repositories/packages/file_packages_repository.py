from pathlib import Path

from src.core.entities.packages import Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.packages_repository import PackagesRepository


class FilePackagesRepository(PackagesRepository):
    def _read_packages_file(self, packages_file: Path) -> list[str]:
        if not packages_file.exists():
            return []
        items: list[str] = []
        for raw in packages_file.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            items.append(line.split()[0])
        return items

    def get(self, cfg: ProgramConfig) -> Packages:
        return Packages(packages=self._read_packages_file(cfg.packages_file))
