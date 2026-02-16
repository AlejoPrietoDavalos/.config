import argparse
from typing import cast

from src.app.drivers.repositories.programs import (
    ProgramInstallerRepository,
    ProgramRegistryRepository,
)
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
    args = parser.parse_args()

    actions = ProgramActions(
        program_factory_repo=ProgramRegistryRepository(),
        program_installer_repo=ProgramInstallerRepository(),
    )
    actions.run(action=args.action, program=cast(ProgramName, args.program))


if __name__ == "__main__":
    main()
