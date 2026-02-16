#!/usr/bin/env python3
"""Apply monitor layout for bspwm using the core use case."""

from src.app.drivers.repositories.programs._implementations.bspc_repository import (
    BspcRepository,
)
from src.app.drivers.repositories.programs._implementations.command_repository import (
    CommandRepository,
)
from src.app.drivers.repositories.programs._implementations.xrandr_repository import (
    XrandrRepository,
)
from src.core.use_cases.apply_monitor_layout import ApplyMonitorLayout


def main() -> int:
    command_repo = CommandRepository()
    use_case = ApplyMonitorLayout(
        xrandr_repo=XrandrRepository(command_repo),
        bspc_repo=BspcRepository(command_repo),
    )
    use_case.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
