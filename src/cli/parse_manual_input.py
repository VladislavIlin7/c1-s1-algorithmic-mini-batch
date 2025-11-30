def parse_manual_input(algo_name: str, line: str) -> list[int] | list[float] | None:
    """
    Разбор ручного ввода с учетом ограничений алгоритма
    """
    # bucket: любые вещественные
    if algo_name == "bucket":
        try:
            return [float(x) for x in line.split()]
        except ValueError:
            print("Ошибка ввода: нужны числа (вещественные)")
            return None

    # radix: только неотрицательные целые
    if algo_name == "radix":
        try:
            arr = [int(x) for x in line.split()]
            if any(n < 0 for n in arr):
                raise ValueError("Числа должны быть ≥ 0")
            return arr
        except ValueError:
            print("Для radix сортировки нужны неотрицательные целые числа")
            return None

    # остальные: произвольные целые
    try:
        return [int(x) for x in line.split()]
    except ValueError:
        print("Ошибка ввода: нужны целые числа")
        return None