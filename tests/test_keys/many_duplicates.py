import random


def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> list[int]:
    """Массив из n элементов, но всего k_unique разных значений"""

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