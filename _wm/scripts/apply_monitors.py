#!/usr/bin/env python3
"""Apply monitor layout for bspwm using the core use case."""

from src.app.drivers.repositories.commands.bspc_repository.repository import (
    ShellBspcRepository,
)
from src.app.drivers.repositories.commands.shell_command_repository import (
    ShellCommandRepository,
)
from src.app.drivers.repositories.commands.xrandr_repository.repository import (
    ShellXrandrRepository,
)
from src.core.use_cases.apply_monitor_layout import ApplyMonitorLayout


def main() -> int:
    command_repo = ShellCommandRepository()
    use_case = ApplyMonitorLayout(
        xrandr_repo=ShellXrandrRepository(command_repo),
        bspc_repo=ShellBspcRepository(command_repo),
    )
    use_case.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
