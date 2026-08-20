def word_ladder_builder(start: str, end: str, word_list: list[str]) -> int:
    if start == end:
        return 1

    words = set(word_list)
    if end not in words:
        return 0

    def differ_by_one(a: str, b: str) -> bool:
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    visited = {start}
    frontier = [start]
    length = 1
    while frontier:
        length += 1
        next_frontier = []
        for word in frontier:
            for candidate in words:
                if candidate not in visited and differ_by_one(word, candidate):
                    if candidate == end:
                        return length
                    visited.add(candidate)
                    next_frontier.append(candidate)
        frontier = next_frontier

    return 0