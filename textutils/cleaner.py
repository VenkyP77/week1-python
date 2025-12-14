def remove_special_chars(text: str) -> str:
    """Removes anything that isn't a letter or number."""
    import re

    return re.sub(r"[^A-Za-z0-9 ]", "", text)


def to_lowercase(text: str) -> str:
    return text.lower()
