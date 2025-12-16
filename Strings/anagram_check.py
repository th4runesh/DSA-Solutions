def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams of each other.
    """
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = "listen"
    s2 = "silent"
    print("String 1:", s1)
    print("String 2:", s2)
    print("Are they anagrams?", is_anagram(s1, s2))
