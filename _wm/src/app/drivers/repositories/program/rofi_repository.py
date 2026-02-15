from pathlib import Path

from src.app.drivers.repositories.program.base_program_repository import BaseProgramRepository
from src.core.entities.program_config import ProgramConfig


class RofiRepository(BaseProgramRepository):
    def build(self, config_root: Path) -> ProgramConfig:
        program_root = config_root / "_wm" / "programs" / "rofi"
        return ProgramConfig(
            name="rofi",
            files_dir=program_root / "files",
            target_dir=config_root / "rofi",
            packages_file=program_root / "packages.txt",
        )
