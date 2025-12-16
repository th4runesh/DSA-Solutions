def factorial(n):
    """
    Returns the factorial of n using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is:", factorial(num))
