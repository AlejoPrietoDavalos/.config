import argparse
from typing import cast

from src.app.drivers.repositories.commands.shell_command_repository import ShellCommandRepository
from src.app.drivers.repositories.files.local_backup_repository import LocalBackupRepository
from src.app.drivers.repositories.files.local_file_operations_repository import LocalFileOperationsRepository
from src.app.drivers.repositories.files.local_filesystem_repository import LocalFilesystemRepository
from src.app.drivers.repositories.packages.program_package_manager_repository import ProgramPackageManagerRepository
from src.app.drivers.repositories.program_config.program_config_registry_repository import ProgramConfigRegistryRepository
from src.core.entities.program import PROGRAM_NAMES, ProgramName
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

    fs_repo = LocalFilesystemRepository()
    actions = ProgramActions(
        config_repo=ProgramConfigRegistryRepository(),
        package_repo=ProgramPackageManagerRepository(),
        file_repo=LocalFileOperationsRepository(
            fs_repo=fs_repo,
            backup_repo=LocalBackupRepository(),
        ),
        command_repo=ShellCommandRepository(),
    )
    actions.run(action=args.action, program=cast(ProgramName, args.program), backup=args.backup)


if __name__ == "__main__":
    main()
