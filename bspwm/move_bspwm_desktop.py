"""
# Ejecutar con 'sudo -E python ...' para exportar las variables de entorno.
"""
from pathlib import Path
import os

BSPWM_DESKTOP = "bspwm.desktop"

path_bspwm = Path(os.getenv("PATH_BSPWM"))
path_bspwm_desktop_in = path_bspwm / BSPWM_DESKTOP
path_bspwm_desktop_out = Path("/usr/share/xsessions") / BSPWM_DESKTOP

# Levanto el archivo y cambio el path.
file_txt = path_bspwm_desktop_in.read_text()
file_txt = file_txt.replace("{{PATH_BSPWM}}", str(path_bspwm))

# Guardo el archivo.
with open(path_bspwm_desktop_out, "w") as f:
    f.write(file_txt)
