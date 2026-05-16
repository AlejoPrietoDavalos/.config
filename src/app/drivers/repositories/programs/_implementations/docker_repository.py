import logging
import os
import subprocess

from src.app.drivers.repositories.shell.command_repository import CommandRepository
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs._implementations.docker_repository import CoreDockerRepository
from src.core.repositories.shell.command_repository import CoreCommandRepository

logger = logging.getLogger(__name__)


class DockerRepository(CoreDockerRepository):
    def __init__(self, command_repo: CoreCommandRepository | None = None) -> None:
        self._command_repo = command_repo or CommandRepository()

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="docker",
            package_dependencies=Packages(
                pkg_specs=[PkgSpec(manager="pacman", names=["docker", "docker-compose"])]
            ),
            post_install_actions=(self.enable_and_start_service, self.configure_docker_group),
        )

    def enable_and_start_service(self) -> None:
        if not self._command_repo.command_exists("systemctl"):
            logger.warning("[docker] [post install skip] systemctl not found")
            return
        try:
            self._command_repo.run_argv(["sudo", "systemctl", "enable", "--now", "docker.service"])
        except subprocess.CalledProcessError:
            logger.info("[docker] [post install retry] falling back to enable + start")
            self._command_repo.run_argv(["sudo", "systemctl", "enable", "docker.service"])
            self._command_repo.run_argv(["sudo", "systemctl", "start", "docker.service"])

    def configure_docker_group(self) -> None:
        if self._command_repo.run_argv_quiet(["getent", "group", "docker"]) != 0:
            self._command_repo.run_argv(["sudo", "groupadd", "docker"])

        user = os.environ.get("USER", "").strip()
        if not user:
            logger.warning("[docker] [post install skip] USER env var not available")
            return

        user_groups = self._command_repo.run_argv_capture(["id", "-nG", user]).split()
        if "docker" not in user_groups:
            self._command_repo.run_argv(["sudo", "usermod", "-aG", "docker", user])
            logger.info(
                "[docker] [post install] user added to docker group; relogin/reboot required"
            )
