#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from typing import cast

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.app.drivers.repositories.programs._implementations.playerctl_repository import (
    PlayerctlRepository,
)
from src.core.repositories.programs._implementations.playerctl_repository import (
    PlayerctlAction,
)

def main(action: PlayerctlAction) -> int:
    repo = PlayerctlRepository()
    repo.run(action)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["previous", "next", "play_pause", "stop"])
    args = parser.parse_args()
    raise SystemExit(main(cast(PlayerctlAction, args.action)))
