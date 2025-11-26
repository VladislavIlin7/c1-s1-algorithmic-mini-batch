import random


def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed=None) -> list[float]:
    """Генерирует список из n случайных вещественных чисел"""

    if n <= 0 or lo > hi:
        return []

    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]