from src.sorting.quick_sort import quick_sort


def bucket_sort(a: list[float]) -> list[float]:
    """Разбиваем числа по «корзинам», внутри корзин сортируем и объединяем результат."""

    if not a:
        return []

    n = len(a)
    minimum = min(a)
    maximum = max(a)

    if minimum == maximum:
        return a[:]

    # создаём корзины
    buckets = [[] for _ in range(n)]

    # распределяем элементы по корзинам
    for value in a:
        index = int((value - minimum) / (maximum - minimum) * (n - 1))
        buckets[index].append(value)

    # сортируем каждую корзину
    for i in range(n):
        buckets[i] = quick_sort(buckets[i])

    # объединяем результат
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result
