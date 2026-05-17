from abc import ABC, abstractmethod


class CoreKeyValueReplaceTextRepository(ABC):
    @abstractmethod
    def replace_text(self, text: str, kv: dict[str, str]) -> str: ...
