def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 10
    fib_sequence = [fibonacci(i) for i in range(n)]
    print(f"Fibonacci sequence ({n} terms):", fib_sequence)
