from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

FileMode = Literal["link", "copy"]


@dataclass(frozen=True)
class ProgramConfig:
    name: str
    files_dir: Path
    target_dir: Path
    packages_file: Path
    files_mode: FileMode = "link"
    backup_files: bool = False
    post_install_commands: tuple[str, ...] = field(default_factory=tuple)
