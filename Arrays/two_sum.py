def two_sum(arr, target):
    """
    Returns indices of two numbers that add up to target.
    """
    d = {}
    for i, num in enumerate(arr):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print("Array:", arr)
    print(f"Indices of two numbers summing to {target}:", two_sum(arr, target))