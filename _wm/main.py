#!/usr/bin/env python3
import argparse
from pathlib import Path

from app.drivers.repositories.commands.shell_command_repository import ShellCommandRepository
from app.drivers.repositories.files.local_backup_repository import LocalBackupRepository
from app.drivers.repositories.files.local_file_operations_repository import LocalFileOperationsRepository
from app.drivers.repositories.files.local_filesystem_repository import LocalFilesystemRepository
from app.drivers.repositories.packages.pacman_package_repository import PacmanPackageRepository
from app.drivers.repositories.program.program_registry_repository import ProgramRegistryRepository
from core.use_cases.program_actions import ProgramActions


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
    parser.add_argument("--program", required=True)
    parser.add_argument("--backup", action="store_true", help="Backup existing files before overwriting/removing")
    args = parser.parse_args()

    config_root = Path.home() / ".config"
    fs_repo = LocalFilesystemRepository()
    actions = ProgramActions(
        config_repo=ProgramRegistryRepository(config_root=config_root),
        package_repo=PacmanPackageRepository(),
        file_repo=LocalFileOperationsRepository(
            fs_repo=fs_repo,
            backup_repo=LocalBackupRepository(config_root=config_root),
        ),
        command_repo=ShellCommandRepository(),
    )
    actions.run(action=args.action, program=args.program, backup=args.backup)


if __name__ == "__main__":
    main()
