from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

PackageManager = Literal["pacman", "yay"]


@dataclass(frozen=True)
class PackageSpec:
    manager: PackageManager
    names: list[str]


@dataclass(frozen=True)
class Packages:
    packages: list[PackageSpec]
