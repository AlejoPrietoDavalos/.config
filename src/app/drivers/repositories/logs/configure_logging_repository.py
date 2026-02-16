import logging
from pathlib import Path

from src.core.repositories.logs import CoreConfigureLoggingRepository


class ConfigureLoggingRepository(CoreConfigureLoggingRepository):
    def configure(self, level: int = logging.INFO, path_logs: Path | None = None) -> None:
        kwargs: dict[str, object] = {
            "level": level,
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "force": True,
        }
        if path_logs is not None:
            path_logs.mkdir(parents=True, exist_ok=True)
            path_log_file = path_logs / "log.log"
            kwargs["handlers"] = [logging.FileHandler(path_log_file, encoding="utf-8")]
        logging.basicConfig(**kwargs)

