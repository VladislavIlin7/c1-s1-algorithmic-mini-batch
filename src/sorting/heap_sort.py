def heapify(arr: list[int], heap_size: int, i: int) -> None:
    # просейка вниз без рекурсии
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest  # продолжаем просейку ниже

def heap_sort(a: list[int]) -> list[int]:
    n = len(a)
    # построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    # извлечение максимума
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)
    return a