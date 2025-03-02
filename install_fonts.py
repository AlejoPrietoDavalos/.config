"""
- Ejecutar con 'sudo python ...'.
"""
from pathlib import Path
import os

def main() -> None:
    path_fonts_in = Path("resources") / "fonts"
    if not path_fonts_in.exists():
        raise Exception("Ejecutar dentro de .config")

    path_fonts_out = "/usr/local/share/fonts"
    os.system(f"mkdir -p {path_fonts_out}")
    os.system(f"sudo cp {str(path_fonts_in)}/*.ttf {path_fonts_out}")

if __name__ == "__main__":
    main()
