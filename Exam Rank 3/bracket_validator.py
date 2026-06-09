def bracket_validator(s: str) -> bool:
    for letter in s:
        if (letter not in "[{()}]"):
            s = s.replace(letter, "")
    for key in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    if s == "":
        return True
    else:
        return False


def main():
    print(f"{bracket_validator("(}")}")
    print(f"{bracket_validator("([)]")}")


main()
