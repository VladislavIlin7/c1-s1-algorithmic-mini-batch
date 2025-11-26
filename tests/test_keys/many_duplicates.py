import random


def many_duplicates(n: int, k_unique: int = 5, *, seed=None) -> list[int]:
    """Массив из n элементов, но всего k_unique разных значений"""

    if seed is not None:
        random.seed(seed)

    base = [random.randint(0, 100) for _ in range(k_unique)]

    return [random.choice(base) for _ in range(n)]