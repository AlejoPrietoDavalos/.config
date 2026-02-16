import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from src.core.repositories.local_file import CoreTmpRepository


class TmpRepository(CoreTmpRepository):
    @contextmanager
    def temporary_path(
        self,
        suffix: str = "",
        filename: str = "tmp",
        directory_prefix: str = "tmp_",
    ) -> Iterator[Path]:
        with tempfile.TemporaryDirectory(prefix=directory_prefix) as tmp_dir:
            yield Path(tmp_dir) / f"{filename}{suffix}"

    @contextmanager
    def temporary_png_path(self) -> Iterator[Path]:
        with self.temporary_path(suffix=".png") as path_png:
            yield path_png
