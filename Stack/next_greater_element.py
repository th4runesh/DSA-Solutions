def next_greater_element(arr):
    """
    Finds the next greater element for each element in the array.
    """
    stack = []
    result = [-1] * len(arr)

    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] < value:
            index = stack.pop()
            result[index] = value
        stack.append(i)
    return result

if __name__ == "__main__":
    arr = [4, 5, 2, 25]
    print("Array:", arr)
    print("Next Greater Elements:", next_greater_element(arr))
