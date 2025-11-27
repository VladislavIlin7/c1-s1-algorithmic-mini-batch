import random


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """Почти отсортированный массив (range(n)), но с random swaps перестановками."""

    if n <= 0:
        return []

    if seed is not None:
        random.seed(seed)

    arr = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr
