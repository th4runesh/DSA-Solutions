def is_palindrome(s):
    """
    Checks if the string is a palindrome.
    """
    return s == s[::-1]

if __name__ == "__main__":
    s = "racecar"
    print("String:", s)
    print("Is Palindrome?", is_palindrome(s))