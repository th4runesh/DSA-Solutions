def two_sum(arr, target):
    """
    Finds two numbers that sum up to target using a hash map.
    """
    lookup = {}
    for i, num in enumerate(arr):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print("Indices with sum", target, ":", two_sum(arr, target))
