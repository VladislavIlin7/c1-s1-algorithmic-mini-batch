def radix_sort(a: list[int]) -> list[int]:
    """Сортируем числа по цифрам: сначала по единицам, потом десяткам и дальше"""

    if not a:
        return []

    max_val = max(a)
    exp = 1  # текущий разряд (1, 10, 100, ...)

    while max_val // exp > 0:
        n = len(a)
        output = [0] * n
        count = [0] * 10  # для цифр 0–9

        # считаем частоты цифр
        for x in a:
            digit = (x // exp) % 10
            count[digit] += 1

        # преобразуем частоты в накопленные позиции
        for i in range(1, 10):
            count[i] += count[i - 1]

        # заполняем выходной массив справа налево (стабильность)
        for i in range(n - 1, -1, -1):
            digit = (a[i] // exp) % 10
            count[digit] -= 1
            output[count[digit]] = a[i]

        # копируем обратно
        for i in range(n):
            a[i] = output[i]

        exp *= 10

    return a
