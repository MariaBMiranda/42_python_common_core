def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    directions = [
        ("H",   (0,  1)),  ("H-",  (0, -1)),
        ("V",   (1,  0)),  ("V-",  (-1, 0)),
        ("D1",  (1,  1)),  ("D1-", (-1,-1)),
        ("D2",  (1, -1)),  ("D2-", (-1, 1)),
    ]
    if not grid or not pattern:
        return []

    matches = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for name, (dr, dc) in directions:
                if _fits(grid, pattern, row, col, dr, dc):
                    matches.append((row, col, name))

    if pattern == pattern[::-1]:
        return matches[:1]
    return matches


def _fits(grid, pattern, row, col, dr, dc):
    for i, ch in enumerate(pattern):
        r, c = row + dr * i, col + dc * i
        if not (0 <= r < len(grid) and 0 <= c < len(grid[r])):
            return False
        if grid[r][c] != ch:
            return False
    return True