import subprocess

from src.core.repositories.command_repository import CommandRepository


class ShellCommandRepository(CommandRepository):
    def run(self, cmd: str) -> None:
        subprocess.run(cmd, shell=True, check=True)

    def run_capture(self, cmd: str) -> str:
        completed = subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            capture_output=True,
        )
        return completed.stdout.strip()
