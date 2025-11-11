def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
