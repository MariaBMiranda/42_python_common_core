def common_elements(lists: list) -> list:
    if len(lists) == 0:
        return []
    return sorted(set(lists[0]).intersection(*lists[1:]))
