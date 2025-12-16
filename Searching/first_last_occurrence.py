def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    print("Array:", arr)
    print("Target:", target)
    print("First Occurrence Index:", first_occurrence(arr, target))
    print("Last Occurrence Index:", last_occurrence(arr, target))
