def twist_permutation(lst: list[int], n: int) -> list[int]:
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


def main():
    print(twist_permutation([1, 2, 3, 4, 5], 2))


main()
