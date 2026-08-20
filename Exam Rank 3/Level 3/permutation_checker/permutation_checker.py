def permutation_checker(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    res1 = permutation_checker("Listen", "Silent")
    print(f"Resultado listen e silent: {res1}")

    res2 = permutation_checker("amor", "roma")
    print(f"Resultado de amor/roma: {res2}")


main()
