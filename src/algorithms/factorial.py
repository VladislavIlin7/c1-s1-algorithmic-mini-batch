def factorial(n: int) -> int:
    """
    Вычисляет факториал данного числа итеративным методом

    :param n: целое число
    :return: произведение всех натуральных чисел до n
    """

    if not isinstance(n, int):
        raise TypeError("Факториал определен только для целых чисел")
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")

    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
