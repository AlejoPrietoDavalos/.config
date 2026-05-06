#!/usr/bin/env python3
"""Apply monitor layout for bspwm using the core use case."""

from src.app.drivers.repositories.logs import ConfigureLoggingRepository
from src.app.drivers.repositories.programs._implementations.bspwm_repository import (
    BspwmRepository,
)
from src.app.drivers.repositories.programs._implementations.xrandr_repository import (
    XrandrRepository,
)
from src.core.use_cases.apply_monitor_layout import ApplyMonitorLayoutService

REVERSE_MONITOR_LAYOUT = False


def main() -> int:
    configure_logging_repo = ConfigureLoggingRepository()
    configure_logging_repo.configure(log_filename="apply_monitors.log")
    use_case = ApplyMonitorLayoutService(
        xrandr_repo=XrandrRepository(),
        bspwm_repo=BspwmRepository(),
        reverse_monitor_layout=REVERSE_MONITOR_LAYOUT,
    )
    use_case.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
