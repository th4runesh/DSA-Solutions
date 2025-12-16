def is_balanced(s):
    """
    Checks if all parentheses in the string are balanced.
    """
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    s = "{[()()]}"
    print("String:", s)
    print("Balanced?", is_balanced(s))
