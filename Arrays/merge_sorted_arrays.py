def merge_sorted_arrays(a, b):
    """
    Merges two sorted arrays into a single sorted array.
    """
    return sorted(a + b)

if __name__ == "__main__":
    a = [1, 3, 5]
    b = [2, 4, 6]
    print("Array 1:", a)
    print("Array 2:", b)
    print("Merged Sorted Array:", merge_sorted_arrays(a, b))