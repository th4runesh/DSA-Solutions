def rotate_array(arr, k):
    """
    Rotates the array to the right by k positions.
    """
    k %= len(arr)  # handle k > length of array
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 2
    print("Original Array:", arr)
    print(f"Array after rotating by {k} positions:", rotate_array(arr, k))