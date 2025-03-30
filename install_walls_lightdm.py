"""
- Ejecutar con 'sudo python ...'.
- Ver /etc/lightdm/lightdm-gtk-greeter.conf, lo necesita.
"""
from pathlib import Path
import os

def main() -> None:
    path_walls = Path("resources") / "wallpapers"
    if not path_walls.exists():
        raise Exception("Ejecutar dentro de .config")

    path_walls_out = "/usr/share/wallpapers/"
    os.system(f"sudo mkdir -p {path_walls_out}")
    os.system(f"sudo cp {str(path_walls)}/* {path_walls_out}")

if __name__ == "__main__":
    main()
