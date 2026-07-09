def common_elements(lists: list) -> list:
    if len(lists) == 0:
        return []
    common = set(lists[0]).intersection(*lists[1:])
    result = []
    for item in lists[0]:
        if item in common and item not in result:
            result.append(item)
    return result