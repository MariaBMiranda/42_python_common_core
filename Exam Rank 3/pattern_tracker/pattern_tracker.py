def pattern_tracker(string: str) -> int:
    result = 0
    for i in range(len(string)):
        try:
            a = int(string[i + 1])
            b = int(string[i])
        except:
            continue

        if a - b == 1:
            result += 1

    return result
