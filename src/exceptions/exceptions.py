class ApplicationException(Exception):
    """Базовая ошибка"""
    def __init__(self, error: str):
        super().__init__(f"{error}")

class StackIsEmptyException(ApplicationException):
    def __init__(self):
        super().__init__("Стэк пуст")

class CmpAndKeyTogetherException(ApplicationException):
    def __init__(self):
        super().__init__("Нельзя одновременно передавать key и cmp")