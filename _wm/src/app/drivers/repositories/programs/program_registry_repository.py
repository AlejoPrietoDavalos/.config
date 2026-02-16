from typing import Dict

from src.core.entities.program_config import ProgramName
from src.core.repositories.programs.program_factory_repository import CoreProgramFactoryRepository
from src.core.repositories.programs.program_repository import CoreProgramRepository
from src.app.drivers.repositories.programs import get_program_repositories


class ProgramRegistryRepository(CoreProgramFactoryRepository):
    def __init__(self) -> None:
        self._repos: Dict[ProgramName, CoreProgramRepository] = get_program_repositories()

    def get_program_repo(self, program: ProgramName) -> CoreProgramRepository:
        repo = self._repos[program]

        cfg = repo.default_config()
        if cfg.files is not None and not cfg.files.source_dir.is_dir():
            raise ValueError(f"Missing files dir: {cfg.files.source_dir}")
        return repo
