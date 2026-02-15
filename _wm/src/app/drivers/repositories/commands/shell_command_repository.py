import subprocess

from core.repositories.command_repository import CommandRepository


class ShellCommandRepository(CommandRepository):
    def run(self, cmd: str) -> None:
        subprocess.run(cmd, shell=True, check=True)
