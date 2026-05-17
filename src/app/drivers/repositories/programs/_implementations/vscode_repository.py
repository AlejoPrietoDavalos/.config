import json
import re
from pathlib import Path
from typing import Any

from src.core.constants import path_config_files, path_dotfiles
from src.core.entities.program_config import PkgSpec, Packages
from src.core.entities.program_config import ProgramConfig, ProgramFiles
from src.core.repositories.programs._implementations.vscode_repository import CoreVscodeRepository

_TOKEN_RE = re.compile(r"\{\{([a-zA-Z0-9_.]+)\}\}")


def _resolve_token(path: str, palette: dict[str, Any]) -> str:
    node: Any = palette
    for key in path.split("."):
        if isinstance(node, list):
            node = node[int(key)]
        elif isinstance(node, dict):
            if key not in node:
                raise KeyError(f"Token '{path}' not found in palette (missing '{key}')")
            node = node[key]
        else:
            raise KeyError(f"Token '{path}' not resolvable past '{key}'")
    if not isinstance(node, str):
        raise ValueError(
            f"Token '{path}' did not resolve to a string (got {type(node).__name__})"
        )
    return node


def _render_settings_from_template(
    path_template: Path, path_palette: Path, path_output: Path
) -> None:
    template = path_template.read_text(encoding="utf-8")
    palette = json.loads(path_palette.read_text(encoding="utf-8"))
    rendered = _TOKEN_RE.sub(lambda m: _resolve_token(m.group(1), palette), template)
    path_output.write_text(rendered, encoding="utf-8")


class VscodeRepository(CoreVscodeRepository):
    # TODO: Renombrar a "code"
    def default_config(self) -> ProgramConfig:
        path_folder_vscode = path_config_files / "vscode"
        path_config_folder = path_folder_vscode / "_config"
        path_template = path_config_folder / "template_settings.jsonc"
        path_palette = path_config_folder / "config_aquamarine.json"
        path_output = path_folder_vscode / "settings.json"

        def render_settings() -> None:
            _render_settings_from_template(path_template, path_palette, path_output)

        return ProgramConfig(
            name="vscode",
            files=ProgramFiles(
                path_folder_config_files_input=path_folder_vscode,
                path_folder_program_dotfile=path_dotfiles / "Code" / "User",
            ),
            package_dependencies=Packages(pkg_specs=[PkgSpec(manager="yay", names=["code"])]),
            pre_install_actions=(render_settings,),
        )
