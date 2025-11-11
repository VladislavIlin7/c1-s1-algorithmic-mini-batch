def fibo_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
