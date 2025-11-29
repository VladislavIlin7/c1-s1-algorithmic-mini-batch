import random


def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed=None) -> list[float]:
    """
    Возвращает список из n случайных вещественных чисел в указанном диапазоне

    :param n: количество элементов в списке
    :param lo: нижняя граница значений
    :param hi: верхняя граница значений
    :param seed: фиксированное значение генератора случайных чисел
    :return: список случайных чисел типа float
    """

    if n <= 0 or lo > hi:
        return []

    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]