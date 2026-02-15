from pathlib import Path

from app.drivers.repositories.program.base_program_repository import BaseProgramRepository
from core.entities.program_config import ProgramConfig


class ThunarRepository(BaseProgramRepository):
    def build(self, config_root: Path) -> ProgramConfig:
        program_root = config_root / "_wm" / "programs" / "thunar"
        return ProgramConfig(
            name="thunar",
            files_dir=program_root / "files",
            target_dir=config_root / "Thunar",
            packages_file=program_root / "packages.txt",
        )
