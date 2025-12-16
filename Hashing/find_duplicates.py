def find_duplicates(arr):
    """
    Returns a list of duplicates in the array using a hash map.
    """
    freq = {}
    duplicates = []
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count > 1:
            duplicates.append(num)
    return duplicates

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 3, 5, 1]
    print("Duplicates in the array:", find_duplicates(arr))
