from pathlib import Path

path_home = Path.home()
path_dotfiles = path_home / ".config"
path_wm = path_dotfiles / "_wm"
path_wm_programs = path_wm / "programs"
path_wm_scripts = path_wm / "scripts"
