from time import perf_counter


def timeit_once(func, *args, **kwargs) -> float:
    """Запускает func один раз и возвращает время в секундах"""


    time_start: float = perf_counter()
    func(*args, **kwargs)
    time_end: float = perf_counter()

    return time_end - time_start