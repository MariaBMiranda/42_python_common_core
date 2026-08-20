def count_consecutive_digit_pairs(s: str) -> int:
    count = 0

    for i in range(len(s) - 1):
        if ord(s[i+1]) == ord(s[i]) + 1:
            count += 1

    return (count)


def main():
    print(count_consecutive_digit_pairs("1112233335"))
    print(count_consecutive_digit_pairs("1234"))
    print(count_consecutive_digit_pairs("1111"))


main()
