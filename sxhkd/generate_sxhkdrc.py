""" Genera el fichero sxhkdrc a partir del template.
- Se utiliza `TAG_TO_REPLACE` para modificarlo por el path real.

- Nota: Esto debe hacerse por que sxhkd no acepta bash en su archivo de configuración.
"""
from typing import List
from pathlib import Path
import subprocess
import re

def format_tag(tag: str) -> str:
    return "{{" + f"{tag}" + "}}"

def format_tag_commands(folder_cmd: str = "commands") -> str:
    return format_tag(folder_cmd)

def main() -> None:
    path_config = Path.home() / ".config"
    path_sxhkd = path_config / "sxhkd"
    path_sxhkd_template = path_sxhkd / "sxhkdrc.template"
    with open(path_sxhkd_template, "r") as f:
        text_template = f.read()
    
    # Se reemplazan los tags de commands.
    path_commands = path_config / "commands"
    text_template = text_template.replace(format_tag_commands(path_commands.stem), str(path_commands))

    # Se buscan todos los tags que tengan la forma {{cmd_xxxxx}}.
    pattern = r"\{\{([^\s{}]+)\}\}"
    tags: List[str] = list(set(re.findall(pattern, text_template)))
    for tag in tags:
        pkg_name = tag.split("cmd_")[-1]    # Nombre del paquete (sxhkd, bspwm, ...)
        tag = f"cmd_{pkg_name}"
        path_cmd_pkg = str(path_config / pkg_name / tag)
        text_template = text_template.replace(format_tag(tag), path_cmd_pkg)

    # Se guarda el sxhkdrc modificado del template.
    path_sxhkdrc = path_sxhkd / "sxhkdrc"
    with open(path_sxhkdrc, "w") as f:
        f.write(text_template)
    
    # Se le da permisos de ejecución y reinicia sxhkd.
    subprocess.run(["chmod", "+x", str(path_sxhkdrc)])
    subprocess.run(["pkill", "-USR1", "sxhkd"])

if __name__ == "__main__":
    main()