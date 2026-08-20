def nebula_compressor(operation: str, data: str) -> str:
    if operation == "compress":
        result = ""
        i = 0
        while i < len(data):
            char = data[i]
            run = 1
            while i + run < len(data) and data[i + run] == char:
                run += 1
            i += run
            while run:
                chunk = min(run, 9)
                result += char if chunk == 1 else char + str(chunk)
                run -= chunk
        return result

    if operation == "decompress":
        result = ""
        i = 0
        while i < len(data):
            char = data[i]
            if i + 1 < len(data) and data[i + 1].isdigit():
                result += char * int(data[i + 1])
                i += 2
            else:
                result += char
                i += 1
        return result

    return "Error"