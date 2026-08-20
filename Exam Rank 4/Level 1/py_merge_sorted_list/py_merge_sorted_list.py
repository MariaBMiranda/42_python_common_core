def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    pointers = [0] * len(lists) 
    result = []

    while True:
        best_val = None
        best_i = -1
        for i, lst in enumerate(lists):
            p = pointers[i]
            if p < len(lst):
                if best_val is None or lst[p] < best_val:
                    best_val = lst[p]
                    best_i = i
        if best_i == -1:
            break
        result.append(best_val)
        pointers[best_i] += 1

    return result


if __name__ == "__main__":
    assert merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_sorted_list([[1, 2, 3], [], [0, 4]]) == [0, 1, 2, 3, 4]
    assert merge_sorted_list([]) == []
    assert merge_sorted_list([[], []]) == []
    assert merge_sorted_list([[-5, -1, 7]]) == [-5, -1, 7]
    assert merge_sorted_list([[2, 2], [2]]) == [2, 2, 2]
    print("py_merge_sorted_list: todos os testes passaram ✅")