import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Генерирует список из n случайных целых чисел
    Если distinct=True — все элементы будут разными
    """

    if n <= 0 or lo > hi:
        return []

    rng = random.Random(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError('Диапазон слишком мал для уникальных значений')
        return rng.sample(range(lo, hi + 1), n)

    return [rng.randint(lo, hi) for _ in range(n)]
