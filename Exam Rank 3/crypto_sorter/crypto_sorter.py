def count_vowels(s: str) -> int:
        return sum(1 for c in s.lower() if c in "aeiou")


def crypto_sorter(s: str) -> str:
    return sorted(
        s,
        key=lambda w: (len(w), [ord(c) for c in w], count_vowels(w))
       )


def main():
    print(f"{crypto_sorter(["apple", "Banana", "kiwi", "orange", "Egg"])}")


main()
