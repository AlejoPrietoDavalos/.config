from src.core.entities.packages import PackageSpec, Packages
from src.core.entities.program_config import ProgramConfig
from src.core.repositories.program_config.program_build_config_repository import ProgramBuildConfigRepository


class NvidiaConfigRepository(ProgramBuildConfigRepository):
    """NVIDIA policy for this repo.

    We always prefer NVIDIA's proprietary stack installed from distro repos
    (never the manual .run installer from NVIDIA website). In this environment
    the packaged kernel module available in repos is `nvidia-open`.
    """

    def build_config(self) -> ProgramConfig:
        return ProgramConfig(
            name="nvidia",
            packages=Packages(
                packages=[
                    PackageSpec(
                        manager="pacman",
                        names=["nvidia-open", "nvidia-utils", "nvidia-settings", "nvidia-prime"],
                    )
                ]
            ),
        )
