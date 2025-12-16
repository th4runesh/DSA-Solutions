def remove_duplicates(arr):
    """
    Removes duplicate elements from the array while preserving order.
    """
    return list(dict.fromkeys(arr))

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 4]
    print("Original Array:", arr)
    print("Array after removing duplicates:", remove_duplicates(arr))