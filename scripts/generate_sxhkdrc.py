"""Genera `~/.config/sxhkd/sxhkdrc` a partir del template trackeado en `programs`."""
from pathlib import Path
import subprocess


def main() -> None:
    # TODO: Crear un repo que tenga toda la lógica para reemplazar un TAG, y tener este
    # generador de configuraciones, en este caso lo uso para sxhkd, pero sirve para cualquiera.
    # TODO: Meter dentro de clean architecture.
    path_config = Path.home() / ".config"
    path_sxhkd = path_config / "sxhkd"
    path_template = path_config / "programs" / "sxhkd" / "files" / "sxhkdrc.template"
    path_output = path_sxhkd / "sxhkdrc"
    path_sxhkd.mkdir(parents=True, exist_ok=True)

    text_template = path_template.read_text()

    path_output.write_text(text_template)
    subprocess.run(["chmod", "+x", str(path_output)], check=False)
    subprocess.run(["pkill", "-USR1", "-x", "sxhkd"], check=False)


if __name__ == "__main__":
    main()
