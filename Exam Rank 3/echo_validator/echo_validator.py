def echo_validator(s: str) -> bool:
    filtered = ''.join(letter.lower() for letter in s if letter.isalnum())
    return filtered == filtered[::-1]


def main():
    print(f"1 - A man, a plan, a canal: Panama: {echo_validator('A man, a plan, a canal: Panama')}")
    print(f"2 - race a car: {echo_validator('race a car')}")
    print(f"3 - '': {echo_validator('')}")


main()
