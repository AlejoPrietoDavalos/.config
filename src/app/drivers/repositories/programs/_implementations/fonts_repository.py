import shutil
import subprocess
from pathlib import Path

from src.core.constants import path_config, path_config_files
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.fonts_repository import CoreFontsRepository


class FontsRepository(CoreFontsRepository):
    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="fonts",
            files=ProgramFiles(
                path_folder_config_files_input=path_config_files / "fonts",
                path_folder_program_dotfile=path_config / "fonts",
            ),
            package_dependencies=Packages(
                pkg_specs=[PkgSpec(manager="pacman", names=["ttf-hack-nerd"])]
            ),
            post_install_actions=(self.install_local_fonts,),
        )

    def install_local_fonts(self) -> None:
        source_dir = path_config / "fonts"
        destination_dir = Path.home() / ".local" / "share" / "fonts"

        font_files = self._list_font_files(source_dir)
        if not font_files:
            return

        destination_dir.mkdir(parents=True, exist_ok=True)
        for font_file in font_files:
            shutil.copy2(font_file, destination_dir / font_file.name)

        self._refresh_font_cache(destination_dir)

    def _list_font_files(self, source_dir: Path) -> list[Path]:
        if not source_dir.is_dir():
            return []

        patterns = ("*.ttf", "*.otf", "*.ttc")
        files: list[Path] = []
        for pattern in patterns:
            files.extend(source_dir.glob(pattern))
        return sorted(files)

    def _refresh_font_cache(self, destination_dir: Path) -> None:
        if shutil.which("fc-cache") is None:
            return
        subprocess.run(["fc-cache", "-f", str(destination_dir)], check=False)
