def count_vowels_consonants(s):
    """
    Counts the number of vowels and consonants in a string.
    """
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

if __name__ == "__main__":
    s = "Hello World"
    vowels, consonants = count_vowels_consonants(s)
    print("String:", s)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
