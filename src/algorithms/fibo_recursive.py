def fibo_recursive(n: int) -> int:
    """
    Вычисляет n-ное число в последовательности Фибоначчи рекурсивным методом

    :param n: целое число
    :return: n-ное число в последовательности Фибоначчи
    """

    if not isinstance(n, int):
        raise TypeError("Последовательность Фибоначчи определена только для целых чисел")
    if n < 0:
        raise ValueError("Последовательность Фибоначчи не определена на отрицательных числах")

    if n <= 1:
        return n
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
