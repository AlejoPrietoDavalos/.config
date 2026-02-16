from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.programs.nvidia_repository import CoreNvidiaRepository


class NvidiaRepository(CoreNvidiaRepository):
    """NVIDIA policy for this repo.

    We always prefer NVIDIA's proprietary stack installed from distro repos
    (never the manual .run installer from NVIDIA website). In this environment
    the packaged kernel module available in repos is `nvidia-open`.
    """

    def default_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="nvidia",
            packages=Packages(
                pkg_specs=[
                    PkgSpec(
                        manager="pacman",
                        names=["nvidia-open", "nvidia-utils", "nvidia-settings", "nvidia-prime"],
                    )
                ]
            ),
        )
