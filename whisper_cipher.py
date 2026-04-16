def whisper_cipher(s: str, shift: int) -> str:
    result = ""

    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            new_char = chr((ord(c) - base + shift) % 26 + base)
            result += new_char
        else:
            result += c

    return result


def main():
    print(f"{whisper_cipher('Hello World!', 3)}")


main()
