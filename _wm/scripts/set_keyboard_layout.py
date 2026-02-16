#!/usr/bin/env python3
"""Set keyboard layout with setxkbmap."""

import argparse

from src.app.drivers.repositories.programs.setxkbmap_repository import (
    SetxkbmapRepository,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--layout", default="latam")
    args = parser.parse_args()

    repo = SetxkbmapRepository()
    repo.set_layout(args.layout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
