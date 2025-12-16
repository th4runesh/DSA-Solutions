from collections import defaultdict

def group_anagrams(words):
    """
    Groups words that are anagrams of each other using a hash map.
    """
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    print("Grouped Anagrams:", grouped)
