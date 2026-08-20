def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid = [["."] * size for _ in range(size)]

    for x, y in stars:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = "*"

    return ["".join(row) for row in grid]


if __name__ == "__main__":
    # --- Testes com os exemplos do subject ---
    assert constellation_mapper([(0, 0), (2, 2)], 3) == ['*..', '...', '..*']
    assert constellation_mapper([(1, 0), (1, 2)], 3) == ['.*.', '...', '.*.']
    assert constellation_mapper([(0, 1), (5, 5)], 3) == ['...', '*..', '...']
    assert constellation_mapper([], 2) == ['..', '..']
    assert constellation_mapper([(0, 0)], 0) == []
    assert constellation_mapper([(0, 0), (0, 0)], 2) == ['*.', '..']
    assert constellation_mapper([(-1, 0), (0, -1)], 2) == ['..', '..']
    print("py_constellation_mapper: todos os testes passaram ✅")
