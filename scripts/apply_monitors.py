#!/usr/bin/env python3
"""Apply monitor layout for bspwm using the core use case."""

from src.app.drivers.repositories.programs import ProgramFactoryRepository
from src.core.use_cases.apply_monitor_layout import ApplyMonitorLayoutService


def main() -> int:
    program_factory_repo = ProgramFactoryRepository()
    use_case = ApplyMonitorLayoutService(
        xrandr_repo=program_factory_repo.get_program_repo("xrandr"),
        bspwm_repo=program_factory_repo.get_program_repo("bspwm"),
    )
    use_case.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
