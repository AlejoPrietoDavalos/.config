#!/usr/bin/env python3
"""Set keyboard layout with setxkbmap."""

import argparse

from src.app.drivers.repositories.commands.setxkbmap_repository.repository import (
    ShellSetxkbmapRepository,
)
from src.app.drivers.repositories.commands.shell_command_repository import (
    ShellCommandRepository,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--layout", default="latam")
    args = parser.parse_args()

    repo = ShellSetxkbmapRepository(ShellCommandRepository())
    repo.set_layout(args.layout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
