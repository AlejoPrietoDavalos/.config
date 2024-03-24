""" Genera el fichero sxhkdrc a partir del template.
- Se utiliza `TAG_TO_REPLACE` para modificarlo por el path real.

- Nota: Esto debe hacerse por que sxhkd no acepta bash en su archivo de configuración.
"""
from pathlib import Path
import subprocess

def main(tag_to_replace: str) -> None:
    path_sxhkd_folder = Path.home() / ".config" / "sxhkd"
    path_sxhkd_scripts = path_sxhkd_folder / "scripts"
    path_sxhkd_template = path_sxhkd_folder / "sxhkdrc.template"

    with open(path_sxhkd_template, "r") as f:
        lines = f.readlines()

    # Se reemplazan los tags.
    lines = [line.replace(tag_to_replace, str(path_sxhkd_scripts)) for line in lines]

    # Se guarda el sxhkdrc modificado del template.
    path_sxhkdrc = path_sxhkd_folder / "sxhkdrc"
    with open(path_sxhkdrc, "w") as f:
        f.write("".join(lines))
    
    # Se le da permisos de ejecución y reinicia sxhkd.
    subprocess.run(["chmod", "+x", str(path_sxhkdrc)])
    subprocess.run(["pkill", "-USR1", "sxhkd"])

if __name__ == "__main__":
    # Este es el tag que reemplazará con el path real de los scripts.
    TAG_TO_REPLACE = "{{path_scripts}}"
    main(TAG_TO_REPLACE)