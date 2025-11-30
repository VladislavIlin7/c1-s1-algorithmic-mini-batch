def cmp_abs(a: int, b: int) -> int:
    return (abs(a) > abs(b)) - (abs(a) < abs(b))


def cmp_len(a, b) -> int:
    a = str(a)
    b = str(b)
    if len(a) == len(b):
        if a == b:
            return 0
        if a > b:
            return 1
        return -1
    if len(a) > len(b):
        return 1
    return -1
