def longest_common_prefix(strs):
    """
    Finds the longest common prefix among a list of strings.
    """
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print("Strings:", strs)
    print("Longest Common Prefix:", longest_common_prefix(strs))
