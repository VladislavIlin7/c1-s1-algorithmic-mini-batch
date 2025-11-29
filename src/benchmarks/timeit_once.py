from time import perf_counter


def timeit_once(func, *args, **kwargs) -> float:
    """
    Измеряет время выполнения функции один раз

    :param func: вызываемая функция
    :param args: позиционные аргументы для функции
    :param kwargs: именованные аргументы для функции
    :return: время выполнения в секундах
    """


    time_start: float = perf_counter()
    func(*args, **kwargs)
    time_end: float = perf_counter()

    return time_end - time_start