import os
import shutil
import tempfile
import logging
from pathlib import Path
from typing import Literal

from src.core.constants import path_screenshots
from src.core.repositories.programs._implementations.scrot_repository import CoreScrotRepository
from src.core.repositories.programs._implementations.xclip_repository import CoreXclipRepository


CaptureMode = Literal["bbox", "focused", "full_screen"]
SaveMode = Literal[0, 1]

logger = logging.getLogger(__name__)


class TakeScreenshotService:
    def __init__(
        self,
        scrot_repo: CoreScrotRepository,
        xclip_repo: CoreXclipRepository,
        path_output_folder: Path = path_screenshots,
    ) -> None:
        self._scrot_repo = scrot_repo
        self._xclip_repo = xclip_repo
        self._path_output_folder = path_output_folder

    def run(self, mode: CaptureMode, with_save: SaveMode) -> Path | None:
        fd_tmp, path_tmp = tempfile.mkstemp(suffix=".png")
        os.close(fd_tmp)
        tmp_png = Path(path_tmp)
        logger.info("Screenshot started | mode=%s | with_save=%s", mode, with_save)
        try:
            self._capture(mode, tmp_png)
            logger.info("Capture done: %s", tmp_png)
            self._xclip_repo.copy_png_to_clipboard(tmp_png)
            logger.info("Image copied to clipboard")

            if with_save == 1:
                path_output = self._next_screenshot_path()
                shutil.move(str(tmp_png), str(path_output))
                logger.info("Screenshot saved: %s", path_output)
                return path_output
            logger.info("Screenshot completed without file save")
            return None
        except Exception:
            logger.exception("Screenshot flow failed")
            raise
        finally:
            tmp_png.unlink(missing_ok=True)

    def _capture(self, mode: CaptureMode, path_output_png: Path) -> None:
        if mode == "bbox":
            self._scrot_repo.capture_bbox(path_output_png)
            return
        if mode == "focused":
            self._scrot_repo.capture_focused(path_output_png)
            return
        self._scrot_repo.capture_full_screen(path_output_png)

    def _next_screenshot_path(self) -> Path:
        self._path_output_folder.mkdir(parents=True, exist_ok=True)
        current_indexes = [
            int(path_png.stem)
            for path_png in self._path_output_folder.glob("*.png")
            if path_png.stem.isdigit()
        ]
        next_index = (max(current_indexes) + 1) if current_indexes else 1
        return self._path_output_folder / f"{next_index}.png"
