from typing import List
from pathlib import Path

path_home = Path.home()
path_config = path_home / ".config"

path_resources = path_config / "_infra" / "resources"
path_wallpapers = path_resources / "wallpapers"

path_resources.mkdir(exist_ok=True)
path_wallpapers.mkdir(exist_ok=True)


def get_paths_wallpaper() -> List[Path]:
    """Return available wallpaper files sorted by name."""
    return sorted([p for p in path_wallpapers.iterdir() if p.is_file()])
