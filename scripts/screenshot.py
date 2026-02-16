#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.app.drivers.repositories.programs._implementations.scrot_repository import (
    ScrotRepository,
)
from src.app.drivers.repositories.programs._implementations.xclip_repository import (
    XclipRepository,
)
from src.app.drivers.repositories.local_file import TmpRepository
from src.app.drivers.repositories.logs import ConfigureLoggingRepository
from src.core.use_cases.take_screenshot import TakeScreenshotService


def main(mode: str, with_save: int) -> int:
    configure_logging_repo = ConfigureLoggingRepository()
    configure_logging_repo.configure(log_filename=f"{Path(__file__).stem}.log")
    use_case = TakeScreenshotService(
        scrot_repo=ScrotRepository(),
        xclip_repo=XclipRepository(),
        tmp_repo=TmpRepository(),
    )
    use_case.run(mode=mode, with_save=with_save)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["bbox", "focused", "full_screen"])
    parser.add_argument("with_save", type=int, choices=[0, 1])
    args = parser.parse_args()
    raise SystemExit(main(args.mode, args.with_save))
