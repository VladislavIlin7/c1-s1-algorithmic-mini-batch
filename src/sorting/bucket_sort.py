from src.sorting.quick_sort import quick_sort


def bucket_sort(a: list[float]) -> list[float]:
    """
    Быстрая сортировка O(n log n) в среднем

    :param a: список элементов одного типа
    :param key: функция получения ключа сортировки
    :param cmp: функция сравнения двух элементов
    :return: новый отсортированный список
    """

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
