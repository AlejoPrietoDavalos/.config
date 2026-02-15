"""
- Ejecutar con 'sudo python ...'.
- Ver /etc/lightdm/lightdm-gtk-greeter.conf, lo necesita.
"""
from pathlib import Path
import os

def main() -> None:
    path_walls = Path(__file__).resolve().parent / "resources" / "wallpapers"
    if not path_walls.exists():
        raise Exception("No se encontro _infra/resources/wallpapers")

    path_walls_out = "/usr/share/wallpapers/"
    os.system(f"sudo mkdir -p {path_walls_out}")
    os.system(f"sudo cp {str(path_walls)}/* {path_walls_out}")

if __name__ == "__main__":
    main()
