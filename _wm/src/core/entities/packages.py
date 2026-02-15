from dataclasses import dataclass


@dataclass(frozen=True)
class Packages:
    packages: list[str]
