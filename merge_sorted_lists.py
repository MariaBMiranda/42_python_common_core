def merge_sorted_lists(nums1: list[int], nums2: list[int]) -> list[int]:
    return sorted(nums1 + nums2)


def main():
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))


main()
