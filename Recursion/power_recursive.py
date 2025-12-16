def power(x, n):
    """
    Computes x raised to the power n using recursion.
    """
    if n == 0:
        return 1
    return x * power(x, n - 1)

if __name__ == "__main__":
    x = 2
    n = 8
    print(f"{x} raised to the power {n} is:", power(x, n))
