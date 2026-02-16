from src.app.drivers.repositories.programs._implementations.bspwm_repository import BspwmRepository
from src.app.drivers.repositories.programs._implementations.display_tools_repository import DisplayToolsRepository
from src.app.drivers.repositories.programs._implementations.hwclock_repository import HwclockRepository
from src.app.drivers.repositories.programs._implementations.kitty_repository import KittyRepository
from src.app.drivers.repositories.programs._implementations.nvidia_repository import NvidiaRepository
from src.app.drivers.repositories.programs._implementations.picom_repository import PicomRepository
from src.app.drivers.repositories.programs._implementations.polybar_repository import PolybarRepository
from src.app.drivers.repositories.programs._implementations.pulseaudio_repository import PulseaudioRepository
from src.app.drivers.repositories.programs._implementations.ranger_repository import RangerRepository
from src.app.drivers.repositories.programs._implementations.rofi_repository import RofiRepository
from src.app.drivers.repositories.programs._implementations.setxkbmap_repository import SetxkbmapRepository
from src.app.drivers.repositories.programs._implementations.sxhkd_repository import SxhkdRepository
from src.app.drivers.repositories.programs._implementations.thunar_repository import ThunarRepository
from src.app.drivers.repositories.programs._implementations.vscode_repository import VscodeRepository
from src.app.drivers.repositories.programs._implementations.wm_base_repository import WmBaseRepository
from src.app.drivers.repositories.programs.program_installer_repository import ProgramInstallerRepository

def get_program_repositories() -> dict[str, ProgramInstallerRepository]:
    # FIXME: Ponerle un name a cada repo y usar eso en vez de hardcodear el name acá.
    return {
        "bspwm": BspwmRepository(),
        "display-tools": DisplayToolsRepository(),
        "hwclock": HwclockRepository(),
        "kitty": KittyRepository(),
        "nvidia": NvidiaRepository(),
        "picom": PicomRepository(),
        "polybar": PolybarRepository(),
        "pulseaudio": PulseaudioRepository(),
        "ranger": RangerRepository(),
        "rofi": RofiRepository(),
        "setxkbmap": SetxkbmapRepository(),
        "sxhkd": SxhkdRepository(),
        "thunar": ThunarRepository(),
        "vscode": VscodeRepository(),
        "wm-base": WmBaseRepository(),
    }
