def factorial_recursive(n: int) -> int:
    """
    Вычисляет факториал данного числа рекурсивным методом

    :param n: целое число
    :return: произведение всех натуральных чисел до n
    """

    if not isinstance(n, int):
        raise TypeError("Факториал определен только для целых чисел")
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
