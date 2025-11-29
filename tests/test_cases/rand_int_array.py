import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Возвращает список из n случайных целых чисел в диапазоне от lo до hi

    :param n: количество элементов
    :param lo: минимально возможное целое значение
    :param hi: максимально возможное целое значение
    :param distinct: если True все элементы будут разными
    :param seed: фиксированное значение генератора случайных чисел
    :return: список случайных целых чисел
    """

    if n <= 0 or lo > hi:
        return []

    rng = random.Random(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError('Диапазон слишком мал для уникальных значений')
        return rng.sample(range(lo, hi + 1), n)

    return [rng.randint(lo, hi) for _ in range(n)]
