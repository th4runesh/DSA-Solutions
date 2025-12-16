def longest_consecutive(arr):
    """
    Finds the length of the longest consecutive elements sequence.
    """
    num_set = set(arr)
    longest = 0
    for num in arr:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive sequence length:", longest_consecutive(arr))
