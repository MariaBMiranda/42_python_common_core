def number_base_converter(s: str, base_from: int, base_to: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= base_from <= 36) or not (2 <= base_to <= 36):
        return "ERROR"

    s = s.upper().strip().split()[0]
    if not s:
        return "ERROR"

    num = 0
    for char in s:
        if char not in digits[:base_from]:
            return "ERROR"
        val = digits.index(char)
        num = num * base_from + val

    value = ""
    while num > 0:
        rest = num % base_to
        value = digits[rest] + value
        num //= base_to

    return value


def main():
    print(number_base_converter("1011", 2, 10))
    print(number_base_converter("1A", 16, 2))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 36))
    print(number_base_converter("z", 36, 10))


main()
