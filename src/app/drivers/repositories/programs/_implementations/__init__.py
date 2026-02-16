from typing import Dict

from src.app.drivers.repositories.programs._implementations.arandr_repository import (
    ArandrRepository,
)
from src.app.drivers.repositories.programs._implementations.bspwm_repository import (
    BspwmRepository,
)
from src.app.drivers.repositories.programs._implementations.kitty_repository import (
    KittyRepository,
)
from src.app.drivers.repositories.programs._implementations.nvidia_repository import (
    NvidiaRepository,
)
from src.app.drivers.repositories.programs._implementations.picom_repository import (
    PicomRepository,
)
from src.app.drivers.repositories.programs._implementations.polybar_repository import (
    PolybarRepository,
)
from src.app.drivers.repositories.programs._implementations.pulseaudio_repository import (
    PulseaudioRepository,
)
from src.app.drivers.repositories.programs._implementations.ranger_repository import (
    RangerRepository,
)
from src.app.drivers.repositories.programs._implementations.rofi_repository import (
    RofiRepository,
)
from src.app.drivers.repositories.programs._implementations.sxhkd_repository import (
    SxhkdRepository,
)
from src.app.drivers.repositories.programs._implementations.thunar_repository import (
    ThunarRepository,
)
from src.app.drivers.repositories.programs._implementations.vscode_repository import (
    VscodeRepository,
)
from src.app.drivers.repositories.programs._implementations.xorg_repository import (
    XorgRepository,
)
from src.core.entities.program_config import ProgramName
from src.core.repositories.programs.program_repository import CoreProgramRepository


def get_program_repositories() -> Dict[ProgramName, CoreProgramRepository]:
    # FIXME: Ponerle un name a cada repo y usar eso en vez de hardcodear el name acá.
    return {
        "arandr": ArandrRepository(),
        "bspwm": BspwmRepository(),
        "kitty": KittyRepository(),
        "nvidia": NvidiaRepository(),
        "picom": PicomRepository(),
        "polybar": PolybarRepository(),
        "pulseaudio": PulseaudioRepository(),
        "ranger": RangerRepository(),
        "rofi": RofiRepository(),
        "sxhkd": SxhkdRepository(),
        "thunar": ThunarRepository(),
        "vscode": VscodeRepository(),
        "xorg": XorgRepository(),
    }
