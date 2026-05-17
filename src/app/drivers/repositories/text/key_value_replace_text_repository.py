from src.core.repositories.text import CoreKeyValueReplaceTextRepository


class KeyValueReplaceTextRepository(CoreKeyValueReplaceTextRepository):
    def replace_text(self, text: str, kv: dict[str, str]) -> str:
        for key, value in kv.items():
            text = text.replace(key, value)
        return text
