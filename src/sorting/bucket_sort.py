def bucket_sort(a: list[float]) -> list[float]:
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
        buckets[i].sort()

    # объединяем результат
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result
