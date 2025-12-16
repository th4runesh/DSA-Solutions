def linear_search(arr, target):
    """
    Returns the index of target in arr using linear search.
    Returns -1 if not found.
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30
    index = linear_search(arr, target)
    print("Array:", arr)
    print("Target:", target)
    print("Index found:", index)
