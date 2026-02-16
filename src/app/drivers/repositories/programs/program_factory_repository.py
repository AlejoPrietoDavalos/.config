from typing import Dict

from src.app.drivers.repositories.programs._implementations import (
    get_program_repositories,
)
from src.core.entities.program_config import ProgramName
from src.core.repositories.programs.program_factory_repository import CoreProgramFactoryRepository
from src.core.repositories.programs.program_repository import CoreProgramRepository


class ProgramFactoryRepository(CoreProgramFactoryRepository):
    def __init__(self) -> None:
        self._repos: Dict[str, CoreProgramRepository] = get_program_repositories()

    def get_program_repo(self, program: ProgramName) -> CoreProgramRepository:
        repo = self._repos[program]

        cfg = repo.default_config()
        if cfg.files is not None and not cfg.files.source_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files.source_dir}")
        return repo

    def list_programs(self) -> list[str]:
        programs: list[str] = []
        for name, repo in self._repos.items():
            if hasattr(repo, "default_config"):
                programs.append(name)
        return programs
