def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    dq = []
    result = []

    for i, n in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.pop(0)

        while dq and nums[dq[-1]] < n:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    assert sliding_window_maximium([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_maximium([4, 2, 12, 11, -5], 2) == [4, 12, 12, 11]
    assert sliding_window_maximium([9], 1) == [9]
    assert sliding_window_maximium([], 3) == []
    assert sliding_window_maximium([1, 2, 3, 4], 5) == []
    assert sliding_window_maximium([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]
    print("py_sliding_window_maximium: todos os testes passaram ✅")