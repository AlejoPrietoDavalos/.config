import argparse
from typing import cast

from src.app.drivers.repositories.programs.program_registry_repository import ProgramRegistryRepository
from src.core.entities.program_config import PROGRAM_NAMES, ProgramName
from src.core.use_cases.program_actions import ProgramActions


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--action",
        required=True,
        choices=[
            "install",
            "uninstall",
            "install-requirement",
            "uninstall-requirement",
            "install-files",
            "uninstall-files",
        ],
    )
    parser.add_argument("--program", required=True, choices=PROGRAM_NAMES)
    parser.add_argument("--backup", action="store_true", help="Backup existing files before overwriting/removing")
    args = parser.parse_args()

    actions = ProgramActions(program_registry_repo=ProgramRegistryRepository())
    actions.run(action=args.action, program=cast(ProgramName, args.program), backup=args.backup)


if __name__ == "__main__":
    main()
