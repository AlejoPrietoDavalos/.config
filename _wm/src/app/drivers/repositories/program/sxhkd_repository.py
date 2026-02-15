from pathlib import Path

from src.app.drivers.repositories.program.base_program_repository import BaseProgramRepository
from src.core.entities.program_config import ProgramConfig


class SxhkdRepository(BaseProgramRepository):
    def build(self, config_root: Path) -> ProgramConfig:
        program_root = config_root / "_wm" / "programs" / "sxhkd"
        return ProgramConfig(
            name="sxhkd",
            files_dir=program_root / "files",
            target_dir=config_root / "sxhkd",
            packages_file=program_root / "packages.txt",
            post_install_commands=(f"{config_root}/_wm/scripts/generate_sxhkd.sh",),
        )
