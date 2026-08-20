def is_rotation(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if arr1 == arr2:
        return True
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False