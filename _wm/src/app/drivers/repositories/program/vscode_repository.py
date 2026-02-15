from pathlib import Path

from app.drivers.repositories.program.base_program_repository import BaseProgramRepository
from core.entities.program_config import ProgramConfig


class VscodeRepository(BaseProgramRepository):
    def build(self, config_root: Path) -> ProgramConfig:
        program_root = config_root / "_wm" / "programs" / "vscode"
        return ProgramConfig(
            name="vscode",
            files_dir=program_root / "files",
            target_dir=config_root / "Code" / "User",
            packages_file=program_root / "packages.txt",
            files_mode="copy",
        )
