import random


def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> list[int]:
    """
    Возвращает список из n чисел содержащий только k_unique разных значений

    :param n: количество элементов в списке
    :param k_unique: сколько уникальных чисел должно быть в результате
    :param seed: фиксированное значение для генератора случайных чисел
    :return: список чисел с большим количеством повторов
    """

    if n <= 0:
        return []

    if k_unique < 1:
        raise ValueError("k_unique должно быть >= 1")

    # если уникальных больше чем элементов, сокращаем
    if k_unique > n:
        k_unique = n

    if seed is not None:
        rng = random.Random(seed)
    else:
        rng = random

    base = [rng.randint(0, n) for _ in range(k_unique)]

    return [rng.choice(base) for _ in range(n)]