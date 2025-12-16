def reverse_string(s):
    """
    Returns the reversed version of the input string.
    """
    return s[::-1]

if __name__ == "__main__":
    s = "hello"
    print("Original String:", s)
    print("Reversed String:", reverse_string(s))