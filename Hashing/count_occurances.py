def count_elements(arr):
    """
    Counts the frequency of each element using a dictionary (hash map).
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 1, 4, 2]
    print("Element frequencies:", count_elements(arr))
