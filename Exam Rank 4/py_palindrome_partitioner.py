def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0

    is_pal = [[False] * n for _ in range(n)]

    cuts = [0] * n

    for i in range(n):
        min_cut = i
        for j in range(i + 1):
            if s[j] == s[i] and (i - j < 2 or is_pal[j + 1][i - 1]):
                is_pal[j][i] = True
                if j == 0:
                    min_cut = 0
                else:
                    min_cut = min(min_cut, cuts[j - 1] + 1)

        cuts[i] = min_cut

    return cuts[n - 1]


if __name__ == "__main__":
    assert palindrome_partitioner("aab") == 1
    assert palindrome_partitioner("aba") == 0
    assert palindrome_partitioner("abc") == 2
    assert palindrome_partitioner("abac") == 1
    assert palindrome_partitioner("abcd") == 3
    assert palindrome_partitioner("") == 0
    assert palindrome_partitioner("noon") == 0
    print("py_palindrome_partitioner: todos os testes passaram ✅")
