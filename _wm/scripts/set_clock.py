#!/usr/bin/env python3
"""Set timezone and sync hardware clock."""

import argparse

from src.app.drivers.repositories.commands.hwclock_repository.repository import (
    ShellHwclockRepository,
)
from src.app.drivers.repositories.commands.shell_command_repository import (
    ShellCommandRepository,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--timezone",
        default="America/Argentina/Buenos_Aires",
        help="Timezone path under /usr/share/zoneinfo",
    )
    args = parser.parse_args()

    repo = ShellHwclockRepository(ShellCommandRepository())
    repo.set_timezone(args.timezone)
    repo.sync_system_to_hardware()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
