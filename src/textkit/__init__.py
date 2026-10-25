import re

from unidecode import unidecode


def slugify(text: str) -> str:
    text = unidecode(text).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def truncate(text: str, n: int) -> str:
    return text if len(text) <= n else text[: n - 1] + "…"
