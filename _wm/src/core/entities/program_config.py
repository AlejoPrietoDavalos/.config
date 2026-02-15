from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from src.core.entities.packages import Packages
from src.core.entities.program import ProgramName

FileMode = Literal["link", "copy"]


@dataclass(frozen=True)
class ProgramConfig:
    name: ProgramName
    files_dir: Path | None = None
    target_dir: Path | None = None
    packages: Packages
    dependencies: tuple[ProgramName, ...] = field(default_factory=tuple)
    files_mode: FileMode = "link"
    backup_files: bool = False
    post_install_commands: tuple[str, ...] = field(default_factory=tuple)
