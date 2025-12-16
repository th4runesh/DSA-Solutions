def binary_search(arr, target):
    """
    Returns the index of target in a sorted array using binary search.
    Returns -1 if not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7
    index = binary_search(arr, target)
    print("Array:", arr)
    print("Target:", target)
    print("Index found:", index)
