def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    return sorted({word for word in words if word.startswith(prefix)})