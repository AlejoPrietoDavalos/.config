"""Genera `~/.config/sxhkd/sxhkdrc` a partir del template trackeado en `_wm`."""
from pathlib import Path
import re
import subprocess


def format_tag(tag: str) -> str:
    return f"{{{{{tag}}}}}"


def main() -> None:
    path_config = Path.home() / ".config"
    path_sxhkd = path_config / "sxhkd"
    path_template = path_config / "_wm" / "programs" / "sxhkd" / "files" / "sxhkdrc.template"
    path_output = path_sxhkd / "sxhkdrc"
    path_sxhkd.mkdir(parents=True, exist_ok=True)

    text_template = path_template.read_text()

    # Resolve commands location from the current repo layout.
    path_commands = path_config / "_infra" / "commands"
    text_template = text_template.replace(format_tag("commands"), str(path_commands))

    # Replace tags in the form {{cmd_<program>}} -> ~/.config/<program>/cmd
    tags = set(re.findall(r"\{\{([^\s{}]+)\}\}", text_template))
    for tag in tags:
        if not tag.startswith("cmd_"):
            continue
        pkg_name = tag.removeprefix("cmd_")
        path_cmd_pkg = path_config / pkg_name / "cmd"
        text_template = text_template.replace(format_tag(tag), str(path_cmd_pkg))

    path_output.write_text(text_template)
    subprocess.run(["chmod", "+x", str(path_output)], check=False)
    subprocess.run(["pkill", "-USR1", "-x", "sxhkd"], check=False)


if __name__ == "__main__":
    main()
