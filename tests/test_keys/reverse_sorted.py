def reverse_sorted(n: int) -> list[int]:
    """Массив в обратном порядке"""

    if n <= 0:
        return []
    return list(range(n - 1, -1, -1))
